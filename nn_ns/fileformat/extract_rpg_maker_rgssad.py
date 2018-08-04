import struct
import io
import os
import re

uint32_fmt = struct.Struct('<L')
rgssad_file_id = b'RGSSAD\x00'
key_mask = 0x0fFFFfFFF
byte_mask = 0x0ff
rgssad_file_version_this_module_supported = {1, 3}
rgssad_file_header_fmt = struct.Struct(str(len(rgssad_file_id)) + 'sB')
size_fmt = uint32_fmt
rgssad_file_encoding = 'utf-8'
key_fmt = uint32_fmt
offset_fmt = uint32_fmt
gen_key_v1 = lambda key: (key * 7 + 3) & key_mask
key_len = 4

def unpack_from_file(fmt, file):
    return fmt.unpack(file.read(fmt.size))

def xor_cipher(key, message):
    # version 2: use int for bitwise operator
    if 0 == len(message): return b''
    assert len(key) > 0
    keys = key * (len(message) // len(key) + 1)
    keys = keys[:len(message)]
    ikey = int.from_bytes(keys, 'little')
    imsg = int.from_bytes(message, 'little')
    iret = ikey ^ imsg
    return iret.to_bytes(len(message), 'little')

def _open_version_1(rgssad_file, file_size, subfiles):pass
def _open_version_3(rgssad_file, file_size, subfiles):pass


def open_rpg_maker_rgssad_file(file_name):
    file_size = os.path.getsize(file_name)
    with open(file_name, 'rb') as rgssad_file:
        rgssad_file_id_in_file, version = unpack_from_file(rgssad_file_header_fmt, rgssad_file)
        assert rgssad_file_id_in_file == rgssad_file_id
        assert version in rgssad_file_version_this_module_supported
        #_open = getattr(__name__, '_open_version_' + str(version))
        _open = globals()['_open_version_' + str(version)]
        subfiles, decrypt_subfile_method = _open(rgssad_file, file_size)

    return subfiles, decrypt_subfile_method

def _decrypt_subfile_v1(subfile_data, key):
    gen = gen_key_v1
    ls = bytearray()
    for i in range(len(subfile_data) // key_len + 1):
        ls += key.to_bytes(key_len, 'little')
        key = gen(key)
    return xor_cipher(ls, subfile_data)

_decrypt_subfile_v3 = _decrypt_subfile_v1

def _open_version_1(rgssad_file, file_size):
    subfiles = {}
    rgssad_file.seek(rgssad_file_header_fmt.size)
    key = 0x0DEADCAFE
    gen = gen_key_v1
    def read_size(rgssad_file, key):
        size, = unpack_from_file(size_fmt, rgssad_file)
        size = size ^ key
        key = gen(key)
        return (size, key)
    def decrypt_bytes(bs, key):
        L = len(bs)
        ls = bytearray(L)
        for i in range(L):
            ls[i] = key & byte_mask
            key = gen(key)
        return xor_cipher(ls, bs), key
    while rgssad_file.tell() < file_size:
        len_of_subfile_name, key = read_size(rgssad_file, key)
        subfile_name = rgssad_file.read(len_of_subfile_name)
        subfile_name, key = decrypt_bytes(subfile_name, key)
        subfile_name = subfile_name.decode(encoding = rgssad_file_encoding)
        subfile_size, key = read_size(rgssad_file, key)
        assert subfile_name not in subfiles
        subfiles[subfile_name] = {'name': subfile_name,
                                  'offset': rgssad_file.tell(),
                                  'size': subfile_size,
                                  'key': key}
        rgssad_file.seek(subfile_size, os.SEEK_CUR)
    assert file_size == rgssad_file_header_fmt.size + \
           len(subfiles) * (size_fmt.size*2) + \
           sum(len(subfile_name.encode(encoding = rgssad_file_encoding)) + \
               info['size'] for subfile_name, info in subfiles.items())
    return subfiles, _decrypt_subfile_v1

def _open_version_3(rgssad_file, file_size):
    subfiles = {}
    rgssad_file.seek(rgssad_file_header_fmt.size)
    key, = unpack_from_file(key_fmt, rgssad_file)
    key = (key * 9 + 3) & key_mask
    bs_key = key.to_bytes(key_len, 'little')
    read1 = lambda rgssad_file, fmt, key: unpack_from_file(fmt, rgssad_file)[0] ^ key
    while True:
        subfile_offset = read1(rgssad_file, offset_fmt, key)
        if not subfile_offset: break
        subfile_size = read1(rgssad_file, size_fmt, key)
        subfile_key = read1(rgssad_file, key_fmt, key)
        len_of_subfile_name = read1(rgssad_file, size_fmt, key)
        subfile_name = rgssad_file.read(len_of_subfile_name)
        subfile_name = xor_cipher(bs_key, subfile_name)
        subfile_name = subfile_name.decode(encoding = rgssad_file_encoding)
        assert subfile_name not in subfiles
        subfiles[subfile_name] = {'name': subfile_name,
                                  'offset': subfile_offset,
                                  'size': subfile_size,
                                  'key': subfile_key}
    assert file_size == rgssad_file_header_fmt.size + key_fmt.size + \
           len(subfiles) * (offset_fmt.size + size_fmt.size*2 + key_fmt.size) + \
           size_fmt.size + \
           sum(len(subfile_name.encode(encoding = rgssad_file_encoding)) + \
               info['size'] for subfile_name, info in subfiles.items())
    return subfiles, _decrypt_subfile_v3


        
def extract_subfile(to_file, rgssad_file, entry, decrypt_method):
    rgssad_file.seek(entry['offset'])
    subfile = rgssad_file.read(entry['size'])
    subfile = decrypt_method(subfile, entry['key'])
    to_file.write(subfile)
    return

def extract_rpg_maker_rgssad_file(to_path, file_name, subfiles, decrypt_method):
    with open(file_name, 'rb') as rgssad_file:
        for subfile_name, entry in subfiles.items():
            path = os.path.join(to_path, subfile_name)
            where = os.path.dirname(os.path.abspath(path))
            os.makedirs(where,exist_ok=True)
            # what if 'path' be removed here? f*ck!
            try:
                with open(path, 'xb') as subfile:
                    extract_subfile(subfile, rgssad_file, entry, decrypt_method)
            except FileExistsError as fee:
                subfile_size = os.path.getsize(path)
                if subfile_size != entry['size']: raise
                with open(path, 'rb') as existed_file, io.BytesIO() as new_file:
                    extract_subfile(new_file, rgssad_file, entry, decrypt_method)
                    if existed_file.read(subfile_size) != new_file.getvalue(): raise

def t2():
    path = r'C:\game\To the Moon/To the Moon.rgssad'
    path = r'E:\temp_output\clip/[to_the_moon]Game.rgssad'
    to = r'C:\game\To the Moon/unpack/'
    subfiles, decrypt_method = open_rpg_maker_rgssad_file(path)
    #s = set()
    #for name in subfiles: s.add(name.split('\\')[0])
    #print(s)
    #with open(to+'names.txt', 'w') as out: out.write(str(subfiles.keys()))
    extract_rpg_maker_rgssad_file(to, path, subfiles, decrypt_method)
    return

def t1():
    path = r'C:\game\To the Moon/To the Moon.rgssad'
    open_rpg_maker_rgssad_file(path)


vb_source_from = 'RPG Maker Decrypter::frmMain.vb'
frmMain.vb = '''
Imports System.IO
Imports System.Text

Public Class frmMain

#Region "Program Variables"
    Const MAX_FILES As Integer = 10000

    Dim sAllFilter As String = "|All Files|*.*"
    Dim sFilter As String = "RPG Maker Encrypted Files|*.rgssad;*.rgss2a;*.rgss3a" & sAllFilter
    Dim sTitle As String = "Open RPG Maker Encrypted File"

    Dim sRoot As String = Application.StartupPath & "\"
    Dim sExtract As String = sRoot & "Extract\"

    Dim sOpenPath, sSavePath As String

    Dim numFiles As Integer
    Dim bVersion As Byte
    Dim iKey As Integer = 0
    Dim bAbort As Boolean = False

    ' File Data
    Dim FILE_Offset(MAX_FILES) As Integer
    Dim FILE_Size(MAX_FILES) As Integer
    Dim FILE_Key(MAX_FILES) As Integer
    Dim FILE_Name(MAX_FILES) As String

#End Region

#Region "Menu"

    Private Sub mnuOpen_Click(sender As System.Object, e As System.EventArgs) Handles mnuOpen.Click
        If OpenFileDlg(sFilter, sTitle, sOpenPath) Then
            bVersion = GetVersion(sOpenPath)

            Select Case bVersion
                Case 1
                    iKey = &HDEADCAFE
                    ReadRGSSADV1(sOpenPath)
                    Exit Select
                Case 3
                    ReadRGSSADV3(sOpenPath)
                    Exit Select
                Case -1
                    MsgBox("Error Reading file, no RGSSAD HEADER!")
                    Exit Select
                Case Else
                    MsgBox("Unknown Version: " & bVersion)
                    Exit Select
            End Select

        End If
    End Sub

    Private Sub mnuExit_Click(sender As System.Object, e As System.EventArgs) Handles mnuExit.Click
        Me.Close()
    End Sub

    Private Sub mnuExtractSelected_Click(sender As System.Object, e As System.EventArgs) Handles mnuExtractSelected.Click
        Dim x As Integer = lstItems.SelectedIndex

        If x > -1 Then
            Try
                ExtractFile(x)
            Catch ex As Exception
                MsgBox(ex.ToString)
                Exit Sub
            End Try
        End If
        MsgBox("Success!")
    End Sub

    Private Sub mnuExtractAllFiles_Click(sender As System.Object, e As System.EventArgs) Handles mnuExtractAllFiles.Click
        Me.Enabled = False

        pbFiles.Minimum = 0
        pbFiles.Maximum = numFiles - 1
        pbFiles.Value = 0

        Try
            For i As Integer = 0 To numFiles - 1

                ExtractFile(i)

                ' Update progress
                pbFiles.Value = i
                Application.DoEvents()

            Next i
        Catch ex As Exception
            MsgBox(ex.ToString)
            Me.Enabled = True
            Exit Sub
        End Try

        MsgBox("Success!")
        Me.Enabled = True
    End Sub

#End Region

#Region "I/O Files"

    Private Function GetVersion(ByVal sPath As String) As SByte
        Dim result As SByte = -1

        Dim br As New BinaryReader(File.OpenRead(sPath))

        If ReadCString(br, 7) = "RGSSAD" Then
            result = br.ReadSByte()
        End If

        br.Close()

        Return result
    End Function

    Private Sub ReadRGSSADV1(ByVal sPath As String)
        Dim length As Integer
        Dim br As New BinaryReader(File.OpenRead(sPath))
        lstItems.Items.Clear()
        numFiles = 0
        bAbort = False

        br.BaseStream.Seek(8, SeekOrigin.Begin)
        Do
            length = DecryptIntV1(br.ReadInt32())
            FILE_Name(numFiles) = DecryptNameV1(br.ReadBytes(length))
            FILE_Size(numFiles) = DecryptIntV1(br.ReadInt32())
            FILE_Offset(numFiles) = br.BaseStream.Position
            FILE_Key(numFiles) = iKey
            lstItems.Items.Add(FILE_Name(numFiles))

            br.BaseStream.Seek(FILE_Size(numFiles), SeekOrigin.Current)
            If br.BaseStream.Position = br.BaseStream.Length Then bAbort = True
            numFiles += 1
        Loop Until bAbort = True

        br.Close()
    End Sub

    Private Sub ReadRGSSADV3(ByVal sPath As String)
        Dim length As Integer
        Dim br As New BinaryReader(File.OpenRead(sPath))
        lstItems.Items.Clear()
        numFiles = 0
        bAbort = False

        br.BaseStream.Seek(8, SeekOrigin.Begin)

        iKey = br.ReadInt32()
        iKey *= 9
        iKey += 3

        Do
            FILE_Offset(numFiles) = DecryptIntV3(br.ReadInt32())
            FILE_Size(numFiles) = DecryptIntV3(br.ReadInt32())
            FILE_Key(numFiles) = DecryptIntV3(br.ReadInt32())
            length = DecryptIntV3(br.ReadInt32())

            If FILE_Offset(numFiles) = 0 Then
                bAbort = True
            Else
                FILE_Name(numFiles) = DecryptNameV3(br.ReadBytes(length))
                lstItems.Items.Add(FILE_Name(numFiles))

                numFiles += 1
            End If
        Loop Until bAbort = True

        br.Close()
    End Sub

#End Region

#Region "Functions"

    Private Function DecryptIntV1(ByVal value As Integer) As Integer
        Dim result As Integer = value Xor iKey

        iKey *= 7
        iKey += 3

        Return result
    End Function

    Private Function DecryptIntV3(ByVal value As Integer) As Integer
        Return value Xor iKey
    End Function

    Private Function DecryptNameV1(ByVal bNameEnc As Byte()) As String
        Dim result As String = ""
        Dim name_dec(bNameEnc.Length - 1) As Byte

        ' decrypt name
        For i As Integer = 0 To bNameEnc.Length - 1
            name_dec(i) = bNameEnc(i) Xor (iKey And &HFF)

            iKey *= 7
            iKey += 3
        Next i

        'decrypted name to string
        result = Encoding.UTF8.GetString(name_dec)

        Return result
    End Function

    Private Function DecryptNameV3(ByVal bNameEnc As Byte()) As String
        Dim result As String = ""
        Dim name_dec(bNameEnc.Length - 1) As Byte

        ' key to byte array
        Dim key As Byte() = BitConverter.GetBytes(iKey)

        ' decrypt name
        Dim j As Integer = 0
        For i As Integer = 0 To bNameEnc.Length - 1
            If j = 4 Then j = 0
            name_dec(i) = bNameEnc(i) Xor key(j)
            j += 1
        Next i

        'decrypted name to string
        result = Encoding.UTF8.GetString(name_dec)

        Return result
    End Function

    Private Function DecryptFileData(ByVal bFileData As Byte(), ByVal key As Integer) As Byte()
        Dim fDecrypt(bFileData.Length - 1) As Byte

        Dim iTempKey As Integer = key
        Dim bTempKey As Byte() = BitConverter.GetBytes(key)
        Dim j As Integer = 0

        For i As Integer = 0 To bFileData.Length - 1

            If j = 4 Then
                j = 0
                iTempKey *= 7
                iTempKey += 3
                bTempKey = BitConverter.GetBytes(iTempKey)
            End If

            fDecrypt(i) = bFileData(i) Xor bTempKey(j)

            j += 1
        Next i

        Return fDecrypt
    End Function

    Private Sub ExtractFile(ByVal fnmb As Integer)
        If sOpenPath <> "" Then
            Dim fData As Byte()
            Dim sOutFile As String = sExtract & FILE_Name(fnmb)

            Dim br As New BinaryReader(File.OpenRead(sOpenPath))
            br.BaseStream.Seek(FILE_Offset(fnmb), SeekOrigin.Begin)
            fData = br.ReadBytes(FILE_Size(fnmb))
            br.Close()

            If Directory.Exists(Path.GetDirectoryName(sOutFile)) = False Then
                Directory.CreateDirectory(Path.GetDirectoryName(sOutFile))
            End If

            DeleteFileIfExist(sOutFile)

            Dim bw As New BinaryWriter(File.OpenWrite(sOutFile))

            If bVersion = 1 Or bVersion = 3 Then
                bw.Write(DecryptFileData(fData, FILE_Key(fnmb)))
            End If

            bw.Close()

        End If
    End Sub

#End Region

#Region "Form"

    Private Sub lstItems_SelectedIndexChanged(sender As System.Object, e As System.EventArgs) Handles lstItems.SelectedIndexChanged
        Dim x As Integer = lstItems.SelectedIndex

        If x > -1 Then
            txtOffset.Text = FILE_Offset(x)
            txtSize.Text = FILE_Size(x)
            txtKey.Text = String.Format("0x{0:X8}", FILE_Key(x))
            txtName.Text = FILE_Name(x)
        End If
    End Sub

    Private Sub btnXP_Click(sender As System.Object, e As System.EventArgs) Handles btnXP.Click
        Dim sOutPath As String = sRoot & "Game.rxproj"
        DeleteFileIfExist(sOutPath)

        Dim sw As New StreamWriter(sOutPath)
        sw.Write(txtXP.Text)
        sw.Close()

    End Sub

    Private Sub btnVX_Click(sender As System.Object, e As System.EventArgs) Handles btnVX.Click
        Dim sOutPath As String = sRoot & "Game.rvproj"
        DeleteFileIfExist(sOutPath)

        Dim sw As New StreamWriter(sOutPath)
        sw.Write(txtVX.Text)
        sw.Close()

    End Sub

    Private Sub btnVXAce_Click(sender As System.Object, e As System.EventArgs) Handles btnVXAce.Click
        Dim sOutPath As String = sRoot & "Game.rvproj2"
        DeleteFileIfExist(sOutPath)

        Dim sw As New StreamWriter(sOutPath)
        sw.Write(txtVXAce.Text)
        sw.Close()

    End Sub

#End Region

End Class

'''



r'''
update1:
    "ScreenBufferSize"=dword:00460060
    ==>> "ScreenBufferSize"=dword:012c0060
    ; 0x46 ==>> 70 lines
    ; at most 70 lines can occur on screen
    ; 0x12c ==>> 300 lines

######################## prototype baseline
#see: HKEY_CURRENT_USER__Console[comment][20180927].reg

Windows Registry Editor Version 5.00

; comment
; cmd.exe setting
; [HKEY_CURRENT_USER\Console]
; or [HKEY_CURRENT_USER\Console\cmd.exe]
; or [HKEY_CURRENT_USER\Console\%SystemRoot%_system32_cmd.exe]???
; mine is [HKEY_CURRENT_USER\Console\%SystemRoot%_system32_cmd.exe]
; but I set them all
[HKEY_CURRENT_USER\Console]
"InsertMode"=dword:00000001
"QuickEdit"=dword:00000001

"FullScreen"=dword:00000001
"ScreenBufferSize"=dword:012c0060
"WindowSize"=dword:00190060
    ; HKCU\Console\WindowSize
    ; 0x190050 = (0x19, 0x50) = (25, 80) = (height, width)
    ;
"CursorSize"=dword:00000064
"FontSize"=dword:00180000
"FontWeight"=dword:00000190
"HistoryBufferSize"=dword:00000032
"HistoryNoDup"=dword:00000001
"NumberOfHistoryBuffers"=dword:00000004

; encoding
"CodePage"=dword:000003a8
"FaceName"="新宋体"
"FontFamily"=dword:00000036

"CurrentPage"=dword:00000001
"PopupColors"=dword:000000f5
"ScreenColors"=dword:00000070
"ColorTable00"=dword:00000000
"ColorTable01"=dword:00800000
"ColorTable02"=dword:00008000
"ColorTable03"=dword:00808000
"ColorTable04"=dword:00000080
"ColorTable05"=dword:00800080
"ColorTable06"=dword:00008080
"ColorTable07"=dword:00c0c0c0
"ColorTable08"=dword:00808080
"ColorTable09"=dword:00ff0000
"ColorTable10"=dword:0000ff00
"ColorTable11"=dword:00ffff00
"ColorTable12"=dword:000000ff
"ColorTable13"=dword:00ff00ff
"ColorTable14"=dword:0000ffff
"ColorTable15"=dword:00ffffff
"EnableColorSelection"=dword:00000000
"ExtendedEditKey"=dword:00000000
"ExtendedEditKeyCustom"=dword:00000000

"LoadConIme"=dword:00000001
"TrimLeadingZeros"=dword:00000000
"WordDelimiters"=dword:00000000


[HKEY_CURRENT_USER\Console\%SystemRoot%_system32_cmd.exe]
"ScreenColors"=dword:00000002

"FullScreen"=dword:00000001
"ScreenBufferSize"=dword:00460060
"WindowSize"=dword:00190060

[HKEY_CURRENT_USER\Console\C:_Python32_python.exe]
"ScreenColors"=dword:00000080
"FontSize"=dword:001c0000

[HKEY_CURRENT_USER\Console\cmd.exe]
"ScreenColors"=dword:00000002

"FullScreen"=dword:00000001
"ScreenBufferSize"=dword:00460060
"WindowSize"=dword:00190060
'''


__all__ = ['update_cmd_reg_setting']

from seed.windows.winreg_helper import reg_create, reg_update_from_table, reg_update_from_value_table

from ast import literal_eval
import winreg

def make_typed_value(s:str):
    s = s.strip()
    if not s: raise TypeError
    elif s == '-':
        # delete
        return None
    elif s[0] == '"':
        value = literal_eval(s)
        assert type(value) is str
        if '\0' in value: raise TypeError # REG_SZ contains '\0'
        return (winreg.REG_SZ, value)
    elif s.startswith('dword:'):
        xdigits = s[len('dword:'):]
        if len(xdigits) != 8: raise TypeError
        value = int(xdigits, 16)
        return (winreg.REG_DWORD, value)
    else:
        raise NotImplementedError('make_typed_value({s!r})')

def _mk_value_table_values(value_name2string):
    value_table = \
        {k:make_typed_value(s)
        for k, s in value_name2string.items()
        }
    return value_table

def make_value_table_HKCU_Console():
    value_name2string =\
        {"InsertMode":"dword:00000001"
        ,"QuickEdit":"dword:00000001"

        ,"FullScreen":"dword:00000001"
        ,"ScreenBufferSize":"dword:012c0060"
        ,"WindowSize":"dword:00190060"
            # HKCU\Console\WindowSize
            # 0x190050 = (0x19, 0x50) = (25, 80) = (height, width)
            #
        ,"CursorSize":"dword:00000064"
        ,"FontSize":"dword:00180000"
        ,"FontWeight":"dword:00000190"
        ,"HistoryBufferSize":"dword:00000032"
        ,"HistoryNoDup":"dword:00000001"
        ,"NumberOfHistoryBuffers":"dword:00000004"

        # encoding
        ,"CodePage":"dword:000003a8"
        ,"FaceName":"\"新宋体\""
        ,"FontFamily":"dword:00000036"

        ,"CurrentPage":"dword:00000001"
        ,"PopupColors":"dword:000000f5"
        ,"ScreenColors":"dword:00000070"
        ,"ColorTable00":"dword:00000000"
        ,"ColorTable01":"dword:00800000"
        ,"ColorTable02":"dword:00008000"
        ,"ColorTable03":"dword:00808000"
        ,"ColorTable04":"dword:00000080"
        ,"ColorTable05":"dword:00800080"
        ,"ColorTable06":"dword:00008080"
        ,"ColorTable07":"dword:00c0c0c0"
        ,"ColorTable08":"dword:00808080"
        ,"ColorTable09":"dword:00ff0000"
        ,"ColorTable10":"dword:0000ff00"
        ,"ColorTable11":"dword:00ffff00"
        ,"ColorTable12":"dword:000000ff"
        ,"ColorTable13":"dword:00ff00ff"
        ,"ColorTable14":"dword:0000ffff"
        ,"ColorTable15":"dword:00ffffff"
        ,"EnableColorSelection":"dword:00000000"
        ,"ExtendedEditKey":"dword:00000000"
        ,"ExtendedEditKeyCustom":"dword:00000000"

        ,"LoadConIme":"dword:00000001"
        ,"TrimLeadingZeros":"dword:00000000"
        ,"WordDelimiters":"dword:00000000"
        }

    value_table_HKCU_Console = \
        _mk_value_table_values(value_name2string)
    return value_table_HKCU_Console


def make_value_table_HKCU_Console_SystemRoot_system32_cmd_exe():
    value_name2string = \
        {"ScreenColors":"dword:00000002"

        ,"FullScreen":"dword:00000001"
        ,"ScreenBufferSize":"dword:012c0060"
        ,"WindowSize":"dword:00190060"
        }

    value_table_HKCU_Console_SystemRoot_system32_cmd_exe = \
        _mk_value_table_values(value_name2string)
    return value_table_HKCU_Console_SystemRoot_system32_cmd_exe

def make_value_table_HKCU_Console_cmd_exe():
    value_name2string = \
        {"ScreenColors":"dword:00000002"

        ,"FullScreen":"dword:00000001"
        ,"ScreenBufferSize":"dword:012c0060"
        ,"WindowSize":"dword:00190060"
        }

    value_table_HKCU_Console_cmd_exe = \
        _mk_value_table_values(value_name2string)
    return value_table_HKCU_Console_cmd_exe


key_name_HKCU_Console_SystemRoot_system32_cmd_exe = '%SystemRoot%_system32_cmd.exe'
key_name_HKCU_Console_cmd_exe = 'cmd.exe'
two_cmd_key_names = \
    [key_name_HKCU_Console_SystemRoot_system32_cmd_exe
    # exclude [HKEY_CURRENT_USER\Console\C:_Python32_python.exe]
    ,key_name_HKCU_Console_cmd_exe
    ]

def make_table_HKCU_Console():
    table_HKCU_Console = \
    ({key_name_HKCU_Console_SystemRoot_system32_cmd_exe
        :({}, make_value_table_HKCU_Console_SystemRoot_system32_cmd_exe())
     ,key_name_HKCU_Console_cmd_exe
        :({}, make_value_table_HKCU_Console_cmd_exe())
    },make_value_table_HKCU_Console()
    )
    return table_HKCU_Console

def update_cmd_reg_setting():
    table_del_two_cmd_keys = (dict.fromkeys(two_cmd_key_names), {})
    table_HKCU_Console = make_table_HKCU_Console()
    with reg_create('HKEY_CURRENT_USER', 'Console') as key_Console:
        reg_update_from_table(key_Console, table_del_two_cmd_keys)
        reg_update_from_table(key_Console, table_HKCU_Console)

if __name__ in ('__main__', '__run_as_main__') or __name__.endswith('.__run_as_main__'):
    update_cmd_reg_setting()


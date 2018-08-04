
#import re, io

#from stream_search import search_all

def to_hex(bytes_):
    return ''.join( [ r'\x{:0>2X}'.format(x) for x in bytes_ ] )

def _find_all(obj, sub, begin, end):
    step = len(sub)
    idx = 0
    idc = []
    while idx >= 0:
        idx = obj.find(sub, begin, end)
        if idx == -1:
            break

        begin = idx + step
        idc.append(idx)

    return idc

def test_find_all():
    s = b'24, 2424'
    sub = b'24'
    begin = 0
    end = 7

    assert [0, 4] == _find_all(s, sub, begin, end)

test_find_all()

def _search_all(bytes_, file_obj, times = 2**10, min_buffer = 2**20):
    L = len(bytes_) * times
    L = max(L, min_buffer)

    head = b''
    offset = 0
    sub = bytes_
    assert len(sub) > 0

    idc = []
    while file_obj:
        bs = head + file_obj.read(L)
        if len(bs) < len(sub):
            break
        
        begin = 0
        _idc = _find_all(bs, sub, 0, len(bs))
        for idx in _idc:
            idc.append(offset + idx)

        
        head = bs[-len(sub)+1:]
        offset += len(bs) - len(head)

    return idc

def test_search_all():
    import io
    sub = b'22'
    file_obj = io.BytesIO(b'222222')

    assert [0, 2, 4] == _search_all(sub, file_obj, 1, 3)
    
test_search_all()

def search_all(key, fname):
    with open(fname, 'rb') as f:
        return _search_all(key, f)


def binary_replace(old, new, fname):
    assert len(old) == len(new)
    assert type(old) == type(new) == bytes

    #old = to_hex(old)

    locations = search_all(old, fname)

    L = len(old)
    with open(fname, 'r+b') as f:
        for loc in locations:
            f.seek(loc)
            assert old == f.read(L)
            
            f.seek(loc)
            f.write(new)


def t():
    import io, os
    
    s = \
        '''./Enginio.pyd
./plugins/designer/pyqt5.dll
./plugins/PyQt5/pyqt5qmlplugin.dll
./QAxContainer.pyd
./Qsci.pyd
./Qt.pyd
./QtCore.pyd
./QtDesigner.pyd
./QtGui.pyd
./QtHelp.pyd
./QtMultimedia.pyd
./QtMultimediaWidgets.pyd
./QtNetwork.pyd
./QtOpenGL.pyd
./QtPositioning.pyd
./QtPrintSupport.pyd
./QtQml.pyd
./QtQuick.pyd
./QtQuickWidgets.pyd
./QtSensors.pyd
./QtSerialPort.pyd
./QtSql.pyd
./QtSvg.pyd
./QtTest.pyd
./QtWebKit.pyd
./QtWebKitWidgets.pyd
./QtWebSockets.pyd
./QtWidgets.pyd
./QtWinExtras.pyd
./QtXmlPatterns.pyd
./_QOpenGLFunctions_ES2.pyd
'''

    path = 'C:\Python33\Lib\site-packages\PyQt5/'
    old = b'python34'
    new = b'python33'
    
    fs = io.StringIO(s)
    for f in fs:
        fname = os.path.join(path, f[2:-1])
        binary_replace(old, new, fname)

#t()



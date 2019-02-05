from django.shortcuts import render

# Create your views here.

#new:
from django.http import HttpResponse
try:
    from ..mzitu_com_project.DATA import (
        website_per_page_url_tpl, per_page_url_regex
        , echo_proxy_name, echo_proxy_query_key)
    from ..mzitu_com_project.per_page_transform import (
        per_page_transform__url)
except (ImportError, ValueError):
    from mzitu_com_project.DATA import (
        website_per_page_url_tpl, per_page_url_regex
        , echo_proxy_name, echo_proxy_query_key)
    from mzitu_com_project.per_page_transform import (
        per_page_transform__url)


def per_mzitu__page_view(request):
    path = request.path.lower()
    m = per_page_url_regex.fullmatch(path)
    if m is None: raise Exception(path)
    str_NUMBER = m['NUMBER']
    old_url = 'https://' + website_per_page_url_tpl.format(NUMBER=str_NUMBER)

    scheme = request.scheme
    host = request.get_host()
    proxy_url_prefix = f'{scheme}://{host}/{echo_proxy_name}/?{echo_proxy_query_key}='
    per_page = per_page_transform__url(old_url, proxy_url_prefix)
    return HttpResponse(per_page)


    #print(dir(request))
    attrs = ['COOKIES', 'FILES', 'GET', 'META', 'POST'
        , '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post_parse_error', '_read_started', '_set_post', '_stream', '_upload_handlers'
        , 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']
    for attr in attrs:
        obj = getattr(request, attr)
        if callable(obj):
            try:
                obj = obj()
            except:
                pass
        print(f'request.{attr} = {obj!r}')

    per_page = per_page_transform__url(old_url, proxy_url_prefix)
    return HttpResponse(per_page)



r'''
request.COOKIES = {'csrftoken': 'ftXZQWEGtWNiHS739KtU5l7baX5FpxozWRYdoy4I2v7tKniWtyJhaMnqaM35FRJ
G'}
request.FILES = <MultiValueDict: {}>
request.GET = <QueryDict: {}>
request.META = {
    '7Z': 'py -m nn_ns.fileformat.zip_by_7z'
    , 'ALLUSERSPROFILE': 'C:\\ProgramData'
    , 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming'
    , 'APR_ICONV_PATH': 'C:\\Program Files (x86)\\Subversion\\iconv'
    , 'BATS_PATH': 'E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat'
    , 'BJJ': 'b2 toolset=msvc --build-dir=D:\\temp_output\\build_dir --stagedir=D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36 address-model=64 architecture=x86 target-os=windows --build-type=complete --layout=versioned threading=multi variant=release runtime-link=shared '
    , 'BOOST': 'D:\\software\\programming\\library\\boost\\boost_1_55_0'
    , 'BOOST_BUILD_OPTIONS': '--build-dir=D:\\temp_output\\build_dir --stagedir=D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36 address-model=64  architecture=x86 target-os=windows --build-type=complete --layout=versioned threading=multi variant=release runtime-link=shared'
    , 'BOOST_BUILD_STAGEDIR': 'D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36', 'BOOST_LIB': 'D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36\\lib', 'CLANGHOME': 'D:\\software\\programming\\LLVM\\clang6\\bin'
    , 'CLANG_LIBCXX_INCLUDE': 'D:\\software\\programming\\LLVM\\clang-6.0.0\\libcxx-6.0.0.src'
    , 'CLASSPATH': 'E:\\my_data\\program_source\\java_src'
    , 'CL_PY': '/Fo /LD /MD /EHsc /IC:\\Python36\\include /ID:\\software\\programming\\library\\boost\\boost_1_55_0 /link /LIBPATH:D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36\\lib /LIBPATH:C:\\Python36\\libs'
    , 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files'
    , 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files'
    , 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files'
    , 'COMPUTERNAME': 'ZGC-20120617LVJ'
    , 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe'
    , 'FFMPEG_BIN': 'D:\\software\\media\\converter\\ffmpeg\\ffmpeg-4.0.2\\bin'
    , 'FFMPEG_HOME': 'D:\\software\\media\\converter\\ffmpeg\\ffmpeg-4.0.2'
    , 'FP_NO_HOST_CHECK': 'NO'
    , 'GCCHOME': 'C:\\mingw64\\x86_64-8.1.0-release-posix-seh-rt'
    , 'GITDIR': 'D:\\software\\Internet\\download_tool\\git\\PortableGit-2.11.1-64-bit\\'
    , 'HASKELL_BINS_PREV': 'C:\\Program Files\\Haskell Platform\\8.0.2\\\\lib\\extralibs\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\\\bin'
    , 'HASKELL_BINS_SUCC': 'C:\\Program Files\\Haskell Platform\\8.0.2\\\\mingw\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\cabal\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\local\\bin'
    , 'HASKELL_HOME': 'C:\\Program Files\\Haskell Platform\\8.0.2\\'
    , 'HASKELL_ROAMING': 'C:\\Users\\Administrator\\AppData\\Roaming'
    , 'HOMEDRIVE': 'C:'
    , 'HOMEPATH': '\\Users\\Administrator'
    , 'JDKHOME': 'D:\\software\\programming\\Java\\jdk8u25'
    , 'LANG': 'zh_CN'
    , 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local'
    , 'LOGONSERVER': '\\\\ZGC-20120617LVJ'
    , 'MATHEMATICA_HOME': 'C:\\Program Files\\Wolfram Research\\Mathematica\\9.0'
    , 'MYSQLHOME': 'D:\\software\\database\\RDBMS\\MySQL\\mysql-5.6.20-winx64'
    , 'NUMBER_OF_PROCESSORS': '2'
    , 'OCAMLLIB': 'D:\\software\\programming\\ML\\OCaml\\lib'
    , 'OS': 'Windows_NT'
    , 'PATH': 'D:\\software\\programming\\gcc\\tool\\UnxUtils\\usr\\local\\wbin;D:\\software\\media\\converter\\ffmpeg\\ffmpeg-4.0.2\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\\\lib\\extralibs\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\\\bin;D:\\software\\programming\\Java\\jdk8u25\\bin;D:\\software\\programming\\library\\boost\\boost_1_55_0\\tools\\build\\v2;D:\\software\\programming\\swig\\swigwin-3.0.2;D:\\software\\programming\\LLVM\\clang6\\bin;C:\\mingw64\\x86_64-8.1.0-release-posix-seh-rt\\bin;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Program Files\\Microsoft Windows Performance Toolkit\\;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py33\\lib;D:\\software\\programming\\ML\\OCaml\\bin;C:\\Program Files\\Haskell\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\lib\\extralibs\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\mingw\\bin;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files\\ImageMagick-6.8.9-Q8;C:\\Program Files\\ImageMagick-6.8.9-Q16;C:\\Program Files (x86)\\GnuPG\\bin;D:\\software\\media\\book\\tex\\TeX_Live\\2016\\bin\\win32;C:\\Program Files (x86)\\Pandoc\\;C:\\Program Files (x86)\\Subversion\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\cabal\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\local\\bin;D:\\software\\programming\\LLVM\\clang6\\bin;C:\\Users\\Administrator\\AppData\\Local\\GitHubDesktop\\bin;C:\\Program Files\\gtk-3.8.1;D:\\software\\media\\book\\tex\\miktex-portable-2.9.4250\\miktex\\bin;C:\\Python36;C:\\Python36\\Scripts;D:\\software\\database\\RDBMS\\MySQL\\mysql-5.6.20-winx64\\bin;D:\\software\\programming\\Qt\\Qt_1_2_1\\\\Desktop\\Qt\\4.8.1\\msvc2010\\bin\\;D:\\software\\Internet\\download_tool\\git\\PortableGit-2.11.1-64-bit\\\\cmd;C:\\Program Files\\Haskell Platform\\8.0.2\\\\mingw\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\cabal\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\local\\bin;D:\\software\\programming\\gcc\\tool\\UnxUtils\\usr\\local\\wbin\\pkg-config;E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat\\set_path\\\\cmdline_tool_link;E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat;D:\\software\\programming\\develop tools\\cmake\\cmake-3.7.2-win64-x64\\bin;D:\\software\\cmdline_tool_link;E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\nn_ns\\app\\scripts;C:\\Python36\\lib\\site-packages\\pywin32_system32;C:\\Python36\\lib\\site-packages\\pywin32_system32'
    , 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC'
    , 'PROCESSOR_ARCHITECTURE': 'AMD64'
    , 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel'
    , 'PROCESSOR_LEVEL': '6'
    , 'PROCESSOR_REVISION': '2a07'
    , 'PROGRAMDATA': 'C:\\ProgramData'
    , 'PROGRAMFILES': 'C:\\Program Files'
    , 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)'
    , 'PROGRAMW6432': 'C:\\Program Files'
    , 'PROMPT': '$P$G'
    , 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\'
    , 'PUBLIC': 'C:\\Users\\Public'
    , 'PYHOME': 'C:\\Python36'
    , 'PY_BIN': 'C:\\Python36'
    , 'PY_INCLUDE': 'C:\\Python36\\include'
    , 'PY_LIB': 'C:\\Python36\\libs'
    , 'PY_PYTHON': '3'
    , 'QT_HOME': 'D:\\software\\programming\\Qt\\Qt_1_2_1\\'
    , 'QT_MINGW_BIN': 'D:\\software\\programming\\Qt\\Qt_1_2_1\\\\Desktop\\Qt\\4.7.4\\mingw\\bin\\'
    , 'QT_MSVC_BIN': 'D:\\software\\programming\\Qt\\Qt_1_2_1\\\\Desktop\\Qt\\4.8.1\\msvc2010\\bin\\'
    , 'SESSIONNAME': 'Console'
    , 'SET_BAT_PATH': 'E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat\\set_path\\'
    , 'SHIM_MCCOMPAT': '0x810000001'
    , 'STACK_ROOT': 'C:\\sr'
    , 'SVN_REPOS': 'D:/software/media/control/svn_repository'
    , 'SVN_REPOS_BASENAME': 'svn_repository'
    , 'SVN_REPOS_URL': 'file:///D:/software/media/control/svn_repository', 'SVN_WORKING_COPY': 'E:\\my_data\\program_source\\svn_working_copy_parent/svn_repository'
    , 'SVN_WORKING_COPY_PARENT': 'E:\\my_data\\program_source\\svn_working_copy_parent'
    , 'SWIG_HOME': 'D:\\software\\programming\\swig\\swigwin-3.0.2'
    , 'SYSTEMDRIVE': 'C:'
    , 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'D:\\TEMP_O~1\\SYSTEM~1'
    , 'TEXHOME': 'D:\\software\\media\\book\\tex\\miktex-portable-2.9.4250\\miktex\\bin'
    , 'TMP': 'D:\\TEMP_O~1\\SYSTEM~1'
    , 'USERDOMAIN': 'ZGC-20120617LVJ'
    , 'USERNAME': 'Administrator'
    , 'USERPROFILE': 'C:\\Users\\Administrator'
    , 'USRBIN_PATH': 'D:\\software\\programming\\gcc\\tool\\UnxUtils\\usr\\local\\wbin'
    , 'VS100COMNTOOLS': 'c:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\Common7\\Tools\\'
    , 'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\'
    , 'WINDIR': 'C:\\Windows'
    , '_DFX_INSTALL_UNSIGNED_DRIVER': '1'
    , 'DJANGO_SETTINGS_MODULE': 'mzitu_com_project.settings'
    , 'RUN_MAIN': 'true'
    , 'SERVER_NAME': 'atm.youku.com'
    , 'GATEWAY_INTERFACE': 'CGI/1.1'
    , 'SERVER_PORT': '8000'
    , 'REMOTE_HOST': ''
    , 'CONTENT_LENGTH': ''
    , 'SCRIPT_NAME': ''
    , 'SERVER_PROTOCOL': 'HTTP/1.1'
    , 'SERVER_SOFTWARE': 'WSGIServer/0.2'
    , 'REQUEST_METHOD': 'GET'
    , 'PATH_INFO': '/per/165161/'
    , 'QUERY_STRING': ''
    , 'REMOTE_ADDR': '127.0.0.1'
    , 'CONTENT_TYPE': 'text/plain'
    , 'HTTP_HOST': '127.0.0.1:8000'
    , 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    , 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    , 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.5'
    , 'HTTP_ACCEPT_ENCODING': 'gzip, deflate'
    , 'HTTP_REFERER': 'http://127.0.0.1:8000/new/'
    , 'HTTP_CONNECTION': 'keep-alive'
    , 'HTTP_COOKIE': 'csrftoken=ftXZQWEGtWNiHS739KtU5l7baX5FpxozWRYdoy4I2v7tKniWtyJhaMnqaM35FRJG'
    , 'HTTP_UPGRADE_INSECURE_REQUESTS': '1'
    , 'HTTP_CACHE_CONTROL': 'max-age=0'
    , 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x000000000532E9B0>
    , 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
    , 'wsgi.version': (1, 0)
    , 'wsgi.run_once': False
    , 'wsgi.url_scheme': 'http'
    , 'wsgi.multithread': True
    , 'wsgi.multiprocess': False
    , 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>
    , 'CSRF_COOKIE': 'ftXZQWEGtWNiHS739KtU5l7baX5FpxozWRYdoy4I2v7tKniWtyJhaMnqaM35FRJG'
    }
request.POST = <QueryDict: {}>
request._current_scheme_host = 'http://127.0.0.1:8000'
request._encoding = None
request._get_full_path = <bound method HttpRequest._get_full_path of <WSGIRequest: GET '/per/165161/'>>
request._get_post = <QueryDict: {}>
request._get_raw_host = '127.0.0.1:8000'
request._get_scheme = 'http'
request._initialize_handlers = None
request._load_post_and_files = None
request._mark_post_parse_error = None
request._messages = <django.contrib.messages.storage.fallback.FallbackStorage object at 0x00000000053B50F0>
request._post_parse_error = True
request._read_started = False
request._set_post = <bound method WSGIRequest._set_post of <WSGIRequest: GET '/per/165161/'>>
request._stream = <django.core.handlers.wsgi.LimitedStream object at 0x000000000532EDD8>
request._upload_handlers = [
    <django.core.files.uploadhandler.MemoryFileUploadHandler object at 0x00000000053C15F8>
    , <django.core.files.uploadhandler.TemporaryFileUploadHandler object at 0x00000000053C15C0>
    ]
request.body = b''
request.build_absolute_uri = 'http://127.0.0.1:8000/per/165161/'
request.close = None
request.content_params = {}
request.content_type = 'text/plain'
request.csrf_processing_done = True
request.encoding = None
request.environ = {
    '7Z': 'py -m nn_ns.fileformat.zip_by_7z'
    , 'ALLUSERSPROFILE': 'C:\\ProgramData'
    , 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming'
    , 'APR_ICONV_PATH': 'C:\\Program Files (x86)\\Subversion\\iconv'
    , 'BATS_PATH': 'E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat'
    , 'BJJ': 'b2 toolset=msvc --build-dir=D:\\temp_output\\build_dir --stagedir=D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36 address-model=64  architecture=x86 target-os=windows --build-type=complete --layout=versioned threading=multivariant=release runtime-link=shared '
    , 'BOOST': 'D:\\software\\programming\\library\\boost\\boost_1_55_0'
    , 'BOOST_BUILD_OPTIONS': '--build-dir=D:\\temp_output\\build_dir --stagedir=D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36 address-model=64  architecture=x86 target-os=windows --build-type=complete --layout=versioned threading=multi variant=release runtime-link=shared'
    , 'BOOST_BUILD_STAGEDIR': 'D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36'
    , 'BOOST_LIB': 'D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36\\lib'
    , 'CLANGHOME': 'D:\\software\\programming\\LLVM\\clang6\\bin'
    , 'CLANG_LIBCXX_INCLUDE': 'D:\\software\\programming\\LLVM\\clang-6.0.0\\libcxx-6.0.0.src'
    , 'CLASSPATH': 'E:\\my_data\\program_source\\java_src'
    , 'CL_PY': '/Fo /LD /MD /EHsc /IC:\\Python36\\include /ID:\\software\\programming\\library\\boost\\boost_1_55_0 /link /LIBPATH:D:\\software\\programming\\library\\boost\\boost_1_55_0\\binary_lib\\x86_64_py36\\lib /LIBPATH:C:\\Python36\\libs'
    , 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files'
    , 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files'
    , 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files'
    , 'COMPUTERNAME': 'ZGC-20120617LVJ'
    , 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe'
    , 'FFMPEG_BIN': 'D:\\software\\media\\converter\\ffmpeg\\ffmpeg-4.0.2\\bin'
    , 'FFMPEG_HOME': 'D:\\software\\media\\converter\\ffmpeg\\ffmpeg-4.0.2'
    , 'FP_NO_HOST_CHECK': 'NO'
    , 'GCCHOME': 'C:\\mingw64\\x86_64-8.1.0-release-posix-seh-rt'
    , 'GITDIR': 'D:\\software\\Internet\\download_tool\\git\\PortableGit-2.11.1-64-bit\\'
    , 'HASKELL_BINS_PREV': 'C:\\Program Files\\Haskell Platform\\8.0.2\\\\lib\\extralibs\\bin;C:\\Program Files\\Haskell Platform\\8.0.2\\\\bin'
    , 'HASKELL_BINS_SUCC': 'C:\\Program Files\\Haskell Platform\\8.0.2\\\\mingw\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\cabal\\bin;C:\\Users\\Administrator\\AppData\\Roaming\\local\\bin'
    , 'HASKELL_HOME': 'C:\\Program Files\\Haskell Platform\\8.0.2\\'
    , 'HASKELL_ROAMING': 'C:\\Users\\Administrator\\AppData\\Roaming'
    , 'HOMEDRIVE': 'C:'
    , 'HOMEPATH': '\\Users\\Administrator'
    , 'JDKHOME': 'D:\\software\\programming\\Java\\jdk8u25'
    , 'LANG': 'zh_CN'
    , 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local'
    , 'LOGONSERVER': '\\\\ZGC-20120617LVJ'
    , 'MATHEMATICA_HOME': 'C:\\Program Files\\Wolfram Research\\Mathematica\\9.0'
    , 'MYSQLHOME': 'D:\\software\\database\\RDBMS\\MySQL\\mysql-5.6.20-winx64'
    , 'NUMBER_OF_PROCESSORS': '2'
    , 'OCAMLLIB': 'D:\\software\\programming\\ML\\OCaml\\lib'
    , 'OS': 'Windows_NT'
    , 'PATH': ...
    , 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC'
    , 'PROCESSOR_ARCHITECTURE': 'AMD64'
    , 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel'
    , 'PROCESSOR_LEVEL': '6'
    , 'PROCESSOR_REVISION': '2a07'
    , 'PROGRAMDATA': 'C:\\ProgramData'
    , 'PROGRAMFILES': 'C:\\Program Files'
    , 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)'
    , 'PROGRAMW6432': 'C:\\Program Files'
    , 'PROMPT': '$P$G'
    , 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\'
    , 'PUBLIC': 'C:\\Users\\Public'
    , 'PYHOME': 'C:\\Python36'
    , 'PY_BIN': 'C:\\Python36'
    , 'PY_INCLUDE': 'C:\\Python36\\include'
    , 'PY_LIB': 'C:\\Python36\\libs'
    , 'PY_PYTHON': '3'
    , 'QT_HOME': 'D:\\software\\programming\\Qt\\Qt_1_2_1\\'
    , 'QT_MINGW_BIN': 'D:\\software\\programming\\Qt\\Qt_1_2_1\\\\Desktop\\Qt\\4.7.4\\mingw\\bin\\'
    , 'QT_MSVC_BIN': 'D:\\software\\programming\\Qt\\Qt_1_2_1\\\\Desktop\\Qt\\4.8.1\\msvc2010\\bin\\'
    , 'SESSIONNAME': 'Console'
    , 'SET_BAT_PATH': 'E:\\my_data\\program_source\\github\\edt-yxz-zzd\\python3_src\\windows_bat\\set_path\\'
    , 'SHIM_MCCOMPAT': '0x810000001'
    , 'STACK_ROOT': 'C:\\sr'
    , 'SVN_REPOS': 'D:/software/media/control/svn_repository'
    , 'SVN_REPOS_BASENAME': 'svn_repository'
    , 'SVN_REPOS_URL': 'file:///D:/software/media/control/svn_repository'
    , 'SVN_WORKING_COPY': 'E:\\my_data\\program_source\\svn_working_copy_parent/svn_repository'
    , 'SVN_WORKING_COPY_PARENT': 'E:\\my_data\\program_source\\svn_working_copy_parent'
    , 'SWIG_HOME': 'D:\\software\\programming\\swig\\swigwin-3.0.2'
    , 'SYSTEMDRIVE': 'C:'
    , 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'D:\\TEMP_O~1\\SYSTEM~1'
    , 'TEXHOME': 'D:\\software\\media\\book\\tex\\miktex-portable-2.9.4250\\miktex\\bin'
    , 'TMP': 'D:\\TEMP_O~1\\SYSTEM~1'
    , 'USERDOMAIN': 'ZGC-20120617LVJ'
    , 'USERNAME': 'Administrator'
    , 'USERPROFILE': 'C:\\Users\\Administrator'
    , 'USRBIN_PATH': 'D:\\software\\programming\\gcc\\tool\\UnxUtils\\usr\\local\\wbin'
    , 'VS100COMNTOOLS': 'c:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\Common7\\Tools\\'
    , 'VS140COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\Common7\\Tools\\'
    , 'WINDIR': 'C:\\Windows'
    , '_DFX_INSTALL_UNSIGNED_DRIVER': '1'
    , 'DJANGO_SETTINGS_MODULE': 'mzitu_com_project.settings'
    , 'RUN_MAIN': 'true'
    , 'SERVER_NAME': 'atm.youku.com'
    , 'GATEWAY_INTERFACE': 'CGI/1.1'
    , 'SERVER_PORT': '8000'
    , 'REMOTE_HOST': ''
    , 'CONTENT_LENGTH': ''
    , 'SCRIPT_NAME': ''
    , 'SERVER_PROTOCOL': 'HTTP/1.1'
    , 'SERVER_SOFTWARE': 'WSGIServer/0.2'
    , 'REQUEST_METHOD': 'GET'
    , 'PATH_INFO': '/per/165161/'
    , 'QUERY_STRING': ''
    , 'REMOTE_ADDR': '127.0.0.1'
    , 'CONTENT_TYPE': 'text/plain'
    , 'HTTP_HOST': '127.0.0.1:8000'
    , 'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    , 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.5'
    , 'HTTP_ACCEPT_ENCODING': 'gzip, deflate'
    , 'HTTP_REFERER': 'http://127.0.0.1:8000/new/'
    , 'HTTP_CONNECTION': 'keep-alive'
    , 'HTTP_COOKIE': 'csrftoken=ftXZQWEGtWNiHS739KtU5l7baX5FpxozWRYdoy4I2v7tKniWtyJhaMnqaM35FRJG'
    , 'HTTP_UPGRADE_INSECURE_REQUESTS': '1'
    , 'HTTP_CACHE_CONTROL': 'max-age=0'
    , 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x000000000532E9B0>
    , 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
    , 'wsgi.version': (1, 0)
    , 'wsgi.run_once': False
    , 'wsgi.url_scheme': 'http'
    , 'wsgi.multithread': True
    , 'wsgi.multiprocess': False
    , 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>
    , 'CSRF_COOKIE': 'ftXZQWEGtWNiHS739KtU5l7baX5FpxozWRYdoy4I2v7tKniWtyJhaMnqaM35FRJG'
    }
request.get_full_path = '/per/165161/'
request.get_full_path_info = '/per/165161/'
request.get_host = '127.0.0.1:8000'
request.get_port = '8000'
request.get_raw_uri = 'http://127.0.0.1:8000/per/165161/'
request.get_signed_cookie = <bound method HttpRequest.get_signed_cookie of <WSGIRequest: GET '/per/165161/'>>
request.is_ajax = False
request.is_secure = False
request.method = 'GET'
request.parse_file_upload = <bound method HttpRequest.parse_file_upload of <WSGIRequest: GET '/per/165161/'>>
request.path = '/per/165161/'
request.path_info = '/per/165161/'
request.read = b''
request.readline = b''
request.readlines = []
request.resolver_match = ResolverMatch(func=per_app.views.per_mzitu__page_view, args=(), kwargs=
{}, url_name=None, app_names=[], namespaces=[])
request.scheme = 'http'
request.session = <django.contrib.sessions.backends.db.SessionStore object at 0x000000000532EE10>
request.upload_handlers = [
    <django.core.files.uploadhandler.MemoryFileUploadHandler object at 0x00000000053C15F8>
    , <django.core.files.uploadhandler.TemporaryFileUploadHandler object at 0x00000000053C15C0>
    ]
request.user = <SimpleLazyObject: <function AuthenticationMiddleware.process_request.<locals>.<lambda> at 0x00000000053A3EA0>>
request.xreadlines = <generator object HttpRequest.xreadlines at 0x0000000005394620>

'''

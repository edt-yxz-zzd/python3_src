see:
    "NOTE/Java/MyJavaBuildSystem/design.txt"

command:
    # should create xxx.depends first
    #   copy "tpl.depends"

    # compile_module_and_dependencies ==>> jc_all.bat
    py -m nn_ns.app.JavaBuildsystem.compile_module_and_dependencies nn_ns.txt.IncrementalTextEditor -cp E:\my_data\program_source\github\edt-yxz-zzd\python3_src\nn_ns\app\IncrementalTextEditor -v

    # make_executable_jarfile ==>> mk_jar.bat
    py -m nn_ns.app.JavaBuildsystem.make_executable_jarfile pkgResourceAccessor.ResourceAccessor -cp E:\my_data\my_record_txt\NOTE\Java\howto\example -v


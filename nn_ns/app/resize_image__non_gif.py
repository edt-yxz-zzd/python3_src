
from nn_ns.multimedia.image.resize_image__non_gif import resize_image__non_gif
from nn_ns.filedir.touch_file_time_pair__ns import (
    get_file_time_pair__ns
    ,touch_file_time_pair__ns
    )


import glob
from pathlib import Path

def old_size2new_size_bound(old_size):
    width, height = old_size
    new_size_bound = max_width, max_height = 1366, 768
    return new_size_bound

def main_impl(input_glob_pattern, maybe_output_dir):
    input_glob_pattern
    maybe_output_dir # None - inplace

    if maybe_output_dir is None:
        def ipath2opath(ipath):
            opath = ipath
            return opath
    else:
        output_dir = maybe_output_dir
        output_dir_path = Path(output_dir)
        if not output_dir_path.is_dir():
            raise NotADirectoryError(output_dir)

        def ipath2opath(ipath):
            name = ipath.name
            opath = Path(output_dir_path, name)
            return opath

    for ifname in glob.iglob(input_glob_pattern, recursive=True):
        ipath = Path(ifname)
        #bug: if ipath.is_dir: continue
        if ipath.is_dir(): continue

        opath = ipath2opath(ipath)
        print(ipath, ':=>:', opath)

        atime, mtime = get_file_time_pair__ns(ipath)

        resize_image__non_gif(
            ipath
            ,opath
            ,old_size2new_size_bound
            ,is_new_size_bound=True
            ,method_kwargs=None
            )

        touch_file_time_pair__ns(opath
            , access_time_ns=atime, modified_time_ns=mtime)





def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(
        description='resize non-gif image'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input_glob_pattern', type=str
                        , required=True
                        , help='glob pattern of inp_ut image file paths')
    parser.add_argument('-o', '--output_dir', type=str
                        , required=True
                        , default='<inplace>'
                        , help='output directory path; <inplace> - resized image overwrite orginal file')


    args = parser.parse_args(args)
    input_glob_pattern = args.input_glob_pattern
    output_dir = args.output_dir
    if output_dir == '<inplace>':
        maybe_output_dir = None
    else:
        maybe_output_dir = output_dir

    print(f'input_glob_pattern={input_glob_pattern!r}; maybe_output_dir={maybe_output_dir!r}')
    main_impl(input_glob_pattern, maybe_output_dir)



if __name__ == "__main__":
    main()



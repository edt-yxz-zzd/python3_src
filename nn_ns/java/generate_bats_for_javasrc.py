
import argparse
from sand import askstring
pkgclass_name = 'com.pulpfreepress.jfa.chapter1.ApplicationClass'




set_main_tpl = '''
set java_class_name={class_name}
set java_pkg_midpath={pkg_midpath}
set java_pkgclass_name={pkg_name}.%java_class_name%
set java_pkg1={pkg1}

set path2javasrc=.\src
set path2javaclass=.\classes
set path2javadoc=.\doc

set javasrc_fname=%path2javasrc%\%java_pkg_midpath%\%java_class_name%.java
set javasrc_fname_all=%path2javasrc%\%java_pkg_midpath%\*.java

set javaclass_fname=%path2javaclass%\%java_pkg_midpath%\%java_class_name%

'''


def split_fullname(fullname):
    ls = fullname.split('.')
    class_name = ls[-1]
    pkg_name = '.'.join(ls[:-1])
    pkg_midpath = '\\'.join(ls[:-1])

    pkg1 = ls[0]

    return class_name, pkg_midpath, pkg_name, pkg1
    
def gen_set_main(pkgclass_name):
    class_name, pkg_midpath, pkg_name, pkg1 = \
                split_fullname(pkgclass_name)[:4]
    
    set_main = set_main_tpl.format(class_name=class_name, \
                                   pkg_midpath=pkg_midpath, \
                                   pkg_name=pkg_name,
                                   pkg1=pkg1)
    return set_main


def gen_other_bats():
    c_bat_part = r'javac  -cp %path2javaclass% -d %path2javaclass% '
    bats = {
        's':     r'py -m removeFirstChars s.java %javasrc_fname% %*',
        'c':     c_bat_part + r'%javasrc_fname%',
        'c_all': c_bat_part + r'%javasrc_fname_all%',
        'r':     r'java -cp %path2javaclass% %java_pkgclass_name% %*',
        'd':     r'javadoc %javasrc_fname% -d %path2javadoc%'\
                 r'\%java_pkg_midpath%\%java_class_name%',
        'j':     r'jar -cmf mainclass %path2javaclass%\%java_pkg1%.jar '\
                 r'-C %path2javaclass% %java_pkg1%',
        'rj':    r'java  -cp %path2javaclass% -jar %path2javaclass%\%java_pkg1%.jar %*',
        
        'm':  'java_set_main',
        'ca': 'c_all',
        'cr': 'call c\nr %*\n',

        #'java_set_main': gen_set_main(pkgclass_name),
    }

    return bats


def to_txt_file(txt, fname):
    with open(fname, 'w') as fout:
        fout.write(txt)

def to_bat_file(txt, fname_base):
    to_txt_file(txt, fname_base+'.bat')



def output_other_bats():
    bats = gen_other_bats()
    for fn, txt in bats.items():
        to_bat_file(txt, fn)

def output_java_set_main(pkgclass_name):
    to_bat_file(gen_set_main(pkgclass_name), 'java_set_main')



def main(args = None):
    noInput = '<None>'
    parser = argparse.ArgumentParser(\
        description='generate some useful bats for java source')
    parser.add_argument('class_fullname', type=str, nargs='?', default=noInput,
                        help='full name of a class, like "com.ns.TestClass"')
    parser.add_argument('-o', action='store_true',
                        help='generate other bat files')


    
    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)
        
    
    #print(args.s)
    if args.o:
        output_other_bats()
    else:
        if args.class_fullname == noInput:
            args.class_fullname = askstring(\
                'input', 'input fullname of a class')

        output_java_set_main(args.class_fullname)


if __name__ == "__main__":
    #print(sys.argv)
    main()



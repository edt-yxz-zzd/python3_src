nauty
  http://users.cecs.anu.edu.au/~bdm/nauty/
   tar xvzf nauty27r1.tar.gz
   cd nauty27r1
   ./configure
   make
   ===
   http://users.cecs.anu.edu.au/~bdm/nauty/pgi.pdf
    Practical Graph Isomorphism (1981)(McKay).pdf
   https://arxiv.org/abs/0804.4881
     Search Space Contraction in Canonical Labeling of Graphs (v2.2011)(Piperno).pdf
    https://arxiv.org/abs/1301.1493
      Practical Graph Isomorphism II (2013)(McKay)(Piperno).pdf





[[[
工具 使用
[
geng : generate small graphs
gentreeg : generate trees
genrang : generate random graphs
genquartic : generate quartic graphs
genspecialg : generate special graphs, like cycles and complete graphs

copyg : convert format and select subset
amtog : read graphs in adjacency matrix form

labelg : canonically label graphs
ranlabg : randomly relabel graphs

listg : display graphs in a variety of forms
showg : a stand-alone subset of listg

planarg : test graphs for planarity and i nd embeddings or obstructions.
]





cd ~/src/nauty27r1
cd /data/data/com.termux/files/home/src/nauty27r1

./listg --help
  Usage: listg [-fp#:#l#o#Ftq] [-a|-A|-c|-d|-e|-H|-M|-W|-L|-s|-b|-G|-y|-Yxxx] [infile [outfile]]
  Write graphs in human-readable format.
    -c  : write ascii form with minimal line-breaks
    -y  : write in dot file format
    -Yxxx : extra dotty commands for dot files (arg continues to end of param)


./showg --help
  无趣，且可被 ./listg 替代

没有 ./plantri，这是另一个项目


./geng -Cd3D3 4 > ~/tmp/graph/geng_Cd3D3_4.g6s
$ ./listg -c ~/tmp/graph/geng_Cd3D3_4.g6s
;n4g1 2 3;2 3;3.
$ ./listg -y ~/tmp/graph/geng_Cd3D3_4.g6s
graph G1 {
0--1;
0--2;
0--3;
1--2;
1--3;
2--3;
}



./copyg --help
  Usage: copyg [-gszfp#:#qhx] [infile [outfile]]
  Copy a file of graphs with possible format conversion.
    -g  Use graph6 format for output
    -s  Use sparse6 format for output
    -z  Use digraph6 format for output


./copyg -g /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/'-adc3m3[4, 6, 8].txt'
  >A ./copyg -g /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3/-adc3m3[4, 6, 8].txt
  >E readg_inc: illegal character
  >E gtools: No such file or directory
  #不能接受 plantri 的输出，待我看看plantri是否有graph6输出选项


cd ~/src/plantri50
./plantri --help
  Plantri version 5.0 - Oct 1, 2015
  Usage: ./plantri [-uagsEh -Ac#txm#P#bpe#f#q -odGV -v] n [res/mod] [outfile]
  See plantri-guide.txt for more information.

view ../../python3_src/c_external/plantri/plantri-doc/plantri-guide.txt
  output format:
    -g graph6
    -s sparse6
    -a ascii

./plantri -adc3m3 4d
  4 bcd,adc,abd,acb

./plantri -gdc3m3 4d
  C~


#cmd.exe: for /L %i in (4,2,16) do echo %i
#bash:
for i in {4..16..2} ; do echo $i ; done
for i in {4..16..2} ; do echo $i ; done > ~/tmp/-sdc3m3[4d-16d].s6s
view ~/tmp/-sdc3m3[4d-16d].s6s

for i in {4..16..2} ; do ./plantri -sdc3m3 ${i}d ; done > ~/tmp/-sdc3m3[4d-16d].s6s
view ~/tmp/-sdc3m3[4d-16d].s6s
for i in {4..16..2} ; do ./plantri -adc3m3 ${i}d ; done > ~/tmp/-adc3m3[4d-16d].txt
view ~/tmp/-adc3m3[4d-16d].txt
diff ~/tmp/-adc3m3[4d-16d].txt /sdcard/0my_files/git_repos/python3_src/nn_ns/graph/adc3m3_from4to18d.txt


cd ~/src/nauty27r1
]]]







[[[
==== 安装 毛病
   tar xvzf nauty27r1.tar.gz
   cd nauty27r1
   ./configure
   make

毛病一
$ ./configure
-bash: ./configure: Permission denied
  原因：共享存储区-不被允许 chmod +x xxx.sh
  改为：
    bash ./configure
  或：
     tar xvzf nauty27r1.tar.gz -C ~/src/
     cd ~/src/nauty27r1
     ./configure
     make

毛病二
$ bash ./configure
configure: error: cannot run /bin/sh ./config.sub
$ ./configure
-bash: ./configure: /bin/sh: bad interpreter: No such file or directory
  原因：Android 没有 /bin/ 或 无访问权限 /sbin/
  termux
  $ which bash
  /data/data/com.termux/files/usr/bin/bash


./configure 文件 配置 出错，需重新 生成：
  $ autoconf
  === $ autoconf ./configure.ac
  === or: $ autoconf ./configure.in
  $ ./configure
  === $ bash ./configure
  === or $ sh ./configure


毛病三
$ ./configure
checking build system type... config.guess: cannot create a temporary directory in /tmp
configure: error: cannot guess build type; you must specify one


==1
$ ./configure --help
$ ./configure --prefix=$HOME
  错误未改变


==2
$ bash config.guess
config.guess: cannot create a temporary directory in /tmp
$ bash config.guess --help

view others/app/termux/autoconf.txt
  https://stackoverflow.com/questions/4810996/how-to-resolve-configure-guessing-build-type-failure

$ which automake
/data/data/com.termux/files/usr/bin/automake
$ automake --version
automake (GNU automake) 1.16.1
Copyright (C...

ls /data/data/com.termux/files/usr/share/automake-1.16/
cp -t ./    /data/data/com.termux/files/usr/share/automake-1.16/config.guess    /data/data/com.termux/files/usr/share/automake-1.16/config.sub

$ bash config.guess
  错误未改变

==3
$ view config.guess
line102 === ": ${TMPDIR=/tmp} ;"
line102 ==>> ": ${TMPDIR=$HOME/tmp} ;"

$ bash config.guess
cat: -: No such file or directory
armv7l-unknown-linux-gnueabi

$ bash ./configure
  成功！

==4
$ make
gcc -c -O3  -march=native -o naututil.o naututil.c
make: /bin/sh: Command not found
make: *** [makefile:100: naututil.o] Error 127


$ view makefile
line4 === "SHELL=/bin/sh"


make SHELL=bash
  成功！




==================
======复制 善后
ls -t
ls -t === ls --sort=time
  shortg
  genbgL
  edgetransg
  genspecialg
  converseg
  hamheuristic
  twohamg
  cubhamg
  delptg
  vcolg
  subdivideg
  dretodot
  watercluster2
  linegraphg
  gentourng
  planarg
  multig
  ranlabg
  gengL
  assembleg
  underlyingg
  genquarticg
  gentreeg
  directg
  genbg
  catg
  newedgeg
  genrang
  pickg
  countg
  deledgeg
  addedgeg
  biplabg
  NRswitchg
  showg
  complg
  geng
  amtog
  dretog
  labelg
  listg
  copyg
  nautyL1.a
          gtnautyL1.o
          gutil2L1.o
          gutil1L1.o
          nautinvL1.o
          naututilL1.o
          naugraphL1.o
          nautilL1.o
          nautyL1.o
  nautyL.a
          nautycliquerL.o
          naugroupL.o
          gtnautyL.o
          gutil2L.o
          gutil1L.o
          nautinvL.o
          naututilL.o
          gtoolsL.o
          schreierL.o
          naugraphL.o
          nausparseL.o
          nautilL.o
          nautyL.o
  nautyW1.a
          gtnautyW1.o
          gutil2W1.o
          gutil1W1.o
          nautinvW1.o
          naututilW1.o
          naugraphW1.o
          nautilW1.o
          nautyW1.o
  nautyW.a
          nautycliquerW.o
          naugroupW.o
          gtnautyW.o
          gutil2W.o
          gutil1W.o
          nautinvW.o
          naututilW.o
          gtoolsW.o
          schreierW.o
          naugraphW.o
          nausparseW.o
          nautilW.o
          nautyW.o
  nauty1.a
          nautinv1.o
          naututil1.o
          naugraph1.o
          nautil1.o
          nauty1.o
  nauty.a
          nautycliquer.o
          naugroup.o
          gtnauty.o
          gutil2.o
          gutil1.o
  dreadnaut
          naurng.o
          schreier.o
          naugraph.o
          nausparse.o
          nautil.o
          nauty.o
          gtools.o
          traces.o
          nautinv.o
          naututil.o
  config.log
  gtools.h
  naututil.h
  nauty.h
  makefile
  config.status
  config.guess
  config.sub
  autom4te.cache #directory
  configure
  genbg.c #below are src
  ...
  ...

mkdir ./out_gen/
cp -t ./out_gen/ config.log gtools.h naututil.h nauty.h makefile config.status config.guess config.sub configure
cp -r -t ./out_gen/ autom4te.cache/


mkdir ./out_exe/
cp -t ./out_exe/ shortg genbgL edgetransg genspecialg converseg hamheuristic twohamg cubhamg delptg vcolg subdivideg dretodot watercluster2 linegraphg gentourng planarg multig ranlabg gengL assembleg underlyingg genquarticg gentreeg directg genbg catg newedgeg genrang pickg countg deledgeg addedgeg biplabg NRswitchg showg complg geng amtog dretog labelg listg copyg nautyL1.a nautyL.a nautyW1.a nautyW.a nauty1.a nauty.a dreadnaut








mkdir termux@armv7l-unknown-linux-gnueabi
  10 items + 49 items
mv -t ./termux@armv7l-unknown-linux-gnueabi/    ./out_gen/ ./out_exe/

7z a nauty27r1@termux@armv7l-unknown-linux-gnueabi.7z     ./termux@armv7l-unknown-linux-gnueabi/
  Scanning the drive:
  4 folders, 61 files, 11473707 bytes (11 MiB)
  Archive size: 1155543 bytes (1129 KiB)
    1.2MB

cp -r -t /sdcard/0my_files/git_repos/python3_src/c_external/nauty/    ./termux@armv7l-unknown-linux-gnueabi/
cp -t /sdcard/0my_files/git_repos/python3_src/c_external/nauty/    ./nauty27r1@termux@armv7l-unknown-linux-gnueabi.7z



cd /sdcard/0my_files/git_repos/python3_src/c_external/nauty/
tree -d -h --du -L 1 ./
du -h -d 2 ./
$ du -h -d 2 ./
19M     ./nauty27r1
688K    ./termux@armv7l-unknown-linux-gnueabi/out_gen
11M     ./termux@armv7l-unknown-linux-gnueabi/out_exe
12M     ./termux@armv7l-unknown-linux-gnueabi
41M     ./
  除去 解压19MB（nauty27r1/）、生成11MB（out_exe/），还剩下11MB


delete 解压19MB（nauty27r1/）、生成11MB（out_exe/）

nauty说明文件（解压至nauty27-doc/）:
  COPYRIGHT
  README
  README_24
  This_is_nauty27r1
  changes24-27.txt
  formats.txt
  schreier.txt
  nug27.pdf


]]]
















[[[
nauty主页

===== http://users.cecs.anu.edu.au/~bdm/nauty/

nauty and Traces
Brendan McKay and Adolfo Piperno

Please visit the other nauty Traces page at https://pallini.di.uniroma1.it for more than is here.
Summary

nauty and Traces are programs for computing automorphism groups of graphs and digraphs. They can also produce a canonical labelling.

nauty and Traces are written in a portable subset of C, and run on a considerable number of different systems.

There is a small suite of programs called gtools included in the nauty package. For example, geng can generate non-isomorphic graphs very quickly. There are also generators for bipartite graphs, trees, digraphs, multigraphs, and other classes, and many programs for manipulating files of graphs in a compact format.
Documentation

A complete manual is included in the package. It is also separately available here.
See the file changes24-27.txt for a summary of recent changes.

The original design of nauty is in B. D. McKay, Practical Graph Isomorphism, Congressus Numerantium, 30 (1981) 45-87. A scan is available.
The original design of Traces is in A. Piperno, Search Space Contraction in Canonical Labeling of Graphs, available at arxiv.org.
The current algorithms behind nauty and Traces are described in the paper of McKay and Piperno cited below.
How to cite nauty or Traces

If you use nauty or Traces in your research, please cite this paper:
B. D. McKay and A. Piperno, Practical Graph Isomorphism, II, J. Symbolic Computation (2013) 60 94-112. https://doi.org/10.1016/j.jsc.2013.09.003. Preprint version at arxiv.org.
How to get it

If you agree to the restrictions listed below, you may fetch version 2.7 of nauty, and version 2.1 of Traces, as a gzipped tar file (1.6MB).

nauty uses the GNU autoconf installation system. You are advised to read the file README before compiling anything.

Installation procedure for Linux, MacOSX, Cygwin, etc.
   tar xvzf nauty27r1.tar.gz
   cd nauty27r1
   ./configure
   make
After this procedure, the directory nauty27r1 contains all the nauty executables. Move them somewhere else as you wish. Some options are available at the configuration stage; see the manual.

A list of the significant changes since version 2.4 are here: changes24-27.txt.

Note that old or broken systems may not be supported at all; try an older version of nauty. A few things in the gtools package, especially shortg, need a Unix-like environment (such as pipes), though newer versions of Cygwin are fine.
A bug

A bug was discovered in nauty by James Trimble and Chris Jefferson in October 2019. Versions 26r12, 27rc5 27r1 have been fixed. See the changes file for a description.
Nauty mailing list

You are invited to join the nauty mailing list so that you can receive notices of updates and exchange information with other users. Once you join the list, you can post to it by sending mail to nauty@anu.edu.au .
Restrictions

Traces and dretodot are copyright to Adolfo Piperno.
Files planarity.[ch] are copyright to the Magma project.
File watercluster2.c is copyright to Gunnar Brinkmann.
Files nautycliquer.h and nautycliquer.c are copyright to Sampo Niskanen and Patric Östergård. Everything else in the package is copyright to Brendan McKay.

The minimal restrictions on usage are in the file COPYRIGHT in the package and here.

Absolutely no guarantees or warranties are made concerning the suitability, correctness, or any other aspect of this program. Any use is at your own risk.
Old Versions

Prior to version 2.2, nauty and gtools were distributed separately. Traces was not distributed with nauty until version 2.5.

Version 2.6r12 of nauty and Version 2.1 of Traces.
Version 2.5r9 of nauty and Version 2.0 of Traces.
Version 2.4r2 of nauty.
Version 2.2 of nauty.
Version 2.0 (beta 9) of nauty.
Version 1.0 (beta 11) of gtools.
Version 1.9 of nauty.
Authors

Brendan D. McKay
Research School of Computer Science
Australian National University
Canberra, ACT, Australia
brendan dot mckay at anu dot edu dot au

Adolfo Piperno
Dipartimento di Informatica
Sapienza Universitá di Roma
Roma, Italy
piperno at di dot uniroma1 dot it
]]]



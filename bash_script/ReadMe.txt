see: termux/apt_pkg.txt
	set up:
		$my_git_sh
		$my_sh

bash $my_git_sh/gss/export/g_sh
chmod +x $my_sh/*
#######or########
bash $my_git_sh/main_sh/ref_sh
cp -u -i -t $my_sh/ $my_git_sh/my_sh/*
chmod +x $my_sh/*


###############
###############
main_sh/
	use python directly
	other directory can use py
gss/export/
	git helper sh
app/
	nn_ns.app
	../windows_bat/
py/
	py scripts
	since "ref_sh" forward all files of some directories, any files other than sh should not mix with sh
	#####
	git_output2utf8.py
		used in "g_out"
		convert regex"\\[0-7]{3}" to one byte
		git output path as f(path.encode('utf8'))
		where
			f bs = concat $ map g bs
			g b = chr(b) | fr"\\{b!0>3o}"
	gen_forwarding_sh.py
		used in "ref_sh"
		since working sh store under /sdcard/... and "chmod +x" fail on them, we have to make forward call sh under ./my_sh/ and copy to $my_sh/

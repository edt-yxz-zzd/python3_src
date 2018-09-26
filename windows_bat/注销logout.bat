goto start

很多时候用到把关机、注销、重启建立成快捷方式，放在桌面。比如你在管理服务器，使用远程桌面链接时，退出往往使用注销的方式更安全，更少的占用服务器资源。

方法如下：

桌面上或者任何地方右键，“新建”，选择“快捷方式”，在弹出的对话框命令行一栏中输入：C:\Windows\System32\shutdown.exe -l，“下一步”，名称一栏可输入“注销”，完成。

关机命令输入：C:\windows\rundll32.exe user,exitwindows（逗号是必须的）

重启命令输入：C:\WINDOWS\system32\shutdown -r -t 0

11点钟系统自动关机：C:\WINDOWS\system32\at 11:00 shutdown -s

 

还可以使用批处理命令来实现：

打开记事本，输入如下内容，保存为.bat文件即可。

注销：shutdown -l

关机：shutdown -s -f -t 0

重启：shutdown -r -t 0





:start
shutdown -l









import subprocess

exit7z_code2meaning = {
    0:'No error',
    1:'Warning (Non fatal error(s)). For example, one or more files were locked by some other application, so they were not compressed.',
    2:'Fatal error',
    7:'Command line error',
    8:'Not enough memory for operation',
    255:'User stopped the process',
    }


exe7z = r'C:/Program Files/7-Zip/7z.exe'
tpl7z = '{exe} t {fname} -p{password} -r'
t7z = (exit7z_code2meaning, exe7z, tpl7z)


exit_rar_code2meaning = {
    0:'成功操作。',
    1:'警告。发生非致命错误。',
    2:'发生致命错误。',
    3:'无效 CRC32 控制和。数据损坏。',
    4:'尝试修改一个 锁定的压缩文件。',
    5:'写错误。',
    6:'文件打开错误。',
    7:'错误命令行选项。',
    8:'内存不足。',
    9:'文件创建错误。',
    10:'没有找到与指定的掩码匹配的文件。',
    255:'用户中断。'
    }


exe_rar = r'C:/Program Files/WinRAR/rar.exe'
tpl_rar = "{exe} t  -p{password} {fname}"

trar = (exit_rar_code2meaning, exe_rar, tpl_rar)







passwords = [
    '四散的尘埃',
    '黙示',
    '123456',
    'baidu',
    'GAL汉化组',
    'http://www.kcjc.net/',
    '破晓之拓',
    'bbs.acg183.com',
    '比利酱☆@oko.co',
    'hacg.me',
    'http://acgzone.us/',
    'http://acgzone.tk/',
    'http://blogacg.info',
    '天照大御神',
    'abacab',
    'DespairTCK#Music',
    'GMHAndDeepmoon',
    'guishen',
    'www.otomedream.com',
    'www.xinplay.com',
    '多喝开水身体好@开水saltytata',
    '开水saltytata',
    '心游之域',
    '苍雪论坛会员“沙耶の呗”上传',
    '沙耶の唄@苍雪的世界',
    '2djgame',
    'baidu',
    'http://kdays.cn/',
    '54103',
    '5518109@CNGBA',
    'air',
    'ammyyk',
    'ccwwss',
    'Creeper',
    'darknight',
    'e_e｀死灵',
    'Genesis',
    '桂言叶',
    'h5gal',
    '禁止轉載,謝謝合作',
    '禁止轉載，謝謝合作',
    'kcjc',
    'mazochina.com',
    '密码显示错误',
    'ntr',
    'Oneeee',
    '飘过武神54103',
    'pikapi',
    'shana520@苍雪的世界',
    'sstm',
    '快要坏掉的翠星石',
    '日月光影',
    '社会主义优越性的充分体现',
    '捂脸联盟',
    'YES',
    '由依喵@9456123',
    '愿伟大的剑之君主宽恕吾等的罪行',
    '造福全人类',
    '苍雪的世界',
    '四散的尘埃',
    '九十九夜',
    '善恶相抵',
    '流黯',
    '说谎要吞千根钉',
    'hannibal125',
    '彡邪恶丨冷月灬',
    '某个大猫MAO',
    'modaov2',
    '西北の天封',
    '毒网蜘蛛',
    'li422936616',
    '随舍',
    '雪拉呀',
    'Motto栀子',
    'li422936616',
    '雪拉呀',
    '恶透led',
    '最后的卡片',
    '我就是神就是我',
    ]

def try_passwords(fname, passwords, texe=t7z):
    exit_code2meaning, exe, tpl = texe
    for password in passwords:
        exit_code = subprocess.call(tpl.format(exe=exe, fname=fname, password=password))
        print('password:{password}  |  exit_code:{exit_code}  |  {meaning}'
              .format(password=password, exit_code=exit_code, meaning=exit_code2meaning[exit_code]))
        
        if not exit_code:
            break

    else:
        return None
    return password
                                    
def test(fname, more_passwords=None):
    #passwords = ['123456']
    print('fname : ', fname)

    _passwords = passwords
    if more_passwords:
        _passwords = more_passwords + _passwords
    return try_passwords(fname=fname, passwords=_passwords, texe=trar)

path = r'E:/download/comic/孔中窥见真理之貌/'
fname = r'『樱翼汉化组』[本名ワコウ][ノ·ゾ·キ·ア·ナ][第四卷].rar'
#fname = r't.rar'
more_passwords = ['樱翼汉化组', '本名ワコウ', 'ワコウ', 'ノ·ゾ·キ·ア·ナ', '第四卷',
                  '『樱翼汉化组』[本名ワコウ][ノ·ゾ·キ·ア·ナ]', '孔中窥见真理之貌']
print(test(path + fname, more_passwords))




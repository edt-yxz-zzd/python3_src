'''
for zm code of length 1 or 2 # so is xx or xxvv or xxaa
'''


from char2zm import char2zm_ls, joiner
from sand import write_txt, set_path_immutable, set_path_mutable

char_zm_strs_path = 'char_zm_strs.u8'
joiner(globals(), 'char_zm_strs_path')
##print(char_zm_strs_path)
##raise

def zm_ls2zm__pred(zm_ls, pred_zm):
    for zm in zm_ls:
        if pred_zm(zm):
            return zm
    return None

def pred_zm__codeN(zm, N):
    return len(zm) == N
def pred_zm__with_tail(zm, tail):
    return zm.endswith(tail)

def mk_pred_zm(f, *args):
    return lambda zm: f(zm, *args)
def mk_zm_ls2zm(f, *args):
    pred_zm = mk_pred_zm(f, *args)
    return lambda zm_ls: zm_ls2zm__pred(zm_ls, pred_zm)

zm_ls2zm__code1 = mk_zm_ls2zm(pred_zm__codeN, 1)
zm_ls2zm__code2 = mk_zm_ls2zm(pred_zm__codeN, 2)
zm_ls2zm__tailA = mk_zm_ls2zm(pred_zm__with_tail, 'aa')
zm_ls2zm__tailV = mk_zm_ls2zm(pred_zm__with_tail, 'vv')
#zm_ls2zm__tailL = mk_zm_ls2zm(pred_zm__with_tail, 'll')
#zm_ls2zm__tailD = mk_zm_ls2zm(pred_zm__with_tail, 'dd')
zm_ls2zm__all_code3 = lambda ls: '|'.join(ls) if set(map(len, ls)) == {3} else None
zm_ls2zm__max_code3 = lambda ls: '|'.join(filter(lambda zm: len(zm)==3, ls))\
                      if max(map(len, ls)) == 3 else None

zm_ls2zm__list = [zm_ls2zm__code1, zm_ls2zm__code2,
                  zm_ls2zm__tailA, zm_ls2zm__tailV,
                  #zm_ls2zm__tailL, zm_ls2zm__tailD,
                  zm_ls2zm__all_code3, zm_ls2zm__max_code3]





def iter_chars_from(pred_zm_ls):
    for ch, ls in char2zm_ls.items():
        if pred_zm_ls(ls):
            yield ch
def iter2sorted_str(it, sep=''):
    return sep.join(sorted(it))

def chars_from_pred_zm_ls(pred_zm_ls):
    return iter2sorted_str(iter_chars_from(pred_zm_ls))

##def iter_chars_with_tail(tail):
##    return iter_chars_of(mk_zm_ls2zm(pred_zm__with_tail, tail))
##def chars_with_tail(tail):
##    return iter2sorted_str(iter_chars_with_tail(tail))
##
##def iter_chars_of_n_code(n):
##    return iter_chars_of(mk_zm_ls2zm(pred_zm__codeN, n))
##def chars_of_n_code(n):
##    return iter2sorted_str(iter_chars_of_n_code(n))


preds = zm_ls2zm__list
*charss, = map(chars_from_pred_zm_ls, preds)
chars1, chars2, charsA, charsV, charsP3, charsM3 = charss
assert chars1 == '一上世个中为了他发在地多对度成我所是月没现用的要说这'
assert chars2 == '丁七万丈三不与专且业两丰主之乐九也习买予争事二于五些亡人今仍从代令以们件份休会传伪似使信候做儿元先光克全八公共其内册军农冷减几凸凹出刀分切初别到前剩割力办加动助包化区十千半单卜即卷厂原县又反取受变口另只叫可吃各同后吗君吨听启员味和四因国土填增壹夕外大太失奉套女如子学完定实审家宽密寸将小尤就尸层展山川州工左巨己巾带帮常年并广应店废建廿开弃弋张弹当录得心忘快怕性总您感戈或户房手才打找把拆拨拿持按据掉推提搏摸支放敢数整文斗料斤断新方无既日旧早时明春晚景暂曲更有朝期木末札机杂权条来极果柒查标校样格栽棉横欠款止此歧死母每比毛氏民气水永求汉河法泼洋洒洲派流测海消渡港湖源溜滤火炎点炼热照爪片版牙牛狠独猪率玉王瓜甘甚生田电疗病白百皮盛目相省看真眼着矢石破碰示禾税穴立等管米类粮素红纯组细经统续编缺置羊群翻者而耗耳联聘肩肯肿胀胜能脉脱腻膜臣自至舌舟般节花若落虎虫行衣补表被装西见观角言警让讲设诉该调败贩贱费赔走越足路跳跺身躲车轨软辛辰近逃速道那都里重金钢钱钻铁铬镇长門门闭问间闻防阳阴随难雨需青非面革页项顺须顾领颇风食马验骗骨鬼鱼鳥鸟鹿黑齐齿龙'
#charsA, charsV = map(chars_with_tail, ['aa', 'vv'])
assert charsA == '〇丅丆丗丨丩丱丶丷丿乀乁乄乑乚乛亅亠亻亼冂冫凵勹匚匸卄卌卩咼囗士夂孑宀尢屮巜廴廾彑彡彳忄戊戋扌攵曰朩毌氣氵灬烏爫牜疒短礻糸糹纟罒耂艮艹虍蟲衤襾覀訁讠貝辶釆釒鉭钅镸阝隹飠饣髟魚\ue815\ue816\ue817\ue818\ue819\ue81c\ue81e\ue822\ue823\ue826\ue82b\ue82c\ue830\ue831\ue836\ue839\ue83a\ue83b\ue843\ue848\ue864'
assert charsV == '丂丄中丹主乃乄久乏乜亇于仈仕仴仼休佀佦信六兲冐冒刁匡升卪卫叩只叭叵叾吅吉吐吕吗呆呈唁唫圠圡圭圼坧壬壭孑孒孓巨开弄忹惍才扎扒扗扣抂抇抈拓挋捦旦旧旺昌昍明曱朋末本札朮术朳杏杜束杩東杲杳枂枉林果柘栕汃汇汢汨汩汪沐沰泪洍洲浊淦渔漁玊玌玐玛玥玨琂琻甴电疖疗疟痋相眀码砳碒笃糺系絲肙肚节芏芝苜苢茝茞茧菳虬虽蚂蚎蚏蚞蚟誩辷辽迋迌這里釓釕釟釡釦釷鈅鈢鈤鈻鉐鉬鉵銯鍂钆钌钍钥钼阳阴驲魯鮖鲁'

#charss = [chars1, chars2, charsA, charsV]
lens = list(map(len, charss))
#print(lens)
assert lens == [26, 467, 108, 185, 2888, 2991] # [26, 467, 108, 185, 93, 2]

#cx = charsA[0]
#print(cx, ord(cx), char2zm_ls[cx])

def iter_join_zm(chars, ls2zm):
    for ch in chars:
        yield ch + ls2zm(char2zm_ls[ch])
def join_zm(chars, ls2zm):
    return iter2sorted_str(iter_join_zm(chars, ls2zm), sep=' ')

*char_zm_strs, = map(join_zm, map(chars_from_pred_zm_ls, preds), preds)
#print(char_zm_strs)

def write_char_zm_strs(force = False,
                       char_zm_strs = char_zm_strs,
                       path = char_zm_strs_path):
    fname = path
    open_mode = 'w' if force else 'x'
    if force:
        set_path_mutable(fname)
    with open(fname, open_mode, encoding='u8') as fout:
        for char_zm_str in char_zm_strs:
            print(char_zm_str, file=fout)

    set_path_immutable(fname)

write_char_zm_strs(1)










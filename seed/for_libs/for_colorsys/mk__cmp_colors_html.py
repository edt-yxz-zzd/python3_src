#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/mk__cmp_colors_html.py
    view html_js/html/try_handle_list_mapping.html
    view ../lots/NOTE/html/js/js_Array.txt


seed.for_libs.for_colorsys.mk__cmp_colors_html
py -m nn_ns.app.debug_cmd   seed.for_libs.for_colorsys.mk__cmp_colors_html -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_colorsys.mk__cmp_colors_html:__doc__ -ht



py_adhoc_call   seed.for_libs.for_colorsys.mk__cmp_colors_html   @str.mk__cmp_colors_html  --version:ver1__list  -show_hruler >  ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver1__list.out.html

py_adhoc_call   seed.for_libs.for_colorsys.mk__cmp_colors_html   @str.mk__cmp_colors_html  --version:ver2__group  -show_diff_only >  ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.out.html


py_adhoc_call   seed.for_libs.for_colorsys.mk__cmp_colors_html   @str.mk__cmp_colors_html  --version:ver2__group  +show_diff_only >  ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.diff_only.out.html


py_adhoc_call   seed.for_libs.for_colorsys.mk__cmp_colors_html   @str.mk__cmp_colors_html  --version:ver3__brief4js   >  ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver3__brief4js.out.html


生成结果:
    总规范标识数: 864
    有歧义的规范标识数: 57
    无歧义的规范标识数: 807

view ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver1__list.out.html
du -h ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver1__list.out.html
    396KB
!rm ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver1__list.out.html

view ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.out.html
du -h ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.out.html
    484KB
!rm ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.out.html

view ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.diff_only.out.html
du -h ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver2__group.diff_only.out.html
    56KB


view ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver3__brief4js.out.html
    总数纟规范颜色名:864
    总数纟颜色值:592
    总数纟规范颜色名牜有歧义:559
    总数纟颜色值牜有歧义:287
    总数纟规范颜色名牜无歧义:305
    总数纟颜色值牜无歧义:305
!du -h ../../python3_src/seed/for_libs/for_colorsys/cmp_colors.ver3__brief4js.out.html
    24KB


#]]]'''
__all__ = r'''
mk__cmp_colors_html
'''.split()#'''
__all__








_fmt = r'''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="en-US">
<head>
  <title>Compare Colors </title>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <style type="text/css">
    body {color:#888; background-color:#fff; background: black none;}
    body {font-size: 500%;}
    code {color:green;}
  </style>
</head>
<body>

<h1>Compare Colors</h1>
  <hr>
#view ../../python3_src/seed/for_libs/for_colorsys/mk__cmp_colors_html.py

  <hr>
  <p> 总规范标识数: {} </p>
  <p> 有歧义的规范标识数: {} </p>
  <p> 无歧义的规范标识数: {} </p>
  <p> 生成的颜色对照表: </p>
{}

  <hr>
</body>
</html>
'''#'''


def mk__cmp_colors_html(*, version:'ver1__list,ver2__group,ver3__brief4js', **kwds):
    # g - group
    # c - color/#\d+
    # cnm - color_name
    # gnm - group_name/module_name
    #
    gnm2cnm2c = mk____gnm2cnm2c()
    gnms__using_c13 = mk____gnms__using_c13(gnm2cnm2c)

    std_cnm2gnm2std_c_cnms_pairs = mk____std_cnm2gnm2std_c_cnms_pairs(gnm2cnm2c)

    std_cnm2std_c2gnm2cnms = mk____std_cnm2std_c2gnm2cnms(std_cnm2gnm2std_c_cnms_pairs)


    #basic:ver1,ver2
    std_cnm2std_c2gnm2cnms
    std_cnm2gnm2std_c_cnms_pairs
    gnms__using_c13

    if version == 'ver3__brief4js':
        (j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c) = prepare4brief(std_cnm2std_c2gnm2cnms)
        #ver3:
        #to findout:ambiguous
        j2std_cnm
        j2std_c
        j4std_cnm_Z_js4std_c
        return __ver3(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c)




    out4nums = []
    lazy_it2 = lambda:__ver2(out4nums, gnms__using_c13, std_cnm2std_c2gnm2cnms, **kwds)
    lazy_it1 = lambda:__ver1(out4nums, gnms__using_c13, std_cnm2gnm2std_c_cnms_pairs, **kwds)
    ver2lazy_it = dict(ver1__list=lazy_it1, ver2__group=lazy_it2)
    it = ver2lazy_it[version]()
    code = '\n'.join(it)
    (total, total4diff, total4same) = out4nums
    assert total == total4diff + total4same
    assert total == len(std_cnm2std_c2gnm2cnms)
    assert total == len(std_cnm2gnm2std_c_cnms_pairs)

    a, b, c, d, e = _fmt.split('{}')
    return ''.join(map(str, [a, total, b, total4diff, c, total4same, d, code, e]))
def mk____gnm2cnm2c():
    import seed.for_libs.for_colorsys.color_names as mdl4colors
    gnms = set(mdl4colors.__all__)
    gnm2cnm2c = {gnm:getattr(mdl4colors, gnm) for gnm in gnms}
        # g - group
        # c - color
    return gnm2cnm2c
def mk____gnms__using_c13(gnm2cnm2c, /):
    gnms__using_c13 = set()
    for gnm, cnm2c in gnm2cnm2c.items():
        count = [*map(len, cnm2c.values())].count(13)
        if count == 0:
            continue
        assert count == len(cnm2c), gnm
        gnms__using_c13.add(gnm)
    return gnms__using_c13
def mk____std_cnm2gnm2std_c_cnms_pairs(gnm2cnm2c, /):
    std_cnm2gnm2std_c_cnms_pairs = {}
    for gnm, cnm2c in gnm2cnm2c.items():
        for cnm, c in cnm2c.items():
            std_cnm = cnm2std_cnm_(cnm)
            c = c2std_c_(c)
            gnm2std_c_cnms_pairs = std_cnm2gnm2std_c_cnms_pairs.setdefault(std_cnm, {})
            (std_c, cnms) = gnm2std_c_cnms_pairs.setdefault(gnm, (c, set()))
            assert std_c == c
            cnms.add(cnm)
    return std_cnm2gnm2std_c_cnms_pairs
def mk____std_cnm2std_c2gnm2cnms(std_cnm2gnm2std_c_cnms_pairs, /):
    std_cnm2std_c2gnm2cnms = {}
    for std_cnm, gnm2std_c_cnms_pairs in sorted(std_cnm2gnm2std_c_cnms_pairs.items()):
        assert gnm2std_c_cnms_pairs
        std_c2gnm2cnms = std_cnm2std_c2gnm2cnms.setdefault(std_cnm, {})
        for gnm, (std_c, cnms) in sorted(gnm2std_c_cnms_pairs.items()):
            gnm2cnms = std_c2gnm2cnms.setdefault(std_c, {})
            _cnms = gnm2cnms.setdefault(gnm, cnms)
            assert _cnms is cnms
    return std_cnm2std_c2gnm2cnms
if 1:
    def cnm2std_cnm_(cnm, /):
        return cnm.replace('_', '').replace(' ', '').lower()
    def _4_to_2(_2_2, /):
        assert len(_2_2) == 4
        ab = _2_2[:2]
        cd = _2_2[2:]
        assert ab == cd
        return ab
    def _c13_2_std_c_(c13, /):
        assert len(c13) == 13
        assert c13[0] == '#'
        r = c13[1:5]
        g = c13[5:9]
        b = c13[9:]
        c7 = '#' + ''.join(map(_4_to_2, [r, g, b]))
        _c7_to_c13.setdefault(c7, c13)
        return c7
    def c2std_c_(color, /):
        'illegal:blue:#00000000FFFF:colors_in_tkinter:blue'
        #return color.upper()
        c = color.upper()
        if len(c) == 13:
            c = _c13_2_std_c_(c)
        return c
    _c7_to_c13 = {}
    def upper_c5std_c(gnms__using_c13, gnm, std_c, /):
        if gnm in gnms__using_c13:
            upper_c = c13 = _c7_to_c13[std_c]
        else:
            upper_c = std_c
        return upper_c
    def _extra5std_c_(std_c, /):
        extra = ' background-color: #fff;' if std_c in ('#000', '#000000') else ''
        return extra
    def __ver2(out4nums, gnms__using_c13, std_cnm2std_c2gnm2cnms, /, *, show_diff_only):
        #ver1__list,ver2__group
      total = 0
      total4diff = 0
      total4same = 0
      for total, (std_cnm, std_c2gnm2cnms) in enumerate(sorted(std_cnm2std_c2gnm2cnms.items()), 1):
        are_same = len(std_c2gnm2cnms) == 1
        if not are_same:
            total4diff += 1
        else:
            total4same += 1

        if (show_diff_only and are_same):
            continue
        yield ('<hr>')
        s_d4total4diff = f'-{total4same}' if are_same else f'+{total4diff}'
        if not show_diff_only:
            std_colors__str = ','.join(sorted(std_c2gnm2cnms))
            s_d = 'same' if are_same else 'diff'
            yield (f'<p style="color: red;" > {total}:{s_d4total4diff}:{std_cnm}:{s_d}:{std_colors__str} </p>')
            yield ('<p>+++++++++</p>')
        assert not (show_diff_only and are_same)
        for std_c, gnm2cnms in sorted(std_c2gnm2cnms.items()):
          extra = _extra5std_c_(std_c)
          yield (f'<p>*****{std_c}</p>')
          for gnm, cnms in sorted(gnm2cnms.items()):
            std_cnm, std_c, gnm, cnms
            cnms__str = ','.join(cnms)
            std_cnm, std_c, gnm, cnms__str
            upper_c = upper_c5std_c(gnms__using_c13, gnm, std_c)
            yield (f'<p style="color: {std_c};{extra}" > {total}:{s_d4total4diff}:{std_cnm}:{upper_c}:{gnm}:{cnms__str} </p>')
      yield ('<hr>end')
      out4nums.append(total)
      out4nums.append(total4diff)
      out4nums.append(total4same)

    def __ver1(out4nums, gnms__using_c13, std_cnm2gnm2std_c_cnms_pairs, /, *, show_hruler):
        #ver1__list,ver2__group
      total = 0
      total4diff = 0
      total4same = 0
      for total, (std_cnm, gnm2std_c_cnms_pairs) in enumerate(sorted(std_cnm2gnm2std_c_cnms_pairs.items()), 1):
        assert gnm2std_c_cnms_pairs
        are_same = 1 == len({std_c for gnm, (std_c, cnms) in gnm2std_c_cnms_pairs.items()})
        if not are_same:
            total4diff += 1
        else:
            total4same += 1

        if show_hruler:
            yield ('<hr>')
        for gnm, (std_c, cnms) in sorted(gnm2std_c_cnms_pairs.items()):
            cnms = sorted(cnms)
            extra = _extra5std_c_(std_c)
            cnms__str = ','.join(cnms)
            std_cnm, gnm, std_c, cnms__str
            upper_c = upper_c5std_c(gnms__using_c13, gnm, std_c)
            s_d4total4diff = f'-{total4same}' if are_same else f'+{total4diff}'
            yield (f'<p style="color: {std_c};{extra}" > {total}:{s_d4total4diff}:{std_cnm}:{upper_c}:{gnm}:{cnms__str} </p>')
      if show_hruler:
        yield ('<hr>end')
      out4nums.append(total)
      out4nums.append(total4diff)
      out4nums.append(total4same)






def prepare4brief(std_cnm2std_c2xxx, /):
    j2std_cnm = sorted(std_cnm2std_c2xxx)
    j2std_c = sorted({std_c for std_c2xxx in std_cnm2std_c2xxx.values() for std_c in std_c2xxx})
    j5std_c = {std_c:j for j,std_c in enumerate(j2std_c)}
    j4std_cnm_Z_js4std_c = [sorted(j5std_c[std_c] for std_c in std_cnm2std_c2xxx[std_cnm]) for std_cnm in j2std_cnm]
    return (j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c)
def __ver3(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c, /):
    #ver3__brief4js:
    #bug:注意:cnm含『'』
    if 0:
        j2std_cnm = 'a b c d e'.split(' ')
        j2std_c = '#aa0 #0b0 #c00 #d0d'.split(' ')
        j4std_cnm_Z_js4std_c = [[1, 2], [3], [3], [0], [3]]
    return (
    (_fmt4ver3
    .replace('{here__j2std_cnm}', ' '.join(j2std_cnm))
    .replace('{here__j2std_c}', ' '.join(j2std_c))
    .replace('{here__j4std_cnm_Z_js4std_c}', ';'.join(','.join(map(str, js4std_c)) for js4std_c in j4std_cnm_Z_js4std_c))
    ))

    # #ver3:
    # #to findout:ambiguous
    # j2std_cnm
    # j2std_c
    # j4std_cnm_Z_js4std_c
    # #py==>>:js:
    # j4std_c_Z_js4std_cnm
    # std_cnm2std_c_set
    # std_c2std_cnm_set
    # #==>>:
    # unambiguous__std_cnm2std_c
    # unambiguous__std_c2std_cnm
    #     #bijection

    # ambiguous__std_cnm2std_c_set
    # ambiguous__std_c2std_cnm_set
    #     #not-bijection

    # #index&total
    # total4std_cnm
    # j2std_cnm
    # j5std_cnm

    # total4unambiguous_std_cnm
    # j2unambiguous_std_cnm
    # j5unambiguous_std_cnm

    # total4ambiguous_std_cnm
    # j2ambiguous_std_cnm
    # j5ambiguous_std_cnm

    # total4std_c
    # j2std_c
    # j5std_c

    # total4unambiguous_std_c
    # j2unambiguous_std_c
    # j5unambiguous_std_c

    # total4ambiguous_std_c
    # j2ambiguous_std_c
    # j5ambiguous_std_c
    # #数组:
    # #show:std_cnm@(+j4unambiguous_std_cnm|-j4ambiguous_std_cnm)/j4std_cnm
    # #show:std_c@(+j4unambiguous_std_c|-j4ambiguous_std_c)/j4std_c
    # #
    # #映射:
    # #映射牜一对一:
    # #show:std_cnm@+j4unambiguous_std_cnm/j4std_cnm<->std_c@j4+unambiguous_std_c/j4std_c
    # #映射牜一对多:
    # #show:std_cnm@-j4ambiguous_std_cnm/j4std_cnm->[std_c@-j4ambiguous_std_c/j4std_c(『,』std_c@-j4ambiguous_std_c/j4std_c)*
    # #show:std_c@-j4ambiguous_std_c/j4std_c->[std_cnm@-j4ambiguous_std_cnm/j4std_cnm(『,』std_cnm@-j4ambiguous_std_cnm/j4std_cnm)*



#xxx:copy from:e script/html/try_handle_list_mapping.html
#!mv -n script/html/  html_js/
#copy from:view html_js/html/try_handle_list_mapping.html
_fmt4ver3 = r'''
<!DOCTYPE HTML><html><head>
  <style>
    body {
      color:lightgreen;
      background-color:#444;
      padding:0px;
      margin:0px;
    }
    p {
      border:36px solid blue;
      padding:0px;
      font-size:500%;
      margin:0px;
    }
    hr {
      color:black;
      border:10px solid black;
      padding:0px;
      font-size:100%;
      margin:0px;
    }
  </style>
  <script>
    ;function f(){
      //;let j2std_cnm = 'a b c d e'.split(' ')
      //;let j2std_c = '#aa0 #0b0 #c00 #d0d'.split(' ')
      //;let j4std_cnm_Z_js4std_c = '1,2;3;3;0;3'.split(';').map(s => s.split(',').map(Number))
      //  //;let j4std_cnm_Z_js4std_c = [[1, 2], [3], [3], [0], [3]]
      //  // => j4std_c_Z_js4std_cnm===[[3],[0],[0],[1,2,4]]
      ////;return [j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c]
      ;
      ;let j2std_cnm = "{here__j2std_cnm}".split(' ')
            //bug:注意:cnm含『'』
      ;let j2std_c = '{here__j2std_c}'.split(' ')
      ;let j4std_cnm_Z_js4std_c = '{here__j4std_cnm_Z_js4std_c}'.split(';').map(s => s.split(',').map(Number))
      ;
      ;return g(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c)
    ;}
    ;class Range {
      constructor(begin, end) {
        ;this.begin = begin
        ;this.end = end
      ;}
      *[Symbol.iterator]() {
        ;for (let j = this.begin; j < this.end; j++) {
          yield j;
        }
      ;}
    ;}
    ;function range(n){
      ;return new Range(0, n)
    ;}
  </script>
  <script>
    ;function mk_html(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c){
      ;[vj2wjs, wj2vjs, vj2ok, wj2ok] = find_ambiguous_cs_cnms(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c)
      // vj - j4std_c
      // wj - j4std_cnm
      ;
      ;function mk_html4unambiguous(std_cnm, wj){
        ;let [vj] = wj2vjs[wj]
        ;let std_c = j2std_c[vj]
        ;ss.push(
`<p style="color:${std_c}; border:36px solid ${std_c};">
<b>+${std_cnm}:${std_c}
</b></p>`
        )
        ;return
      ;}
      ;function mk_html4ambiguous(std_cnm, wj){
        ;ss.push('<hr>')
        ;let vjs = wj2vjs[wj]
        ;for (let vj of vjs){
          ;let wjs = vj2wjs[vj]
          ;let std_cnms = wjs.map(wj => j2std_cnm[wj])
          ;let std_c = j2std_c[vj]
          ;let extra = (wjs.length == 1)
            ? ''
            //: `:${std_cnms.length}:${JSON.stringify(std_cnms)}`
            : `:${std_cnms.length}:${std_cnms}`
          ;ss.push(
`<p style="color:${std_c}; border:36px solid ${std_c};">
<b>-${std_cnm}:${std_c}${extra}
</b></p>`
            )
        ;}
        ;ss.push('<hr>')
        ;return
      ;}
      ;function mk_header(){
        ;total4std_cnm = j2std_cnm.length
        ;total4std_c = j2std_c.length
        ;
        ;total4std_cnm4unambiguous = +wj2ok.reduce((sum, is_ok)=>(sum+is_ok), 0)
        ;total4std_c4unambiguous = +vj2ok.reduce((sum, is_ok)=>(sum+is_ok), 0)
        ;
        ;total4std_cnm4ambiguous = total4std_cnm -total4std_cnm4unambiguous
        ;total4std_c4ambiguous = total4std_c -total4std_c4unambiguous
        ;
        ;ss.push(`<p>总数纟规范颜色名:${total4std_cnm}</p>`)
        ;ss.push(`<p>总数纟颜色值:${total4std_c}</p>`)
        ;
        ;ss.push(`<p>总数纟规范颜色名牜有歧义:${total4std_cnm4ambiguous}</p>`)
        ;ss.push(`<p>总数纟颜色值牜有歧义:${total4std_c4ambiguous}</p>`)
        ;
        ;ss.push(`<p>总数纟规范颜色名牜无歧义:${total4std_cnm4unambiguous}</p>`)
        ;ss.push(`<p>总数纟颜色值牜无歧义:${total4std_c4unambiguous}</p>`)
      ;}
      ;let ss = []
      ;mk_header()
      ;j2std_cnm.forEach((std_cnm, wj) => (wj2ok[wj]? mk_html4unambiguous : mk_html4ambiguous)(std_cnm, wj))
      ;return ss.join('\n')
    ;}
    ;function g(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c){
      ;let html = mk_html(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c)
      ;let show_area = document.getElementById('show_area')
      ;show_area.insertAdjacentHTML("beforeend", html)
      ;return html
    ;}
    ;function find_ambiguous_cs_cnms(j2std_cnm, j2std_c, j4std_cnm_Z_js4std_c){
      ;let total4std_cnm = j2std_cnm.length
      ;let total4std_c = j2std_c.length
      ;
      ;let j4std_c_Z_js4std_cnm = j2std_c.map(() => [])
      ;j4std_cnm_Z_js4std_c.forEach(
        (js4std_c, j4std_cnm) => js4std_c.forEach(
          j4std_c => j4std_c_Z_js4std_cnm[j4std_c].push(j4std_cnm)
        )
      )
      // ;return j4std_c_Z_js4std_cnm

      // vj - j4std_c
      // wj - j4std_cnm
      ;let vj2wjs = j4std_c_Z_js4std_cnm
      ;let wj2vjs = j4std_cnm_Z_js4std_c
      ;
      ;let vj2ok = vj2wjs.map((wjs, vj) => (wjs.length === 1 && wj2vjs[wjs[0]].length === 1))
      ;let wj2ok = wj2vjs.map((vjs, wj) => (vjs.length === 1 && vj2wjs[vjs[0]].length === 1))
      ;return [vj2wjs, wj2vjs, vj2ok, wj2ok]
      ;
      ;
      //;let vj_ls0 = Array.from(range(total4std_c))
      ////;let wj_ls0 = Array.from(range(total4std_cnm))
      //;let wj_ls0 = Array.from(j2std_cnm.keys())
      ////;alert(wj_ls0)
      //;
      //;let vj_ls1 = vj_ls0.filter(vj => vj2wjs[vj].length === 1)
      //;let wj_ls1 = wj_ls0.filter(wj => wj2vjs[wj].length === 1)
      //;
      //;let vj_ls2 = vj_ls1.filter(vj => wj2vjs[vj2wjs[vj][0]].length === 1)
      //;let wj_ls2 = wj_ls1.filter(wj => vj2wjs[wj2vjs[wj][0]].length === 1)
      //;
      //;if (vj_ls2.length != wj_ls2.length) {alert('bug');}
      //// ;return [vj_ls2, wj_ls2]
      //;vjs4unambiguous = vj_ls2
      //;wjs4unambiguous = wj_ls2
      //;
      //;vjs4ambiguous = new Set(vj_ls0) -new Set(vjs4unambiguous)
      //;return vjs4ambiguous
    ;}
  //;alert(3)
  //;alert(JSON.stringify(f()))
  ;
  </script>


</head>
<body>
  <div id='show_area'>
  </div>
  <script>
    //;alert(JSON.stringify(f()))
    ;f()
  ;</script>
</body></html>



'''#'''
__all__
from seed.for_libs.for_colorsys.mk__cmp_colors_html import *

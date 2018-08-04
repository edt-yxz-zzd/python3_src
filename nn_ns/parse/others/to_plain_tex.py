import tempfile # for NamedTemporaryFile
import subprocess # for call
import io

import sand
from sand import replace_substrings

special_chars = '\\\n{}$&#^_%~'
replace_ls = [(ch, r'{{\{ch}{{}}}}'.format(ch=ch)) for ch in special_chars]
replace_ls[0] = ('\\', '{\\backslash}')
replace_ls[1] = ('\n', '\n\n')
replace_ls = tuple(replace_ls)



def to_plain_tex_text(ifile):
    ls = []
    for line in ifile:
        line = replace_substrings(line, replace_ls)
        ls.append(line)

    tex = ''.join(ls)
    return tex


tex2dvi_cmd_tpl = r'tex -job-name={out_fname} \input {tex_fname}'
dvi2ps_cmd_tpl = r'dvips -o {out_fname} {dvi_fname}'
ps2pdf_cmd_tpl = r'ps2pdf {ps_fname} {pdf_fname}'

tex_home = r'D:/software/media/book/tex/miktex-portable-2.9.4250/miktex/bin'
def to_pdf(tex_fname, pdf_fname):
    #dvi_file = tempfile.NamedTemporaryFile(prefix='textmp', delete=True)
    with tempfile.NamedTemporaryFile(suffix='.dvi', prefix='textmp', delete=True) as dvi_file:
        dvi_fname = dvi_file.name
        subprocess.call(tex2dvi_cmd_tpl.format(out_fname=dvi_fname, tex_fname=tex_fname))
        with tempfile.NamedTemporaryFile(suffix='.ps', prefix='textmp', delete=True) as ps_file:
            ps_fname = ps_file.name
            subprocess.call(dvi2ps_cmd_tpl.format(out_fname=ps_fname, dvi_fname=dvi_fname))
            subprocess.call(ps2pdf_cmd_tpl.format(ps_fname=ps_fname, pdf_fname=pdf_fname))
        

if sand.is_main(__name__):
    txt_fname = 'task.txt'
    pdf_fname = 'tasktmp.pdf'
    with open(txt_fname) as txt_file:
        tex = to_plain_tex_text(txt_file)

    with tempfile.NamedTemporaryFile(suffix='.tex', prefix='textmp', delete=True) as tex_file:
        tex_fname = tex_file.name
        tex_file.write(tex.encode(encoding='utf_8'))
        to_pdf(tex_fname, pdf_fname)

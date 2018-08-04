
from .replace_substrings import replace_substrings

def raw_text2html_content(txt):
    content = replace_substrings(txt, [
        ('&', '&amp;'),
        ('<', '&lt;'),
        ('>', '&gt;'),
        ('\n', '\n<br/>'),
        ])
    return content



__all__ = ['chars_in_banned_words']

# data collected from 敏感词库 by collect_chars.py

ifname = r'chars_in_banned_words.u8'
iencoding = 'utf8'
def _read():
    with open(ifname, encoding=iencoding) as fin:
        return fin.read()
chars_in_banned_words = _read()



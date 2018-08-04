
import re

c = re.compile
m = re.match

match_all = r'(?s).*' # s : dot match all
match_delimiter = r'(?s)(?P<delimiter><html>).*?(?P=delimiter)' # nongreedy
assert match_delimiter == c(match_delimiter).pattern

match_complement = r'(?a)[^2]+'
p = c(match_complement)
assert m(p, '一')
assert m('(?a).+', '一')
assert not m('[\x00-\xff]+', '一')
assert not m('\d+', '一')




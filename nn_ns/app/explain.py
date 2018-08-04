
import os
import bisect
import os.path
import re


r'''
to avoid failure:
    read from txt:
        errors = 'surrogateescape'
    print to stdout:
        encoding = sys.getfilesystemencoding() 
        s = s.encode(encoding, 'replace')
        s = s.decode(encoding)

to overwrite previous options:
    action = 'append', default = [xx]
    args.xxxx[-1]

    --> xx.exe -k willbeoverwritten -k thelaterwins


'''


dict_path = r'E:\book\数据\英汉词典\牛津英汉双解(第4版)TXT'
history_file = r'E:\temp_output\explain_history.txt'



def get_dict_txt_for_explain(path, word,
                encoding='gb18030',
                errors = 'surrogateescape'
                ):
    fn = get_fname(path, word)
    with open(fn, encoding = encoding, errors = errors) as fin:
        txt = fin.read()

    return txt


def get_word_pattern_str(word):
    word_pattern_tpl = r'(?i)(^|(?<=\n)){word!s}.{{0,70}}\n'
    return word_pattern_tpl.format(word = re.escape(word))
def get_longest_word_pre_and_pos(txt, word, start = 0):
    word_pre = word
    #start = 0
    while word_pre:
        
        m = re.search(get_word_pattern_str(word_pre), txt, start)
        if m:
            begin = m.start()
            break
        word_pre = word_pre[:-1]
    else:
        raise Exception("fail to find one")
    return word_pre, begin




def get_explain(txt, word, word_pre, begin, nshow = 1,
                nfollow_at_fail = 12,
                nfollow_at_success = 0):

    explains = []
    rngs = []
    if word == word_pre:
        # when success
        tpl = get_word_pattern_str(word) + r'.*(\n|$)'
        count_ls = [1 for m in re.finditer(tpl, txt[begin:])]
        nshow += len(count_ls)
        
    for _, m in zip(range(nshow), re.finditer(r'.*\n.*(\n|$)', txt[begin:])):
        explains.append(m.group(0))
        rngs.append((m.start() + begin, m.end() + begin))
    assert rngs
    assert rngs[0][0] == begin

    explains = ''.join(explains)
    end = begin + len(explains)
    assert rngs[-1][-1] == end
    
##    m = re.match(r'.*\n.*(\n|$)', txt[begin:])
##    assert m
##    assert m.start() == 0
##    #print('file:', fn)
##    #print('word_prefix:', word_pre)
##    r = m.group(0)

    nfollow = nfollow_at_success
    if word_pre < word:
        nfollow = nfollow_at_fail
        
    follow_words = get_follow_words(txt, end, nfollow)
    explains += '\n'.join(follow_words)
    return explains

    
def get_follow_words(txt, begin, n):
    ls = []
    for _, m in zip(range(n), re.finditer(r'(.*)\n.*\n', txt[begin:])):
        if not m: break
        ls.append(m.group(1))
    return ls



def to_real_word(word):
    # remove all non-letter
    return ''.join(c for c in word if c.isalpha())
def get_fname(path, word):
    # word may be "-oid"
    word = to_real_word(word)
    assert word
    c = word[0].upper()
    assert 'A' <= c <= 'Z'


    # get folder
    n = ord(c) - ord('A') + 1
    folder = os.path.join(path, '{:0>4}{}'.format(n, c))
    
    fn = _get_fname(folder, word)
    fn = os.path.join(folder, fn)
    return fn

def _get_fname(folder, word):
    # get txt names
    for _, _, fnames in os.walk(folder):
        break
    else:
        raise Exception("empty or no such folder {}".format(folder))

    if not fnames:
        raise Exception("no files in folder {}".format(folder))
    

    # if only one file:
    if len(fnames) == 1:
        fn = fnames[0]
        tmp = (word[0] + '.txt').lower()
        if fn.lower() != tmp:
            raise Exception("the only one file {} in folder {} is not {}"\
                            .format(fname, folder, tmp)) 
        return fn

    
    # standardize fnames
    fnames.sort()
    ls = []
    pattern = re.compile(r'^(\w)-(\w+)\b[\.~,].*txt$')
    for fname in fnames:
        m = pattern.match(fname)
        if not m:
            raise Exception("unknown file {} in folder {}"\
                            .format(fname, folder))
        head, middle = m.group(1, 2)
        new = head + middle
        ls.append(new.lower())
    assert len(ls) == len(fnames)
    assert all(ls[i] < ls[i+1] for i in range(len(ls) - 1))

    
    # X -> Xa
    old_word = word
    if len(word) == 1:
        word += 'a'


    i = bisect.bisect_right(ls, word)
    if i == 0:
        #raise Exception("no file in folder {} contains word {!r}".format(folder, old_word))
        i = 1
    else:
        assert ls[i-1] <= word
        assert all(word < fn for fn in ls[i:i+1])
    
    i -= 1
    fn = fnames[i]
    return fn


#################33


    c2 = word[1].lower()
    head = '{}-{}\xff'.format(c, c2) # \xff to make head larger than any c-c2XXX.txt
    i = bisect.bisect_right(fnames, head)
##    if i == 0:
##        raise Exception("no file of name '{}.*.txt' in folder {}".format(head, folder))
    #i -= 1
    if len(fnames) == 1:
        assert i == 0
        i = 1 # for only one file: K.txt: '.' > '-'
    for fn in reversed(fnames[:i]):
        if re.match(r'(?i){}.*\.txt$'.format(c), fn):
            break
    else:
        raise Exception("no file of name '{}.*.txt' in folder {}".format(head[:-1], folder))

    fn = os.path.join(folder, fn)
    return fn


def record_word(fname, word, success):
    if success:
        line = word
    else:
        line = False, word
        
    with open(fname, 'a', encoding='utf8') as history:
        print(repr(word), file=history)
    

def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='get explain of the given word')
    parser.add_argument('word', type=str, \
                        help='word used to search its explanation')
    
    parser.add_argument('-p', '--path', type=str, \
                        default=dict_path,
                        help='path to english dictionary')
    
    parser.add_argument('-n', '--nshow', type=int, \
                        default = 1, 
                        help='number of the follow words whose explain will be shown.')

    parser.add_argument('-nf', '--nfollow_at_fail', type=int, \
                        default = 12,
                        help='number of the follow words who will be shown when fail.')

    parser.add_argument('-ns', '--nfollow_at_success', type=int, \
                        default = 0,
                        help='number of the follow words who will be shown when success.')

    parser.add_argument('-r', '--record_file', type=str, \
                        default = None, nargs='?',
                        help='record the input word to this file')


    args = parser.parse_args(args)

    path = args.path
    word = args.word.strip().lstrip('\\') # to find "-oid" (e.g. groupoid) ==>> input '" -oid"' or '\-oid'
    record_file = args.record_file
    #print(args.record_file)
    
    txt = get_dict_txt_for_explain(path, word)
    word_pre, pos = get_longest_word_pre_and_pos(txt, word)
    explain = get_explain(txt, word, word_pre, pos,
                          nshow = args.nshow,
                          nfollow_at_fail = args.nfollow_at_fail,
                          nfollow_at_success = args.nfollow_at_success)
    
    if record_file is not None:
        is_success = word == word_pre
        record_word(record_file, word, is_success)

    # bug fixed: once I mistook the 'UnicodeEncodeError'
    # I believed it was a decode error and can't figure out
    # why 'surrogateescape' does not fix the problem.
    encoding = sys.getfilesystemencoding() 
    explain = explain.encode(encoding, 'replace')
    explain = explain.decode(encoding)
    print(explain) 
    return 0
    


if __name__ == "__main__":
    main()

    
#print(get_explain(dict_path, 'python'))

    

    

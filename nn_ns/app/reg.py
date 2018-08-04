import hashlib


def reg(sitename, usrname = 'hh', datetime = '', length = 16):
    s = sitename + usrname + datetime
    b = s.encode('utf8')
    sha = hashlib.sha256()
    sha.update(b)
    d = sha.hexdigest()

    #print(len(d))
    assert 64 == len(d)
    
    userID, password = d[:length], d[length:2*length]
    return userID, password



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Yield userID and password')
    parser.add_argument('sitename', type=str, nargs=1,
                        help='sitename like "ltaaa.com"')
    parser.add_argument('usrname', type=str, nargs='?', default='hh',
                        help='user name to the site')
    parser.add_argument('datetime', type=str, nargs='?', default='',
                        help='the register datetime')
    parser.add_argument('length', type=int, nargs='?', default=16,
                        help='the length of userID and password')
    

    args = parser.parse_args()
    assert 0 < args.length <= 32

    #print((args.sitename[0], args.usrname, args.datetime, args.length))
    print(reg(args.sitename[0], args.usrname, args.datetime, args.length))

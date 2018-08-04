
try:
    try:
        raise ValueError()
    except ValueError:
        print('ValueError')
        raise
    except Exception:
        just-cannot-come-here
        print('Exception')
        raise
    except:
        just-cannot-come-here
        print('all exc')
        pass
except:
    # success
    pass

try:
    raise ValueError # omit '()'
except ValueError:
    print('ValueError')
    pass

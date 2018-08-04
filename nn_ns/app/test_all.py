
'''
import test_all
exec(test_all.text)

'''
text = '''
def test_all():
    #import sys
    #dir(sys.modules[__name__]) # except __name__ == '__main__'
    tests = []
    for item in globals().keys():
        if item[:5] == 'test_' and item != 'test_all':
            tests.append(item)

    for test in tests:
        print(test)
        exec(test + '()')

'''

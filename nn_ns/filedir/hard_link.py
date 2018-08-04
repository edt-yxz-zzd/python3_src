
'''
os.link(source, link_name) 
Create a hard link pointing to source named link_name.

Availability: Unix, Windows.


'''



if __name__ == "__main__":
    import os
    try:
        if len(sys.argv) < 2:
            pass
        elif len(sys.argv) == 3: # ['hard_link.py', '$source_path', '$link_name']
            os.link(sys.argv[1], sys.argv[2])
        else:
            raise ValueError('usage: python hard_link.py source_path link_name')
    except Exception as e:
        raise e

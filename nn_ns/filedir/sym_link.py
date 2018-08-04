
'''
os.symlink(source, link_name) 
os.symlink(source, link_name, target_is_directory=False) 
Create a symbolic link pointing to source named link_name.

On Windows, symlink version takes an additional optional parameter, target_is_directory, which defaults to False.

On Windows, a symlink represents a file or a directory, and does not morph to the target dynamically. If target_is_directory is set to True, the symlink will be created as a directory symlink, otherwise as a file symlink (the default).

Symbolic link support was introduced in Windows 6.0 (Vista). symlink() will raise a NotImplementedError on Windows versions earlier than 6.0.

Note
The SeCreateSymbolicLinkPrivilege is required in order to successfully create symlinks. This privilege is not typically granted to regular users but is available to accounts which can escalate privileges to the administrator level. Either obtaining the privilege or running your application as an administrator are ways to successfully create symlinks.

OSError is raised when the function is called by an unprivileged user.

Availability: Unix, Windows.




'''



if __name__ == "__main__":
    import os
    try:
        if len(sys.argv) < 2:
            pass
        elif len(sys.argv) == 3: # ['sym_link.py', '$source_path', '$link_name']
            os.link(sys.argv[1], sys.argv[2])
        else:
            raise ValueError('usage: python sym_link.py source_path link_name')
    except Exception as e:
        raise e

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#
# use os.walk() instead of this....!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#############################################################################
#############################################################################
#############################################################################
#############################################################################



### python file_tree.py $path $max_depth
#>>>python file_tree.py test/path_for_testing_file_tree/ 0
#test/path_for_testing_file_tree/



import os, operator #itemgetter, attrgetter


# node ~ [folder_name, subfolders, subfiles, sublinks]
# tree = node
# node[curfolder] = this folder's name or full path
# node[subfolders] = [ nodes of subfolders of this folder]
# node[subfiles] = [ subfiles of this folder]
# node[sublinks] = [ sublinks of this folder]

class _Txx: pass


class Node:
    def __init__(self, name, subnodes, subfiles, sublinks):
        # note: since the default value only calculated once,
        #       if used it, we'll always get the same object []!!!
        #assert type(name) == str
        #assert type(subnodes) == type(subfiles) == type(sublinks) == list 
        self.name = name # basename; sometime is a path for convenience
        self.subnodes = subnodes
        self.subfiles = subfiles
        self.sublinks = sublinks

    def __init__(self, name = ''):
        #assert type(name) == str
        self.name = name
        self.subnodes = []
        self.subfiles = []
        self.sublinks = []



    def __repr__(self, type_name = ''):
                                   #'Node'):
                                   #repr(type(_Txx()))[8:-2-len('_Txx')]+'Node'):
        return type_name + \
               repr((self.name, self.subnodes,
                     self.subfiles,self.sublinks))

    






def show_file_tree( path, max_depth = float('inf'),
                    prefix = '', prefix_sub = '', path_end = '/',
                    prefix_pad_char = ' ', branch_char = '|', link_char = '-',
                    depth = 0, printer = print):
    '''show the file tree of path

    #folderX stands for a folder name
    #fileX stands for a regular file name
    #symbolX stands for a link file name

    >>> show_file_tree( 'path_for_testing_python_file_tree', 0)
    path_for_testing_python_file_tree/

    >>> show_file_tree( 'path_for_testing_python_file_tree', 1)
    path_for_testing_python_file_tree/
    |-folder1/
    |-folder2/
    |-folder3/
    |-folder4/
    |-folder5/
    |
    |-symbol1
    |-symbol2
    |
    |-file1
    |-file2

    >>> show_file_tree( 'path_for_testing_python_file_tree')
    path_for_testing_python_file_tree/
    |-folder1/
    |-folder2/
    | |-folder1/
    | | |-symbol1
    | | |
    | | |-file1
    | |
    | |-folder2/
    | |-folder3/
    | | |-file1
    | |
    | |-symbol1
    | |-symbol2
    | |
    | |-file1
    | |-file2
    |
    |-folder3/
    |-folder4/
    |-folder5/
    |
    |-symbol1
    |-symbol2
    |
    |-file1
    |-file2
    
    '''

    show_tree( file_tree( path, max_depth),
               prefix = prefix, prefix_sub = prefix_sub, path_end = path_end,
               prefix_pad_char = prefix_pad_char, branch_char = branch_char,
               link_char = link_char, depth = depth, printer = printer)



def test_show_file_tree( word_dir = 'E:/temp_output/test/', create_files_first = False):
    cwd = os.getcwd()
    os.chdir(word_dir)
    top = 'path_for_testing_python_file_tree/'
    if create_files_first:
        if os.path.lexists(top):
            if os.path.isfile(top):
                os.remove(top)
            else:
                import shutil
                shutil.rmtree(top)
        
        os.makedirs(top)
        subfolders = [ 'folder' + str(i) for i in range(1,6)] + \
                     [ 'folder2/folder' + str(i) for i in range(1,4)]
        sublinks = ['symbol1','symbol2']
        subfiles = ['file1', 'file2']
        sub = [ ('',[1,2]), ('folder2/',[1,2]), ('folder2/folder1/',[1])]
        for name in subfolders:
            os.mkdir(top+name)

        for (pre, nums) in sub:
            for i in nums:
                file = top+pre+'file'+str(i)
                link = top+pre+'symbol'+str(i)
                open( file, 'w').close()
                os.symlink(file,link)

        open( top+'folder2/folder3/file1', 'w').close()


    import doctest
    
    #print(__name__)
    doctest.testmod()
    os.chdir(cwd)



def file_tree( path, max_depth = float('inf')):
    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError( 'path doesnot exist or is not a directory')
        return None

    # path maybe a link
    _path = path
    path = os.path.realpath(path)
        
    #if max_depth == 0, return [path]
    # node ~ [folder_name, subfolders, subfiles, sublinks]
    tree = Node( name = path)
    nul_root = Node()
    nul_root.subnodes.append(tree)

    # node and its path and the number of unhandled subnodes of it
    class Tuple:
        def __init__( self, node, path):
            self.node = node
            self.path = path
            self.num = len(node.subnodes)
            if ()self.

        def __repr__(self):
            return repr( (self.node, self.path, self.num) )
            
    stack = [ Tuple( node = nul_root, path = '')] 
    while(1):
        #print(stack)
        # to meet the need of max_depth
        if len(stack) > max_depth:
            #xxxx   Deletion of a target list recursively
            #xxxx   deletes each target, from left to right.
            #xxxxx del stack[max_depth:] #
            # what I want is:
            #stack = stack[:max_depth] # so, tree and all its subnodes will survive
            #??? why does it work?
            del stack[max_depth:]

        # pop empty set of unhandled folders
        while( stack and stack[-1].num < 1):
            stack.pop()

        # if all subfolders of depth < max_depth have been handled,
        # then stop
        if not stack:
            break

        # to get next node unhandled
        stack[-1].num -= 1

        # now the top folder's todo[1]th subfolder's
        #       todo[2]th subfolder's... todo[-1]th subfolder
        #       will be handled
        # the followed section yields the desired node and path
        node = stack[-1].node.subnodes[ stack[-1].num]
        path = os.path.join( stack[-1].path, node.name)

        # list contents of path
        ls = os.listdir( path)
        for f in ls:
            p = os.path.join( path, f)
            if os.path.islink(p):
                node.sublinks.append(f)
            elif os.path.isfile(p):
                node.subfiles.append(f)
            elif os.path.isdir(p):
                node.subnodes.append(Node(name=f))
            else:
                raise 'logic_error: design error!!'


        node.sublinks.sort()
        node.subfiles.sort()
        node.subnodes.sort(key=operator.attrgetter('name'))

        # push those new subfolders to be handled
        stack.append( Tuple( node = node, path = path))

    tree.name = _path
    return tree




def show_tree( node, prefix = '', prefix_sub = '', path_end = '/', prefix_pad_char = ' ', branch_char = '|', link_char = '-', depth = 0, printer = print):
    # prefix     = '| | |-'
    # prefix_sub = '| | | '
    printer( prefix + node.name + path_end)
    depth += 1
    subfolder_prefix     = prefix_sub + branch_char + link_char
    subfolder_prefix_sub = prefix_sub + branch_char + prefix_pad_char
    subfile_prefix       = prefix_sub + branch_char + link_char
    sublink_prefix       = prefix_sub + branch_char + link_char

    line_break = prefix_sub + branch_char
    
    for subnode in node.subnodes:
        show_tree( subnode,
                   prefix       = subfolder_prefix,
                   prefix_sub   = subfolder_prefix_sub,
                   path_end     = path_end,
                   prefix_pad_char = prefix_pad_char,
                   branch_char  = branch_char,
                   link_char    = link_char,
                   depth        = depth,
                   printer = printer)
        
        if subnode is not node.subnodes[-1] and  \
           len(subnode.subnodes) + \
           len(subnode.sublinks) + \
           len(subnode.subfiles) != 0:
            printer( line_break)
        
    if len(node.subnodes) and len(node.sublinks)+len(node.subfiles):
        printer( line_break)

    for sublink in node.sublinks:
        printer( sublink_prefix + sublink)

    if len(node.sublinks) and len(node.subfiles):
        printer( line_break)
        
    for subfile in node.subfiles:
        printer( subfile_prefix + subfile)

    return





        
if __name__ == "__main__":
    import sys
    try:
        #print( sys.argv)
        if len(sys.argv) < 2:
            pass
        elif len(sys.argv) == 2: # ['file_tree.py', '$path']
            show_file_tree(sys.argv[1])
        elif len(sys.argv) == 3: # ['file_tree.py', '$path', '$max_depth']
            show_file_tree(sys.argv[1], int(sys.argv[2]))
        else:
            raise ValueError('usage: python file_tree.py path [max_depth]')
    except Exception as e:
        #print('usage: python file_tree.py path [max_depth]')
        raise e

    

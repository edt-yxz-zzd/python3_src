
import os

Null = 0
'''
def dir2dict(path):
    if not os.path.isdir(path):
        return Null

    d = {}
    for file in os.listdir(path):
        d[file] = dir2dict(os.path.join(path, file))

    return d
def _dir2dict(path):
    return dict((k,v) for k, v in dir2dict(path).items() if v != Null)
'''

def dir2list(path):
    if not os.path.isdir(path):
        return Null

    d = []
    for file in os.listdir(path):
        e = (file, dir2list(os.path.join(path, file)))
        d.append(e)

    d.sort()
    return d

def _dir2list(path):
    return list((k,v) for k, v in dir2list(path) if v != Null)

def list2dict_str(ls):
    if type(ls) != list:
        return repr(ls)

    str_ls = []
    for k, v in ls:
        kv = '{key}:{value}'.format(key=repr(k), value=list2dict_str(v))
        str_ls.append(kv)

    return '{' + ','.join(str_ls) + '}'



def gen_index(path = '.', encoding = 'gb18030'):
    s = index_htm_tpl.replace('{place_encoding_here}', encoding)
    s = s.replace('{place_data_here}', list2dict_str(_dir2list(path)))

    data = s.encode(encoding)
    with open('index.htm', 'wb') as fout:
        fout.write(data)

index_htm_tpl = r'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> 
<html xmlns="http://www.w3.org/1999/xhtml"> 
<head> 
<meta http-equiv="Content-Type" content="text/html; charset={place_encoding_here}" /> 
<title>view images</title>

<style type="text/css">
    body, ul { 
        padding:0; 
        background-color: #eee; 
        list-style-type: none; 
    }
</style>

<script>

var Null = 0;//null;
var files = {place_data_here};

files = {'.':files}


img_tpl = "<img src='{id}' width='100%'><br />\n"

dir_tpl_1 = "<li onclick='_onclick(this)' id='li:{id}'><a href='#a:{id}' id='a:{id}'>"
dir_tpl_2 = "{base}"
dir_tpl_3 = "</a></li>\n<subfolder id='subfolder:{id}'></subfolder>\n"
subfolder_id_tpl = 'subfolder:{id}'

function gen_dir_tpl(id, base){
    return dir_tpl_1.replace(/\{id\}/g, id) +
            base +
            dir_tpl_3.replace(/\{id\}/g, id);
}

var curr_path = '.';
function _onclick(element){try{//alert('aff');
    path = element.attributes['id'].value.slice(3);
    if (curr_path.indexOf(path) === 0) {
        var ps = path.split('/');
        ps.pop();
        path = ps.join('/')
    }

    open_dir(path);
    curr_path = path;

    //a_title = element.getElementsByTagName('a')[0]
    //a_title.blur()
    //a_title.focus();
}catch(err){alert(err);document.write(err);}
}



function _open_dir(folder, id, base, ps){
    var ls = [];
    var link;
    for (file in folder){
        file_id = id + '/' + file;
        if (folder[file] === Null){
            link = img_tpl.replace(/\{id\}/g, file_id);
        }
        else{
            link = gen_dir_tpl(file_id, file);
        }
        ls.push(link)
    }
    return '<ul>' + ls.join('<br />') + '</ul>'
}
function open_dir(path){
    var ps = path.split('/');
    ps.reverse();
    var folder = files;
    var id = '';
    var base;
    while(ps.length){
        base = ps.pop();
        id += base;
        folder = folder[base];
        
        //alert('base:' + base);
        subfolder_id = subfolder_id_tpl.replace(/\{id\}/g, id);
        innerHTML = _open_dir(folder, id, base, ps);
        document.getElementById(subfolder_id).innerHTML = innerHTML;
        id += '/';
    }
}

function init(body){
    //this.innerHTML = "<subfolder id='subfolder:.'></subfolder>";
    open_dir(curr_path);
    
}

</script>


</head> 

<body> 
<subfolder id='subfolder:.'></subfolder>
<script> init(0) </script>
</body> 
</html>
'''



def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='generate "index.html" to view comics')
    parser.add_argument('path', type=str, \
                        help='comic folder and the folder to output index.html')

    parser.add_argument('encoding', type=str, \
                        nargs='?', default='gb18030',
                        help='encoding of index.html')

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    
    gen_index(args.path, args.encoding)
        

    


if __name__ == "__main__":
    main()



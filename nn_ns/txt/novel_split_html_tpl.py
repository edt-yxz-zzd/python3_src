
r'''
novel.txt:
----------------------------------------
head...
vol. 1
v1head...
chapter. 1
chapter1txt...
----------------------------------------

err: re_seps = [r'(?m)^vol. \d+$', r'(?m)^chapter. \d+$']
re_seps = [r'(?m)(^vol. \d+\s*\n)', r'(?m)(^chapter. \d+\s*\n)']
result = list of (path_parts, txt)
= [
    ((), head...),
    (('vol. 1',), v1head...),
    (('vol. 1', 'chapter. 1'), chapter1txt...),
]
'''

r'''
<!DOCTYPE html>
<html>
<head>
    <meta charset={encoding!r}/>
    <title>{title}</title>


    <link rel="stylesheet" type="text/css" href={style_css_fname!r} />
    <style type="text/css">
        {styles}
    </style>

    <script src="jquery-1.4.2.min.js"></script>
    <!-- <script src="http://code.jquery.com/jquery-1.4.2.min.js"></script> -->
</head>


<body>
<p>c</p>
<dl>
<dt level=1><a id="a1" href="#a1">1</a></dt>
<dd>
    <p>c1</p>
    <dl>
    <dt level=2>1.1</dt>
    <dd>
        <p>c1.1</p>
    </dd>


    <dt level=2>1.2</dt>
    <dd>
        <p>c1.2</p>
    </dd>
    </dl>
</dd>


<dt level=1><a href="#">2</a></dt>
<dd>
    <p>c2</p>
    <dl>
    <dt level=2>2.1</dt>
    <dd>
        <p>c2.1</p>
    </dd>


    <dt level=2>2.2</dt>
    <dd>
        <p>c2.2</p>
    </dd>
    </dl>
</dd>
</dl>

</body>


<script src={action_js_fname!r}></script>
<script type="text/javascript">
{jscript}
</script>

</html>
'''



style_css = r'''
dd { display: none; }
body, dl { padding:0; background-color: #eee; list-style-type: none; }
'''

action_js = r'''
elems = [null];

function get_elem(level){
    if (level < elems.length){
        return elems[level];
    }
    alert("error: index outside array");
    return null;
}

function _hide_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).hide();
}

function _show_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).slideDown();
}

function _toggle_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).toggle();
}

function set_elem(level, elem){
    clear_elems_to(level);
    if (elem && (elem === get_elem(level))){
        clear_elems_to(level-1);
    }
    else{
        _hide_elem(level);
        elems[level] = elem;
        _show_elem(level);
    }
}

function clear_elems_to(level){
    while (!(level < elems.length)){
        elems.push(null);
    }

    while ((level+1) < elems.length){
        _hide_elem(elems.length-1);
        elem = elems.pop();
    }
}


function next_elem(curr){
    var next = curr;
    if (next === null) alert("error: next == null");
    for (next = next.nextSibling; next; next = next.nextSibling){
        if (next.nodeType === 1) break;
    }
    return next;
}

$('dt').click(
        function(){
            var level = parseInt(this.getAttribute("level"));
            var next = next_elem(this);
            set_elem(level, next);
            //this.focus();
        }
    );
'''



'''
    html = (html_head, html_body, jscript)
    html_head = (encoding, title, style_css, jquery)
    html_body = content_dl
    content_dl = (content, [dt_dd])
    dt_dd = (level, id, href, title, content_dl)
'''

html_tpl = r'''
<!DOCTYPE html>
<html>
<head>
    <meta charset={encoding!r}/>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href={style_css_fname!r} />
    <style type="text/css">
        {styles}
    </style>

    <script src="jquery-1.4.2.min.js"></script>
    <!-- <script src="http://code.jquery.com/jquery-1.4.2.min.js"></script> -->
</head>


<body>
{content_dl}
</body>

<script src={action_js_fname!r}></script>
<script type="text/javascript">
{jscript}
</script>

</html>
'''



content_dl_tpl = r'''
<p>{content}</p>
<dl>
{dt_dd_ls}
</dl>
'''
dt_dd_tpl = r'''
<dt level={level}><a id="{id!s}" href="#{id!s}">{title}</a></dt>
<dd>
{content_dl}
</dd>
'''





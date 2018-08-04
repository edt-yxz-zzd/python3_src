var elems = [null]; // elems[0] === null
var KEY_LEFT = 37;
var KEY_RIGHT = 39;
var KEY_BACKSPACE = 8;
var KEY_FORWARD_SLASH = 191;
var curr_a_id = null;


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
    //alert("hide");
}

function _show_elem(level){
    elem = get_elem(level);
    if (elem) $(elem).show();
    //alert("show");
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


function next_elem(curr){ // dt to dd // title to content
    var next = curr;
    if (next === null) alert("error: next == null");
    for (next = next.nextSibling; next; next = next.nextSibling){
        if (next.nodeType === 1) break;
    }
    return next;
}
function dt_a__onclick(this_elem){
            var dt = this_elem.parentNode;
            var level = parseInt(dt.getAttribute("level"));
            var next = next_elem(dt);
            set_elem(level, next);
            //alert([elems.length, elems]);
            //alert(curr_a_id);
            curr_a_id = this_elem.id; // globol curr_a_id
            //alert(next_aid());
            this_elem.focus();
            //this_elem.blur();
        }
$('dt a').click(
    function(){dt_a__onclick(this);});



////////////////////////////////
function __get_last_aid(){
    var a_ls = document.getElementsByTagName('a');
    var i = a_ls.length;
    while (i --> 0){
        aid = a_ls[i].id;
        if (is_aid(aid)){
            return aid;
        }
    }
    return null;
}

function __get_first_aid(){
    var a_ls = document.getElementsByTagName('a');
    var i = 0;
    for (; i < a_ls.length; ++i){
        aid = a_ls[i].id;
        if (is_aid(aid)){
            return aid;
        }
    }
    return null;
}


last_aid = __get_last_aid();
first_aid = __get_first_aid();
last_aid_idx = null_aid2idx(last_aid);
first_aid_idx = null_aid2idx(first_aid);

function is_aid(aid){
    return aid && aid.length >= 3 && aid.slice(0, 3) == 'aid';
}
function null_aid2idx(aid){
    return aid === null? null : aid2idx(aid);
}
function aid2idx(aid){
    return parseInt(aid.slice(3, aid.length));
}
function idx2aid(idx){
    return 'aid' + idx;
}
function next_aid(){
    if (curr_a_id === null){
        return first_aid;
    }
    
    var i = aid2idx(curr_a_id);
    return i < last_aid_idx ? idx2aid(i+1) : last_aid;
}
function prev_aid(){
    if (curr_a_id === null){
        return last_aid;
    }
    
    var i = aid2idx(curr_a_id);
    return i > first_aid_idx ? idx2aid(i-1) : first_aid;
}
function curr_aid(){
    return curr_a_id;
}


function click_aid(aid){
    if (aid){
        var a = document.getElementById(aid);
        //dt_a__onclick(a);
        a.click();
    }
}

var open_aid = click_aid;

function onright(){
    // open next aid
    open_aid(next_aid());
    
}
function onleft(){
    open_aid(prev_aid());
}
function click_curr_aid(){
    click_aid(curr_aid());
}


var trigger = document.getElementsByTagName('body')[0];
trigger.addEventListener('keydown', onarrow_left_right, false);
function onarrow_left_right(e) {
    //alert([e.target, e.type, e.button, e.keyCode])
    //alert('press key ' + e.keyCode);
    if (e.keyCode == KEY_RIGHT)onright(); //{alert('right');}
    else if (e.keyCode == KEY_LEFT)onleft(); //{alert('left');}
    else if (e.keyCode == KEY_FORWARD_SLASH)click_curr_aid();
    else return false;
    return true;
}








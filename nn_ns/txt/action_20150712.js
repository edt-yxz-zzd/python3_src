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


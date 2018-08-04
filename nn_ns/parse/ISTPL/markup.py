

r'''
using python literals to implement a markup-like language

ast.literal_eval
LiteralType can be yielded by literal_eval
AnyType is LiteralType


NameType == None or is union of int float bool str bytes tuple of NameType
NameType is LiteralType, is hashable

StreamType is a list
NodeType is a 1/2/3-tuple (tag, attrs?, content?)
    tag is of NameType
    attrs is a dict of (NameType, AnyType), attrs[attr]=value
        attrs can be divided into 2 classes: known/unknown
        known-attrs -> required/nonrequired
        nonrequired-attrs -> default/inherited # require init_value
            attrx = ('@sys@', 'default', attr)
            parent.attrx -> this.attrx -> this.attr
            if set this.attr, then
                default-attr -> pass
                inherited-attr -> set this.attrx the same value
    content == None or is list of NodeType StreamType
        None means this is an empty-tag # html?


TagDefine: tag_name, known_attr's name and property, content type
ClassDefine: class_name, base_class_names
TypeDefine:
    buildin: bool int float, str bytes, tuple, list set dict
    Alias <typename>
    Array <type, min=0, max=None> # tuple, too; but only one value type
    Struct <types...> # tuple, too; fixed length
    List <type, min=0, max=None> # like array; but mutable
    Dict <key_type, value_type>
    Set <type>
    Union <types...>
    Disjoint <types...>
    Not <type>
    Enum of constants # includes empty set : ('@sys@', 'set', [])
    Rex of str bytes # regular expression
    Range of int # integer range

    AnyType
    NameType
    NodeType <tagname, attrs_constraint>
    StreamType
    SysType <typename, args_type> # ('@sys@', typename, args)
        typename = set Enum Rex Range NameType NodeType SysType Union

        

('typedef', [
    ####('Rex', {'id': 'TypeNameType', 'rex': '[_\w][_\w\d]*'}),
    #('Range', {'id': 'Mod6Type', start=0, stop=6, step=1}),
    ('Enum', {'id':'NoneType', 'enum':[None]}),
    
    ('Union', {'id':'LiteralType', 'union': [
        'str', 'bytes', 'int', 'float', 'tuple',
        'list', 'dict', 'set', 'bool', 'NoneType']}),
        
    ('Alias', {'id':'AnyType', 'type': 'LiteralType'}),

    
    ('Union', {'id':'NameType', 'union': [
        'str', 'bytes', 'int', 'float', 'bool', 'NoneType',
        'Array(NameType)']}),
    ('Array', {'id':'Array(NameType)',
        'type': 'NameType', 'min'=0, 'max'=None}),

        
    ('Struct', {'id':'NodeType_tag', 'types':['NameType']}),
    ('Struct', {'id':'NodeType_tag_attrs', 'types':['NameType', 'AttrsType']}),
    ('Struct', {'id':'NodeType_tag_content',
        'types':['NameType', 'ContentType']}),
    ('Struct', {'id':'NodeType_tag_attrs_content',
        'types':['NameType', 'AttrsType', 'ContentType']}),
    ('Union', {'id':'NodeType', 'union': [
        'NodeType_tag', 'NodeType_tag_attrs', 'NodeType_tag_content',
        'NodeType_tag_attrs_content']}),

    
    ('Dict', {'id':'AttrsType',
        'key_type': 'NameType', 'value_type'='AnyType'}),

    ('List', {'id':'StreamType', 'type': 'AnyType'}),
    ('Union', {'id':'ContentType_sub', 'union': ['StreamType', 'NodeType']}),
    ('List', {'id':'ContentType_list', 'type': 'ContentType_sub'}),
    ('Union', {'id':'ContentType', 'types': ['ContentType_list', 'NoneType']}),

    
])


'''

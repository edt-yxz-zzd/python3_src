
import sqlite3
import ast


con = sqlite3.connect(":memory:")

#DROP TABLE customer;

stats = [
    '''CREATE TABLE author_id_n_file_id_set (
        author_id TEXT, file_id TEXT, 
        CONSTRAINT author_id_n_file_id_pk PRIMARY KEY (author_id, file_id),
        CONSTRAINT author_id_fk FOREIGN KEY (author_id)
            REFERENCES author_id_set (author_id),
        CONSTRAINT file_id_fk FOREIGN KEY (file_id)
            REFERENCES file_id_set (file_id));
    ''',
    'CREATE TABLE tag_n_file_id_set (tag TEXT PK FK, file_id TEXT PK FK);',]



def make_composite_pk_set_fields_raw_n_table_n_file_name(field_names):
    raw_table_name = '_n_'.join(field_names)
    table_name = '{}_set'.format(raw_table_name)
    fname = '{}.txt'.format(table_name)
    fields_str = ', '.join(field_names)
    return fields_str, raw_table_name, table_name, fname

def make_composite_pk_set_create_stat(field_names, data_types):
    assert len(field_names) == len(data_types)
    fields_str, raw_table_name, table_name, fname = \
                    make_composite_pk_set_fields_raw_n_table_n_file_name(\
                        field_names)
  
    pk_constraint_name = '{}_pk'.format(raw_table_name)
    fields_def = ', '.join('{field_name} {data_type}'\
                           .format(field_name=field_name, data_type=data_type)
                           for field_name, data_type in zip(field_names, data_types))
    pk_constraint = 'CONSTRAINT {} PRIMARY KEY ({})'\
                    .format(pk_constraint_name, fields_str)
    fk_constraint_tpl = 'CONSTRAINT {field_name}_fk FOREIGN KEY ({field_name}) '\
            'REFERENCES {field_name}_set ({field_name})'
    fk_constraints = ', '.join(fk_constraint_tpl.format(field_name=field_name) \
                               for field_name in field_names)
    create_stat = 'CREATE TABLE {table_name} ({fields_def}, '\
                  '{pk_constraint}, {fk_constraints});'\
                  .format(table_name=table_name, fields_def=fields_def,
                          pk_constraint=pk_constraint, fk_constraints=fk_constraints)
    return create_stat



def create_composite_pk_set_table(field_names, data_types, cursor):
    create_stat = make_composite_pk_set_create_stat(field_names, data_types)
    cursor.execute(create_stat)


def fill_composite_pk_set_table(field_names, cursor, encoding=None):
    fields_str, raw_table_name, table_name, fname = \
                    make_composite_pk_set_fields_raw_n_table_n_file_name(\
                        field_names)
    insert_stat = 'INSERT INTO {table_name} ({field_names}) values ({question_marks})'\
                  .format(table_name=table_name, field_names=fields_str,
                          question_marks = ', '.join('?'*len(field_names)))
    
    
    for line in read_map_table_txt(fname, encoding=encoding):
        cursor.execute(insert_stat, line)

def show_composite_pk_set_table(field_names, cursor):
    fields_str, raw_table_name, table_name, fname = \
                    make_composite_pk_set_fields_raw_n_table_n_file_name(\
                        field_names)
    select_stat = 'SELECT {field_names} FROM {table_name}'\
                  .format(table_name=table_name, field_names=fields_str)
    
    cursor.execute(select_stat)
    print('show table {table_name} ({field_names})'\
          .format(table_name=table_name, field_names=fields_str))
    for row in cursor.fetchall():
        print('\t', *row)




    
def read_nonempty_lines(fname, encoding=None):
    with open(fname, encoding=encoding) as fin:
        for line in fin:
            line = line.strip()
            if line:
                yield line






def read_set_table_txt(fname, encoding=None):
    return read_nonempty_lines(fname, encoding=encoding)

def read_map_table_txt(fname, encoding=None):
    return map(ast.literal_eval,
               read_nonempty_lines(fname, encoding=encoding))
    with open(fname) as fin:
        for line in fin:
            line = line.strip()
            if line:
                ls.append(literal.eval(line))
    return ls

def make_set_table_n_file_name(field_name):
    table_name = '{}_set'.format(field_name)
    fname = '{}.txt'.format(table_name)
    return table_name, fname

def create_set_table(field_name, cursor, *, data_type = 'TEXT'):
    table_name, fname = make_set_table_n_file_name(field_name)
    create_stat = 'CREATE TABLE {table_name} ({field_name} {data_type} PRIMARY KEY);'\
                  .format(table_name=table_name, field_name=field_name, data_type=data_type)
    cursor.execute(create_stat)
    
def fill_set_table(field_name, cursor, encoding=None):
    table_name, fname = make_set_table_n_file_name(field_name)
    insert_stat = 'INSERT INTO {table_name} ({field_name}) values (?)'\
                  .format(table_name=table_name, field_name=field_name)
    
    for line in read_set_table_txt(fname, encoding=encoding):
        cursor.execute(insert_stat, (line,))

def show_set_table(field_name, cursor):
    table_name, fname = make_set_table_n_file_name(field_name)
    select_stat = 'SELECT {field_name} FROM {table_name}'\
                  .format(table_name=table_name, field_name=field_name)
    
    cursor.execute(select_stat)
    print('show table {table_name} ({field_name})'\
          .format(table_name=table_name, field_name=field_name))
    for row in cursor.fetchall():
        print('\t', *row)


def show_tag2tag():
    tags = list(set(tag for tags in read_map_table_txt('tag2super_tag.txt')
                    for tag in tags))
    tags.sort()
    for tag in tags:
        print(tag)

    

cur = con.cursor()
#con.execute(stat)

e = con.execute
f = cur.fetchall
field_names = ['file_id', 'author_id', 'tag', 'file_format', 'media_type']
composite_pk_field_names_ls = [('author_id', 'file_id'), ('tag', 'file_id')]

cursor = cur
for field_name in field_names:
    create_set_table(field_name, cursor)
    fill_set_table(field_name, cursor)
    #show_set_table(field_name, cursor)

data_types = ['TEXT'] * 2
for field_names in composite_pk_field_names_ls:
    create_composite_pk_set_table(field_names, data_types, cursor)
    fill_composite_pk_set_table(field_names, cursor)
    show_composite_pk_set_table(field_names, cursor)

##for i, stat in enumerate(stats):
##    cur.execute(stat)




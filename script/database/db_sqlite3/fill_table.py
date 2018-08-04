

import ast
from make_create_stat import make_fields_str, \
     make_raw_n_table_name_of_composite_pk_set, \
     table_name2file_name, make_table_name_of_set


def make_insert_stat(table_name, field_names):
    fields_str = make_fields_str(field_names)
    insert_stat = 'INSERT INTO {table_name} ({field_names}) values ({question_marks})'\
                  .format(table_name=table_name, field_names=fields_str,
                          question_marks = ', '.join('?'*len(field_names)))
    return insert_stat


    
def make_insert_stat_of_composite_pk_set(field_names):
    raw_table_name, table_name = make_raw_n_table_name_of_composite_pk_set(field_names)
    insert_stat = make_insert_stat(table_name, field_names)
    return insert_stat

def make_insert_stat_of_set(field_name):
    insert_stat = make_insert_stat_of_composite_pk_set([field_name])
    return insert_stat


def make_insert_stat_of_map(table_name, field_names):
    insert_stat = make_insert_stat(table_name, field_names)
    return insert_stat



#######################################


    
def read_nonempty_lines(fname, encoding=None):
    #print(fname)
    with open(fname, encoding=encoding) as fin:
        for line in fin:
            line = line.strip()
            if line:
                yield line

def read_strs_txt(fname, encoding=None):
    return map((lambda s:(s,)), read_nonempty_lines(fname, encoding=encoding))

def read_tuple_reprs_txt(fname, encoding=None):
    return map(ast.literal_eval,
               read_nonempty_lines(fname, encoding=encoding))


def fill_table(table_name, field_names, reader, encoding=None):
    fname = table_name2file_name(table_name)
    insert_stat = make_insert_stat(table_name, field_names)
    for row in reader(fname, encoding=encoding):
        yield (insert_stat, row)


def fill_table_args_of_set(field_name):
    return make_table_name_of_set(field_name), [field_name], read_strs_txt


def fill_table_args_of_composite_pk_set(field_names):
    _raw, table_name = make_raw_n_table_name_of_composite_pk_set(field_names)
    return table_name, field_names, read_tuple_reprs_txt


def fill_table_args_of_map(table_name, field_names):
    return table_name, field_names, read_tuple_reprs_txt




##################################33


def _fields_or_all(field_names):
    if field_names:
        fields_str = make_fields_str(field_names)
    else:
        fields_str = '*'
    return fields_str

def make_select_stat(table_name, field_names=None):
    fields_str = _fields_or_all(field_names)
    select_stat = 'SELECT {field_names} FROM {table_name}'\
                  .format(table_name=table_name, field_names=fields_str)
    return select_stat

def show_table(cursor, table_name, field_names=None):
    select_stat = make_select_stat(table_name, field_names)
    cursor.execute(select_stat)
    
    fields_str = _fields_or_all(field_names)
    print('show table {table_name} ({field_names})'\
          .format(table_name=table_name, field_names=fields_str))
    for row in cursor.fetchall():
        print('\t', *row)

        


    


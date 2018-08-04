

from make_create_stat import make_create_stat, \
    make_table_name_of_set


example = 'CREATE TABLE tag_set (tag TEXT PRIMARY KEY);'

def make_create_stat_of_set(field_name, data_type):
    table_name, fname = make_table_n_file_name_of_set(field_name)
    create_stat = 'CREATE TABLE {table_name} ({field_name} {data_type} PRIMARY KEY);'\
                  .format(table_name=table_name, field_name=field_name, data_type=data_type)
    return create_stat


def make_create_stat_of_set(field_name, data_type):
    table_name = make_table_name_of_set(field_name)
    
    field_names = [field_name]
    data_types = [data_type]
    num_pk_fields = len(field_names)
    foreign_table_n_field_names = []
    create_stat = make_create_stat(table_name, field_names, data_types,
                                   num_pk_fields, foreign_table_n_field_names)
    return create_stat



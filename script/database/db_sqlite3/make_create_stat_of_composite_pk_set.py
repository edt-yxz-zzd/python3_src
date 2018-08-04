

from make_create_stat import make_create_stat, \
    make_raw_n_table_name_of_composite_pk_set, \
    make_table_name_of_set


example = '''
    CREATE TABLE author_id_n_file_id_set (
        author_id TEXT NOT NULL, file_id TEXT NOT NULL, 
        CONSTRAINT author_id_n_file_id_pk PRIMARY KEY (author_id, file_id),
        CONSTRAINT author_id_fk FOREIGN KEY (author_id)
            REFERENCES author_id_set (author_id),
        CONSTRAINT file_id_fk FOREIGN KEY (file_id)
            REFERENCES file_id_set (file_id));
    '''

    
def make_create_stat_of_composite_pk_set(field_names, data_types):
    fields_def = make_fields_def(field_names, data_types)
    fields_str, raw_table_name, table_name, fname = \
                    make_fields_raw_n_table_n_file_name_of_composite_pk_set(\
                        field_names)
  
    pk_field_names = field_names
    pk_constraint = make_pk_constraint(pk_field_names)
    
    fk_constraint_tpl = 'CONSTRAINT {field_name}_fk FOREIGN KEY ({field_name}) '\
            'REFERENCES {field_name}_set ({field_name})'
    fk_constraints = ', '.join(fk_constraint_tpl.format(field_name=field_name) \
                               for field_name in field_names)
    create_stat = 'CREATE TABLE {table_name} ({fields_def}, '\
                  '{pk_constraint}, {fk_constraints});'\
                  .format(table_name=table_name, fields_def=fields_def,
                          pk_constraint=pk_constraint, fk_constraints=fk_constraints)
    return create_stat



def make_create_stat_of_composite_pk_set(field_names, data_types):
    raw_table_name, table_name = \
                    make_raw_n_table_name_of_composite_pk_set(\
                        field_names)

    num_pk_fields = len(field_names)
    foreign_table_n_field_names = []
    for ref_field_name in field_names:
        ref_table_name = make_table_name_of_set(ref_field_name)
        foreign_table_n_field_names.append((ref_table_name, [ref_field_name]))
        
    create_stat = make_create_stat(table_name, field_names, data_types,
                                   num_pk_fields, foreign_table_n_field_names)
    return create_stat





from make_create_stat import make_create_stat


example = '''
    CREATE TABLE tag2super_tag (
        tag TEXT  NOT NULL, super_tag TEXT  NOT NULL, 
        CONSTRAINT tag_pk PRIMARY KEY (tag),
        CONSTRAINT tag_fk FOREIGN KEY (tag)
            REFERENCES tag_set (tag),
        CONSTRAINT super_tag_fk FOREIGN KEY (super_tag)
            REFERENCES tag_set (tag));
    '''



def make_create_stat_of_map(table_name, field_names, data_types,
                            num_pk_fields, foreign_table_n_field_names):
    assert len(field_names) == len(data_types)
    assert sum(len(fs) for t, fs in foreign_table_n_field_names) <= len(field_names)
    
    fields_def = make_fields_def(field_names, data_types)
    pk_field_names = field_names[:num_pk_fields]
    pk_constraint = make_pk_constraint(pk_field_names)
    fk_constraints = make_fk_constraints(field_names, foreign_table_n_field_names)

    create_stat = 'CREATE TABLE {table_name} ({fields_def}, '\
                  '{pk_constraint}, {fk_constraints});'\
                  .format(table_name=table_name, fields_def=fields_def,
                          pk_constraint=pk_constraint, fk_constraints=fk_constraints)
    return create_stat


def make_create_stat_of_map(table_name, field_names, data_types,
                            num_pk_fields, foreign_table_n_field_names):
    return make_create_stat(table_name, field_names, data_types,
                            num_pk_fields, foreign_table_n_field_names)




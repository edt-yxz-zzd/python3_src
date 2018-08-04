
import os.path

data_path = 'data/'

def table_name2file_name(table_name):
    fname = '{}.txt'.format(table_name)
    fullfilename = os.path.join(data_path, fname)
    return fullfilename


def make_table_name_of_set(field_name):
    raw_table_name, table_name = \
                    make_raw_n_table_name_of_composite_pk_set([field_name])
    return table_name


def make_raw_n_table_name_of_composite_pk_set(field_names):
    raw_table_name = make_joinand_fields_str(field_names)
    table_name = '{}_set'.format(raw_table_name)
    return raw_table_name, table_name



def make_fields_def(field_names, data_types):
    assert len(field_names) == len(data_types)
    fields_def = ', '.join('{field_name} {data_type}  NOT NULL'\
                           .format(field_name=field_name, data_type=data_type)
                           for field_name, data_type in zip(field_names, data_types))
    return fields_def

def make_fields_str(field_names):
    fields_str = ', '.join(field_names)
    return fields_str


def make_joinand_fields_str(field_names):
    joinand_fields_str = '_n_'.join(field_names)
    return joinand_fields_str

def make_pk_constraint(pk_field_names):
    joinand_fields_str = make_joinand_fields_str(pk_field_names)
    fields_str = make_fields_str(pk_field_names)
    pk_constraint_name = '{}_pk'.format(joinand_fields_str)
    
    pk_constraint = 'CONSTRAINT {} PRIMARY KEY ({})'\
                    .format(pk_constraint_name, fields_str)
    return pk_constraint


def make_fk_constraint(fk_field_names, ref_table_name, ref_field_names):
    assert len(fk_field_names) == len(ref_field_names) > 0
    
    joinand_fields_str = make_joinand_fields_str(fk_field_names)
    fields_str = make_fields_str(fk_field_names)
    fk_constraint_name = '{}_fk'.format(joinand_fields_str)
    ref_fields_str = make_fields_str(ref_field_names)
    
    fk_constraint_tpl = (#'CONSTRAINT {fk_constraint_name} '\
                        'FOREIGN KEY ({field_names}) '\
            'REFERENCES {ref_table_name} ({ref_field_names}) '\
            'ON DELETE RESTRICT ON UPDATE RESTRICT')
    fk_constraint = fk_constraint_tpl.format(fk_constraint_name=fk_constraint_name,
                                             field_names=fields_str,
                                             ref_table_name=ref_table_name,
                                             ref_field_names=ref_fields_str)

    return fk_constraint

def make_fk_constraints(field_names, foreign_table_n_field_names):
    assert sum(len(fs) for t, fs in foreign_table_n_field_names) <= len(field_names)

    i = 0
    ls = []
    for ref_table_name, ref_field_names in foreign_table_n_field_names:
        L = len(ref_field_names)
        fk_field_names = field_names[i:i+L]
        fk_constraint = make_fk_constraint(fk_field_names, ref_table_name, ref_field_names)
        i += L
        ls.append(fk_constraint)
    fk_constraints = ls
    return fk_constraints



def make_create_stat(table_name, field_names, data_types,
                     num_pk_fields, foreign_table_n_field_names):
    assert len(field_names) == len(data_types)
    assert sum(len(fs) for t, fs in foreign_table_n_field_names) <= len(field_names)
    
    fields_def = make_fields_def(field_names, data_types)
    pk_field_names = field_names[:num_pk_fields]
    pk_constraint = make_pk_constraint(pk_field_names)
    fk_constraints = make_fk_constraints(field_names, foreign_table_n_field_names)
    
## bug fixed: if no fk_constraints, tail ',' remained
##    create_stat = 'CREATE TABLE {table_name} ({fields_def}, '\
##                  '{pk_constraint}, {fk_constraints});'\
##                  .format(table_name=table_name, fields_def=fields_def,
##                          pk_constraint=pk_constraint, fk_constraints=fk_constraints)

    defs = ', '.join([fields_def, pk_constraint] +fk_constraints)
    create_stat = 'CREATE TABLE {table_name} ({defs});'\
                  .format(table_name=table_name, defs=defs)
    return create_stat








import sqlite3
import ast
from make_create_stat_of_set import make_create_stat_of_set
from make_create_stat_of_composite_pk_set import make_create_stat_of_composite_pk_set
from make_create_stat_of_map import make_create_stat_of_map
from fill_table import fill_table, \
     fill_table_args_of_set, \
     fill_table_args_of_composite_pk_set, \
     fill_table_args_of_map, \
     show_table



con = sqlite3.connect(":memory:")
cur = con.cursor()
cursor = cur

set_field_name_ls = ['file_id', 'author_id', 'tag', 'file_format', 'media_type']
composite_pk_set_field_names_ls = [('author_id', 'file_id'), ('tag', 'file_id')]
map_info = [
    #('tag_n_super_tag_set', ['tag', 'super_tag'], 2, [('tag_set', ['tag', 'tag'])]),
    ('tag_n_super_tag_set', ['tag', 'super_tag'], 2, [
        ('tag_set', ['tag']),
        ('tag_set', ['tag']),
        ]),
    ('file_format2media_type', ['file_format', 'media_type'], 1, [
        ('file_format_set', ['file_format']),
        ('media_type_set', ['media_type'])
        ]),
    
    ]


create_stats = []
data_type = 'TEXT'
for field_name in set_field_name_ls:
    create_stats.append(make_create_stat_of_set(field_name, data_type))

data_types = ['TEXT'] * 2
for field_names in composite_pk_set_field_names_ls:
    create_stats.append(make_create_stat_of_composite_pk_set(field_names, data_types))

for table_name, field_names, num_pk_fields, foreign_table_n_field_names in map_info:
    data_types = ['TEXT'] * len(field_names)
    stat = make_create_stat_of_map(table_name, field_names, data_types,
                            num_pk_fields, foreign_table_n_field_names)
    create_stats.append(stat)


for i, create_stat in enumerate(create_stats):
    try:cur.execute(create_stat)
    except:
        print(i)
        print(create_stat)
        raise
    

#for stat in create_stats: print(stat)

###############

fill_table_args_ls = []

for field_name in set_field_name_ls:
    fill_table_args_ls.append(fill_table_args_of_set(field_name))


for field_names in composite_pk_set_field_names_ls:
    fill_table_args_ls.append(fill_table_args_of_composite_pk_set(field_names))

for table_name, field_names, num_pk_fields, foreign_table_n_field_names in map_info:
    fill_table_args_ls.append(fill_table_args_of_map(table_name, field_names))


for table_name, field_names, reader in fill_table_args_ls:
    for insert_stat, row in fill_table(table_name, field_names, reader):
        try:cursor.execute(insert_stat, row)
        except:
            print(insert_stat)
            print(row)
            raise


##for table_name, field_names, reader in fill_table_args_ls:
##    show_table(cursor, table_name, field_names)


stat = '''
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME, CONSTRAINT_NAME
    FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
    WHERE REFERENCED_TABLE_SCHEMA IS NOT NULL;'''

stat = '''
SELECT * FROM sqlite_master;'''
cur.execute(stat)
for row in cur.fetchall():
    print(row)







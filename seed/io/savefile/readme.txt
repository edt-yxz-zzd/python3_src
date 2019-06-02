
save_as use cases:
    * pprint a python object
        pprint(object)
    * increasingly save many objects, each per line
        f'{object!r}\n'
    * increasingly save many tuple of objects, each object per block, each object per line
        f'({object!r}\n'
        f',{object!r}\n'
        f')\n'
    * increasingly add key/value to a dict-in-file (key/"del"), key or value per line
        #new
        f'>{object!r}\n'
        f':{object!r}\n'
        f'.\n'

        #overwrite
        f'@{object!r}\n'
        f':{object!r}\n'
        f'.\n'

        #new or overwrite
        f'?{object!r}\n'
        f':{object!r}\n'
        f'.\n'

        #delete
        f'/{object!r}\n'
        f'.\n'
    * increasingly add element to a set-in-file, element per line
        #add
        f'>{object!r}\n'
        #remove
        f'/{object!r}\n'

other fields:
    * "--^^--^ nn_ns text Save File ^^--^^-\n"
    * "^^---^^ encoding = {encoding!r} --^^^--\n"
    ##* "{hash_method!r}"
    ##* "{physical_file_name!r}"
        physical_file_name = f"{logic_file_name}-{short_encoded_partial_args}-{hash(information,encoding)}-{collision_number}-{encoding}.{ext}"
        where
            '-' not in ext/logic_file_name/short_encoded_partial_args/hash/collision_number/encoding
    * information
        # ordered???? neednot
        # see: seed.helper.stable_repr
        # one dict span multiline, should not begin with '='
        {"file_type" : regex"(pprint single object|object per line|tuple per block|updatable dict|updatable set)"
        ,"logic_file_name" : f"logic_file_name!r}"
        ,"generator" : f"{program_name!r}"
        ,"args" : f"{args!r}"
        ,"kwargs" : f"{kwargs!r}"
        ,"description" : f"{description!r}"
        }\n
    * end-of-head
        "=====\n"


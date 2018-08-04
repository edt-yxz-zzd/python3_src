
def are_instances(iterable, types):
    # Types = type | tuple<Types...>
    return all(isinstance(obj, types) for obj in iterable)


from six import string_types

class DictInsensitive(dict):
    def __init__(self, *args, **kwargs):
        self.original = {}

        if len(args) == 1:
            mapping = args[0]

            if hasattr(mapping, 'keys') and hasattr(mapping, '__getitem__'):
                iterable = ((key, mapping[key]) for key in mapping)
            elif hasattr(mapping, '__iter__'):
                iterable = mapping
            else:
                raise TypeError("TypeError: '{}' object is not iterable".format(type(mapping)))
        elif len(args) > 1:
            raise TypeError('TypeError: dict expected at most 1 arguments, got {}'.format(len(args)))
        else:
            iterable = kwargs

        for key, value in iterable:
            self.__setitem__(key, value)

    def __getitem__(self, key):
        if isinstance(key, string_types):
            key = key.lower()
        return super(DictInsensitive, self).__getitem__(key)

    def __setitem__(self, key, value):
        if isinstance(key, string_types):
            self.original[key.lower()] = key
            key = key.lower()
        else:
            self.original[key] = key

        return super(DictInsensitive, self).__setitem__(key, value)

    def __delitem__(self, key):
        if isinstance(key, string_types):
            key = key.lower()
        return super(DictInsensitive, self).__delitem__(key)

    def __iter__(self):
        return iter(self.original.values())

    def keys(self):
        return self.original.values()

    def items(self):
        return [
            (self.original[key], value)
            for key, value in super(DictInsensitive, self).items()
        ]

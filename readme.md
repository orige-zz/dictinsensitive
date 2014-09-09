# Dict Insensitive
Before use this, try to refactor your code.
If you too lazy, use it!


# How To

Create a dictionary and instantiate a DictInsensitive for search, update and delete values with case insensitive keys:

```python
from dictinsensitive import DictInsensitive

normal_dict = {'movie': 'Star Wars', 'director': 'George Lucas'}
insensitive_dict = DictInsensitive(normal_dict)

normal_dict['Movie'] # will raises a KeyError exception
insensitive_dict['Movie'] # will print Star Wars

normal_dict['Movie'] # will raises a KeyError exception
insensitive_dict.get('Movie')

# You can do this too:
insensitive_dict = DictInsensitive({'movie': 'Star Wars'})

# Or:
insensitive_dict = DictInsensitive([('movie', 'Star Wars')])
```

Use DictInsentive like a normal **dict** with more chances to break something!

# TODO
- Create a pip package
- Improve tests

# License
MIT

# Collaborators
- Eduardo Orige (@orige)
- Augusto Hack (@hackaugusto)

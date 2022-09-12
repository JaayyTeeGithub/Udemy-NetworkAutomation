'''
1. Create a function called serialize() that takes 3 arguments: 1) the Python object you want to serialize, 2) the file
to which it serializes the object and 3) the serialization protocol which is pickle or json.

The function will create the file (the 2nd argument) and will write the Python object to that file according to its 3rd
argument. If the 3rd argument is pickle, It will use pickle to serialize the object and if the argument is json it will
use json for serialization.

2. Create a function called deserialize() that takes 2 arguments: 1) the file which contains serialized data and 2) the
type of deserialization which is pickle or json.

The function will deserialize from the file into a Python object and will return that object.

3. Test the functions by serializing and deserializing Python objects using both pickle and json.
'''


def serialize(obj, file, protocol):
    if protocol == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    elif protocol == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj, f)

    else:
        print('Use json or pickle. Duh.')


def deserialize(file, protocol):
    if protocol == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            result = pickle.load(f)
            return result

    elif protocol == 'json':
        import json
        with open(file, 'r') as f:
            result = json.load(f)
            return result
    else:
        print('Use json or pickle. Duh.')
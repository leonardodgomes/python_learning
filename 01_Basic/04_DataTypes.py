#Built-in Data Types
    #In programming, data type is an important concept.
    #Variables can store data of different types, and different types can do different things.

    #Python has the following data types built-in by default, in these categories:

        # Text Type:	str
        # Numeric Types:	int, float, complex
        # Sequence Types:	list, tuple, range
        # Mapping Type:	dict
        # Set Types:	set, frozenset
        # Boolean Type:	bool
        # Binary Types:	bytes, bytearray, memoryview


#You can get the data type of any object by using the type()
x = 5
name='Leonardo'
print(type (x))
print(type (name))


v_str = str("Hello World")	
v_int = int(20)
v_float = float(20.5)
v_complex = complex(1j)
v_list = list(("apple", "banana", "cherry"))
v_tuple = tuple(("apple", "banana", "cherry"))
v_range = range(6)
v_dict = dict(name="John", age=36)	
v_set = set(("apple", "banana", "cherry"))	
v_frozenset = frozenset(("apple", "banana", "cherry"))	
v_boll = bool(5)
v_bytes = bytes(5)
v_bytearray = bytearray(5)	
v_memoryview = memoryview(bytes(5))

print(v_str)
print(v_int)
print(v_float)
print(v_complex)
print(v_list)
print(v_tuple)
print(v_range)
print(v_dict)
print(v_set)
print(v_frozenset)
print(v_boll)
print(v_bytes)
print(v_bytearray)
print(v_memoryview)
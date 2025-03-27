def type_validation(variable, type_str):
    type_map = {
        "int": int,
        "float": float,
        "str": str,
        "bool": bool,
        "list": list,
        "tuple": tuple,
        "dict": dict,
        "set": set
    }
    
    return isinstance(variable, type_map.get(type_str, object))

print(type_validation(42, "int"))
print(type_validation("42", "int"))
print(type_validation(3.14, "float"))
print(type_validation(True, "bool"))
print(type_validation([], "list"))
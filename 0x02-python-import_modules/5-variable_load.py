#!/usr/bin/python3
import importlib.util

def import_variable(module_name, variable_name):
    spec = importlib.util.spec_from_file_location(module_name, module_name + ".py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)

if __name__ == "__main__":
    a = import_variable("variable_load_5", "a")
    print(a)


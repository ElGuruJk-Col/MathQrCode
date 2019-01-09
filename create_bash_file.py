import sys, inspect


file = str(input("Enter File Name:"))

with open(f"{file}.sh", "w") as f:
    f.write("")

with open(f"{file}.sh", "a+") as f:
    f.write("#!/usr/bin/env bash")
    for name, obj in inspect.getmembers(sys.modules[f"{file}.py"]):
        if inspect.isclass(obj):
            f.write(f"python3 extract_scene.py mean_squared_error.py {obj}")
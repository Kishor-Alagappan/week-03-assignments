# Intentionally cause a SyntaxError
try:
    eval("print('Hello, world!'")
except SyntaxError as e:
    print(f"SyntaxError: {e}")
else:
    print("No SyntaxError occurred.")

# Intentionally cause a NameError
try:
    print(variable_that_does_not_exist)
except NameError as e:
    print(f"NameError: {e}")
else:
    print("No NameError occurred.")

# Intentionally cause a ValueError
try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")
else:
    print("No ValueError occurred.")

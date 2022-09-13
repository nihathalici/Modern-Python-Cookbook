# Exer-10-Chaining-exceptions-with-the-raise-from-statement

class Error(Exception):
    pass

###

"""
try:
    something
except (IndexError, NameError) as exception:
    print("Expected", exception)
    raise Error("something went wrong") from exception
except Exception as exception:
    print("Unexpected", exception)
    raise
"""

class Error(Exception):
    pass
try:
    'hello world'[99]
except (IndexError, NameError) as exception:
    raise Error("index problem") from exception

"""
try:
    some_function()
except Exception as exception:
    print(exception)
    print(exception.__cause__)
"""

"""
try:
    something
except ValueError as exception:
    print("Some message", exceotuib)
"""
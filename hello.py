#! /usr/bin/env python
"""
When executed, it will print  Hello, world!  to the console. 

Python is a very flexible language, and it is possible to write code 
that is not structured in this way. However, in order to make your code 
more readable and maintainable, it is recommended to follow this structure. 

The  
```
if __name__ == "__main__": 
```
block is used to ensure that the  `main()` function is only executed when the 
script is run directly, and not when it is imported as a module in another script. 
 
This is important if you want to import your script into another script, 
or if you are writing a library that will be used by other scripts.
"""


def main():
    print("Hello, world!")


if __name__ == "__main__":
    main()

# AirBnB_clone #
###### AirBnB clone project for AlxSWE. ######

## Command Line Interpreter functionality ##
The command line interpreter should:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Execution ###
> Interactive Mode Functionality:
 $ ./console.py
 (hbnb) help

 Documented commands (type help <topic):
 ========================================
 EOF  help  quit

 (hbnb) 
 (hbnb) 
 (hbnb) quit
 $
>

> Non-interactive Mode Functionality:
> $ echo "help" | ./console.py
> (hbnb)
>
> Documented commands (type help <topic>):
> ========================================
> EOF  help  quit
> (hbnb) 
> $
> $ cat test_help
> help
> $
> $ cat test_help | ./console.py
> (hbnb)
>
> Documented commands (type help <topic>):
> ========================================
> EOF  help  quit
> (hbnb) 
> $

## Requirements ##
* Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
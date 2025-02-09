#Note: An error and an exception are just different words that describe the same thing when we are talking about exception handling.

# Common Exceptions:

"""
The most common built-in exceptions:

. Exception (This is what almost all the others are built off of)
. AttributeError - Raised when an attribute reference or assignment fails.
. IOError - Raised when an I/O operation (such as print statement, the built-in open() function or a method of a file object ) fails for an I/O-related reason, eg: "file not found" or "disk full" 
. ImportError - Raised whenn an import statement fails to find the module defination or when a from...import fails to find a name that is to be imported.
. IndexError - Raised when a sequence subscript is out of range.
. KeyError - Raised when a mapping (dictionary) key is not found in the set of existig keys.
. KeyboardInterrupt - Raised when the user hits the interrupt key (noramlly Contron + C or Delete) 
. NameError - Raised when a local or global name is not found.
. OSError - Riased when a function returns a system-related error.
. SyntaxError - Riased when the parser encounters a syntax error.
. TypeError - Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
. ValueError - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
.ZeroDivisionError - Riased when the second argument of a division or modulo opration is zero.


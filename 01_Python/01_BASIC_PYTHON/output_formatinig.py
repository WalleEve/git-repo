# Output Formatting
# The reprlib module provides a ersion of repr() customized for abbreviated display of alarge or deeply nested containers

import reprlib
set = reprlib.repr(set('supercalifragilisticexpialidocious'))
print("set:", set)



# pprint
"""
The pprint module offers more sophisticated control over printing both buit-in and user defined objects in a way that is readable by the interpreter. When the result is longer than one line, the "pretty printer" adds line breaks and indention to more clearly revel data structure:
"""
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']],[['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)
print(t)


# textwrap:
# The textwrap module formats paragraphs of text to fit a given screen width:

import textwrap

doc = """ The warp() method is just like fill() except that it 
returns a list of strings instead of one big string with newline to 
separate the wrapped lines."""

print(textwrap.fill(doc, width=40))


# locale 
# The locale module accesses a database of culture specific data format. The grouping attribute of locale's format function provides a direc way of formating numbers with group separetaors:

import locale
print(locale.setlocale(locale.LC_ALL, "English_United States.1252"))
conv =  locale.localeconv()
x = 1234567.8
print(locale.format_string("%d", x, grouping=True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))



# Templating:
"""
The string module includes a versatile Template calss with a simplified syntax suitable for aditing by end users. 
The format uses placeholde name formed by $ with valid Python identifiers (alphanumeric characters and underscores).
Surrounding the placeholder with braces allows it to be followed by more aplhanumeric letters with no interventig spaces. 
Writing $$ creates a single escaped $:
"""

from string import Template
t = Template('${village} folk send $$100 to $cause.')

print(t.substitute(village="Nottigham", cause="The ditch found"))


"""
The substitute() method raises a KeyError when a placeholder is not supplied in a dictionary or a keyword argument. For mail-merge style applications,
user supplied data may be imcomplete and the safe_substitute() method may be more appropriate It will leave placeholder inchanged if data is missing:
"""

t = Template("Return the $item to $owner.")
d = dict(item="unladen swallow")
#print(t.substitute(d))

print(t.safe_substitute(d))


 



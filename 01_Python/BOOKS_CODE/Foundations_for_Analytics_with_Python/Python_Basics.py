# Numbers 

# Integers 
x = 9 

print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))


# Floating-point numbers:

print("Output #7: {0:.3f}".format(8.3/2.7))

y = 2.5 * 4.8 
print("Output #8: {0:.1f}".format(y))

r = 8/float(3)
print("Output #9: {0:.2f}".format(r))

print("Output #10: {0:.4f}".format(8.0/3))


# Strings 

print("Output #14: {0:s}".format('I\'m enjoing learning Python.'))

print("Output #15: {0:s}".format("This is a long string. Wothout the backslash\
                                 it would run off of the page on the right in the text editor and by very\
                                 difiicult to read and edit. By using the backslash we can split the long\
                                 string into smaller strings on separate lines so that the whole string is easy\
                                 to view in the text editor. "))


print("Output #16: {0:s}".format('''We can use triple single quotes
                                 for milti-line comment strings.'''))

print("Output #17: {0:s}".format("""We can also use triple double quotes
                                 for multi-line comment strings."""))


string1 = "This is a "
string2 = "short string."
sentence = string1 + string2 
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s} {2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))


# Split 

string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(" ", 2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PICES: {0} SECOND PICES: {1} THIRTD PICES: {2}"\
      .format(string1_list2[0], string1_list2[1], string1_list2[2]))

string2 = "Your,deliverable,is,due,in,June"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))
print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[2],\
                                       string2_list[-1]))



# join 

print("Output #25: {0}".format(','.join(string2_list)))


# Strip 

string3 = " Remove unwanted characters   from this string.\t\t   \n"
print("Output #26: string3: {0:s}".format(string3))

string3_lstrip = string3.lstrip()
print("Output #27: lstrip: {0:s}".format(string3_lstrip))

string3_rstrip = string3.rstrip()
print("Output #28: rstrip: {0:s}".format(string3_rstrip))

string3_strip = string3.strip()
print("Output #29: strip: {0:s}".format(string3_strip))


string4 = "$$Here's another string that has unwanted characters.__----++"
print("Output #30: {0:s}".format(string4))

string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

string5 = "   $$The unwanted characters have been removed.__---++ \t\t \n"
print("Output #32: {0:s}".format(string5))
string5_strip = string5.strip('$_-+')
print("Output #33: {0:s}".format(string5_strip))

string6_strip = string5.strip().strip('$_-+')
print("Output #33: {0:s}".format(string6_strip))


# Replace 
string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))

string5_replace = string5.replace(" ", ',')
print("Output #33 (with commas): {0:s}".format(string5_replace))

string5_replace = string5.replace(" ", ',')
print("Output #33 (with commas): {0:s}".format(string5_replace))


# lower, upper, capilalize 

string6 = "Her's WHAT Happens WHEN we Use Lower."
print("Output #34: {0:s}".format(string6.lower()))
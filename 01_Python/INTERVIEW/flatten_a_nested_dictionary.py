# Flatten a Nested Dictionary 
# You are given a dictionary that may contain nested dictionaries. Write a function
# flattend_dict(d) that flattens it so that nested keys are combined in to a single key using a dot(.) as separator.

# Example:
#Input:
#{
#  "a": {
#    "b": {
#      "c": 1
#    }
#  },
#  "d": 2
#}
#
#Output:
#{
#  "a.b.c": 1,
#  "d": 2
#}



def flatten_dict(d, parent_key="", sep="."):
	
	items = {}
	
	for k, v in d.items():
		new_key = f"{parent_key} {sep}{k}" if parent_key else k 
		print(new_key)
		
		if isinstance(v, dict):
			items.update(flatten_dict(v, new_key, sep=sep))
		else:
			items[new_key] = v 
	return items 
	

nested_dict = {
    "a": {
        "b": {
            "c": 1
        }
    },
    "d": 2
}

flattened = flatten_dict(nested_dict)
print(flattened)

 

# for k, v in nested_dict.items():
# 	print(f"Key {k}, value: {v}")
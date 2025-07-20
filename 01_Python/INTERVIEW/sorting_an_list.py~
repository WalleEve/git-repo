insorted_list =  [2, 1, 5, 3, 7, 9, 8, 6, 4]


def sorted_list(inList):
	sorted_list = []
	for i in range(0, len(inList)):
		if len(sorted_list) == 0:
			sorted_list.append(inList[i])			
		else:
			for j in range(0, len(sorted_list)):
				if sorted_list[j] >= inList[i]:
					sorted_list.insert(j, inList[i])
					break
				else:
					if len(sorted_list)-1 == j:
						sorted_list.append(inList[i])
					else:
						continue 
	return sorted_list 
	
	

final_list = sorted_list(insorted_list)
print(final_list)
	
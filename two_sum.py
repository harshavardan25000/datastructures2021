def twoNumberSum(array, targetSum):
    # Write your code here.
	hashset=[]
	result=[]
	
	for num in array:
		
		if targetSum-num not in hashset:
			hashset.append(num)
		else:
			result=[targetSum-num,num]
			return result
			
	return result

assert twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9],17)==[8,9]

print("All Tests Passes")
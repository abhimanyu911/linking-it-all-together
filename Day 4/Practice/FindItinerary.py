'''Given a list of tickets, find itinerary in order using the given list.
Example: 
 

Input:
"Chennai" -> "Banglore"
"Bombay" -> "Delhi"
"Goa"    -> "Chennai"
"Delhi"  -> "Goa"

Output: 
Bombay->Delhi, Delhi->Goa, Goa->Chennai, Chennai->Banglore,'''

class Solution():

	def __init__(self):
		pass

	#method for printing iterary
	def findIterary(self,d):
		#create a reversed HashMap of the original HashMap 'd' 
		reverse_d = dict()
		for i in d:
			reverse_d[d[i]] = i
		#Find the starting point - Starting point will be that value which is not present in 'd' as a key.
		for i in reverse_d:
			if reverse_d[i] not in reverse_d:
				starting_pt = reverse_d[i]
				break;
		#Simply proceed one by one to print the entire route
		while(starting_pt in d):
			print(starting_pt,"->",d[starting_pt],end=", ")
			starting_pt = d[starting_pt]
		#method prints here only. Does not return anything.


if __name__=="__main__":

	# Mapping of from-to locations using inbuilt data structure 'dictionary'
	d = dict()
	d["Chennai"] = "Banglore"
	d["Bombay"] = "Delhi"
	d["Goa"] = "Chennai"
	d["Delhi"] = "Goa"

	obj = Solution()
	obj.findIterary(d)

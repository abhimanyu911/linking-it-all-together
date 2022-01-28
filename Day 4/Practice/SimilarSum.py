# Python Program to find four different elements a,b,c and d of
# array such that a+b = c+d

# function to find a, b, c, d such that
# (a + b) = (c + d)


def similarSum(arr = None):
	map = {}

	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
            #all possible sum combinations
			sum = arr[i] + arr[j]

            #if sum is present in Hash Table as a key, then print the prev values and current values
			if sum in map:
				print(f"{map[sum]} and ({arr[i]}, {arr[j]})")
				return
            #add sum to the map with array elements as values
			else:
				map[sum] = (arr[i], arr[j])


# Driver code
if __name__ == "__main__":
	arr = [3, 4, 7, 1, 2, 9, 8]
	similarSum(arr)

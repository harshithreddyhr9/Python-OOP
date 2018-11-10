# Time Complexity:O(n*2)
# Space complexity: O(1)
# Insertion sort takes maximum time to sort if elements are sorted in reverse order.
# And it takes minimum time (Order of n) when elements are already sorted.
def insertion_sort(nums):
    
	for i in range(len(nums)):
		
		j = i
		
		while j>0 and nums[j-1] > nums[j]:
			swap(nums,j,j-1)
			j = j - 1
	
	return nums
	
# To swap the numbers	
def swap(nums, i, j):
	temp = nums[i]
	nums[i] = nums[j]
	nums[j] = temp
 
if __name__ == "__main__":
   
   nums = [5,4,3,2,1]
   print(insertion_sort(nums))
  
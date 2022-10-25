# Question 1:
    
# Write a program that takes as input a sorted array of numbers. The objective is to return the array arranged in an
# alternate order such that max value is followed by min value in a descending fashion, so that the 1st element is the
# max value, 2nd element is the min value, 3rd element is the second max value, 4th element is the second min value &
# so on.
# Example: For an input array [2, 4, 6, 8, 10],
# the expected result would be [10, 2, 8, 4, 6]
# Note: The solution should modify the original array itself.

# Solution :

array = list(map(int, input().split()))

array.sort()
length = len(array)
mid = length//2 
arr1 = array[:mid]
arr2 = array[mid:]
arr2.sort(reverse=True)

arr = []
for i in range(max(len(arr1),len(arr2))) :
    try :
        arr.extend([arr2[i],arr1[i]])
    except :
        try :
            arr.append(arr2[i])
        except :
            arr.append(arr1[i])
print(arr)
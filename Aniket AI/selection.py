def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Get user input for the list of numbers
'''numbers = input("Enter a list of numbers (space-separated): ").split()
   numbers = [int(num) for num in numbers]
'''

n=int(input("enter total numbers to sort"))
sort=[]
for i in range(n):
    j=int(input("enter numbers one by one"))
    sort.append(j)
# Sort the numbers using selection sort
sorted = selection_sort(sort)

# Print the sorted numbers
print("Sorted numbers:", sorted)

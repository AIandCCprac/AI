def Selection_Sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]


n= int(input("enter total no of numbers"))
array=[]
for i in range(1,n+1){
    p=int(input("enter the numbers"))
    p.append(array)
}
Selection_Sort(array)
print("List after sorting is ")
print(array)
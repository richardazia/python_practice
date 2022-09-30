# Bubble sort

def bubbleSort(dataset):
    for i in range(len(dataset) -1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j + 1] = temp
        print("Current state: ", dataset)

def main():
    list = [20,24,13,12,65,4,3,2,7,9,12,17,5,4,33,23,12]
    bubbleSort(list)
    print("Result: ", list)

if __name__ == "__main__":
    main()

# Merge sort

merge_array = [4,3,6,7,8,12,90,2,5,45,23,16,8,32,18,42,38]

def mergesort(dataset):
    if len(dataset) > 1: # If it has one more than one element keep going.
        mid = len(dataset) // 2 # Floor Division (also called Integer Division)
        alpha_array = dataset[:mid]
        beta_array = dataset[mid:]

        # Call the function recursively
        mergesort(alpha_array)
        mergesort(beta_array)

        i = 0
        j = 0
        k = 0

        # Do this wilst both arrays are not empty
        while i < len(alpha_array) and j < len(beta_array):
            if alpha_array[i] < beta_array[j]:
                dataset[k] = alpha_array[i]
                i += 1
            else:
                dataset[k] = beta_array[j]
                j += 1
            k += 1
        # While alpha array is not empty
        while i < len(alpha_array):
            dataset[k] = alpha_array[i]
            i += 1
            k += 1
        # While beta array is not empty
        while j < len(beta_array):
            dataset[k] = beta_array[j]
            j += 1
            k += 1

print(merge_array)
mergesort(merge_array)
print(merge_array)

# Quicksort
print("Quicksort")
quicksort_array = [4,3,6,7,8,12,90,2,5,45,23,16,8,32,18,42,38]

def quickSort(dataset, first, last):
    if first < last:
        # Find the split point
        pivotIdx = partition(dataset, first, last)

        #Sort the two partitions
        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)

def partition(datavalues, first, last):
    # Choose the first pivot
    pivotvalue = datavalues[first]
    # Define the upper and lower indexes
    lower = first + 1
    upper = last

    # Start sorting the data
    done = False
    while not done:
        #Advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
        #Advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        #When the two indexes converge we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # Swap the pivot value when the split point is found
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point index
    return upper

print(quicksort_array)
quickSort(quicksort_array, 0, len(quicksort_array) -1 )
print(quicksort_array)

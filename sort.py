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
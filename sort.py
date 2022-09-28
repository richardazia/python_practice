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


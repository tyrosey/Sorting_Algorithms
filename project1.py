#
# CS 340 - Project 1 by Tyler Rose
#


# HeapSort function
def heapFunction():
       
        def heapify(array, size, index):    # initializing heapify function with root index and size of heap
                largest = index             # set largest to root index
                left = 2 * index + 1        # left
                right = 2 * index + 2       # right
                
                if right < size and array[largest] < array[right]:  # checking if right exists and is greater than root
                    largest = right                                 # set largest to right
                
                if left < size and array[largest] < array[left]:    # checking if left exists and is greater than root
                    largest = left                                  # set largest to left
                
                if largest != index:                                            # if largest does not equal index
                    array[index], array[largest] = array[largest], array[index] # switch
                    heapify(array, size, largest)                               # call heapify function 


        def heapSort(arr):                                          # let the sorting begin
                size = len(array)                                   # get the length of the array

                for index in range(size//2 - 1, -1, -1):            # initializing a max heap 
                    heapify(array, size, index)                     # calling heapify function

                for index in range(size-1, 0, -1):                  # reading out the content of the file
                    array[index], array[0] = array[0], array[index] # switch
                    heapify(array, index, 0)                        # calling heapify function


# outputting to text file
        array = []                                  # initialize array
        with open(fileName,'r') as file:            # open file
            for line in file:                       # for loop for each line in the file
                for word in line.split():           # for loop for each word of every line in the file
                        array.append(word)          # adds each word to the end of the array
        heapSort(array)                             # call heapSort for the array

        file1 = open(outputFile, 'w')               # create an output txt file
        size = len(array)                           # initialize array length

        for index in range(size):                   # for loop to go through entire heap for all index
                file1.write(array[index]+"\n")      # printing to file


# MergeSort Function
def mergeFunction():

        def mergeSort(array):
                if len(array) > 1:

                        center = len(array)//2                  # diving array by 2 to find center
                        left = array[:center]                   # assigning left side of array
                        right = array[center:]                  # assigning right side of array
                        mergeSort(left)                         # calling mergeSort function for left side
                        mergeSort(right)                        # calling mergeSort function for right side

                        indexLeft = indexRight = count = 0      # initializing index and count

                        while indexLeft < len(left) and indexRight < len(right):    # moving data to temp arrays
                                if left[indexLeft] < right[indexRight]:             # if left index is less than right
                                        array[count] = left[indexLeft]              # set left array
                                        indexLeft += 1                              # increment indexLeft
                                else:
                                        array[count] = right[indexRight]            # set right array
                                        indexRight += 1                             # increment indexRight
                                count += 1                                          # increment count

                        while indexLeft < len(left):                                # while loop checking all characters to left
                                array[count] = left[indexLeft]
                                indexLeft += 1
                                count += 1

                        while indexRight < len(right):                              # while loop checking all characters to right
                                array[count] = right[indexRight]
                                indexRight += 1
                                count += 1


# outputting to text file
        array = []                                  # initialize array
        with open(fileName,'r') as file:            # open file
            for line in file:                       # for loop for each line in the file
                for word in line.split():           # for loop for each word of every line in the file
                        array.append(word)          # adds each word to the end of the array
        mergeSort(array)                            # call mergeSort for the array

        file1 = open(outputFile, 'w')               # create an output txt file
        size = len(array)                           # initialize array length

        for index in range(size):                   # for loop to go through entire heap for all index
                file1.write(array[index]+"\n")      # printing to file


# Insertion Function
def insertionFunction():

        def insertionSort(array):                           # defining insertionSort function
                for index in range(1, len(array)):          # for loop checking through entire array
                    flag = array[index]                     # setting a flag
                    count = index - 1                       # checking through array
                
                    while count >= 0 and flag < array[count]:   # while loop for moving elements into new positions and checking/repeating
                            array[count + 1] = array[count]
                            count -= 1
                    array[count + 1] = flag


# outputting to text file
        array = []                                  # initialize array
        with open(fileName,'r') as file:            # open file
            for line in file:                       # for loop for each line in the file
                for word in line.split():           # for loop for each word of every line in the file
                        array.append(word)          # adds each word to the end of the array
        insertionSort(array)                        # call mergeSort for the array

        file1 = open(outputFile, 'w')               # create an output txt file
        size = len(array)                           # initialize array length

        for index in range(size):                   # for loop to go through entire heap for all index
                file1.write(array[index]+"\n")      # printing to file

# selecting methods and files

method = float(input("Select Sorting Method:\n1. HeapSort\n2. MergeSort\n3. InsertionSort\n\nYour Selection: ")) # recieving user input for method

# HEAPSORT
if method == 1:
        print("\nHeapSort Selected\n")
        # Recieving user input for files
        fileSelect = float(input("Select File Type:\n1.  perm15K.txt\n2.  perm30K.txt\n3.  perm45K.txt\n4.  perm60K.txt\n5.  perm75K.txt\n6.  perm90K.txt\n7.  perm105K.txt\n8.  perm120K.txt\n9.  perm135K.txt\n10. perm150K.txt\n\n11. sorted15K.txt\n12. sorted30K.txt\n13. sorted45K.txt\n14. sorted60K.txt\n15. sorted75K.txt\n16. sorted90K.txt\n17. sorted105K.txt\n18. sorted120K.txt\n19. sorted135K.txt\n20. sorted150K.txt\n\nYour Selection: ")) 
        
        if fileSelect == 1:
                
                print("\nperm15K.txt Selected\n")   # printing what file was selected
                fileName = ("perm15K.txt")          # setting file name to the file selected by the user
                outputFile = ("HS15K.txt")          # setting output file name in accordance to the selected file
                heapFunction()                      # calling heap function for the selected file
                
        if fileSelect == 2:

                print("\nperm30K.txt Selected\n")
                fileName = ("perm30K.txt")
                outputFile = ("HS30K.txt")
                heapFunction()
                
        if fileSelect == 3:
                
                print("\nperm45K.txt Selected\n")
                fileName = ("perm45K.txt")
                outputFile = ("HS45K.txt")
                heapFunction()
                
        if fileSelect == 4:

                print("\nperm60K.txt Selected\n")
                fileName = ("perm60K.txt")
                outputFile = ("HS60K.txt")
                heapFunction()        
                
        if fileSelect == 5:
                
                print("\nperm75K.txt Selected\n")
                fileName = ("perm75K.txt")
                outputFile = ("HS75K.txt")
                heapFunction()
                
        if fileSelect == 6:

                print("\nperm90K.txt Selected\n")
                fileName = ("perm90K.txt")
                outputFile = ("HS90K.txt")
                heapFunction()
                
        if fileSelect == 7:
                
                print("\nperm105K.txt Selected\n")
                fileName = ("perm105K.txt")
                outputFile = ("HS105K.txt")
                heapFunction()
                
        if fileSelect == 8:

                print("\nperm120K.txt Selected\n")
                fileName = ("perm120K.txt")
                outputFile = ("HS120K.txt")
                heapFunction()         
                
        if fileSelect == 9:
                
                print("\nperm135K.txt Selected\n")
                fileName = ("perm135K.txt")
                outputFile = ("HS135K.txt")
                heapFunction()
                
        if fileSelect == 10:

                print("\nperm150K.txt Selected\n")
                fileName = ("perm150K.txt")
                outputFile = ("HS150K.txt")
                heapFunction()
                
        if fileSelect == 11:
                
                print("\nsorted15K.txt Selected\n")
                fileName = ("sorted15K.txt")
                outputFile = ("HS15K.txt")
                heapFunction()
                
        if fileSelect == 12:

                print("\nsorted30K.txt Selected\n")
                fileName = ("sorted30K.txt")
                outputFile = ("HS30K.txt")
                heapFunction()        
                
        if fileSelect == 13:
                
                print("\nsorted45K.txt Selected\n")
                fileName = ("sorted45K.txt")
                outputFile = ("HS45K.txt")
                heapFunction()
                
        if fileSelect == 14:

                print("\nsorted60K.txt Selected\n")
                fileName = ("sorted60K.txt")
                outputFile = ("HS60K.txt")
                heapFunction()
                
        if fileSelect == 15:
                
                print("\nsorted75K.txt Selected\n")
                fileName = ("sorted75K.txt")
                outputFile = ("HS75K.txt")
                heapFunction()
                
        if fileSelect == 16:

                print("\nsorted90K.txt Selected\n")
                fileName = ("sorted90K.txt")
                outputFile = ("HS90K.txt")
                heapFunction()         
                
        if fileSelect == 17:
                
                print("\nsorted105K.txt Selected\n")
                fileName = ("sorted105K.txt")
                outputFile = ("HS105K.txt")
                heapFunction()
                
        if fileSelect == 18:

                print("\nsorted120K.txt Selected\n")
                fileName = ("sorted120K.txt")
                outputFile = ("HS120K.txt")
                heapFunction()
                
        if fileSelect == 19:
                
                print("\nsorted135K.txt Selected\n")
                fileName = ("sorted135K.txt")
                outputFile = ("HS135K.txt")
                heapFunction()
                
        if fileSelect == 20:

                print("\nsorted150K.txt Selected\n")
                fileName = ("sorted150K.txt")
                outputFile = ("HS150K.txt")
                heapFunction()         
                
# MERGESORT
if method == 2:
        print("\nMergeSort Selected\n")
        fileSelect = float(input("Select File Type:\n1.  perm15K.txt\n2.  perm30K.txt\n3.  perm45K.txt\n4.  perm60K.txt\n5.  perm75K.txt\n6.  perm90K.txt\n7.  perm105K.txt\n8.  perm120K.txt\n9.  perm135K.txt\n10. perm150K.txt\n\n11. sorted15K.txt\n12. sorted30K.txt\n13. sorted45K.txt\n14. sorted60K.txt\n15. sorted75K.txt\n16. sorted90K.txt\n17. sorted105K.txt\n18. sorted120K.txt\n19. sorted135K.txt\n20. sorted150K.txt\n\nYour Selection: ")) 
        
        if fileSelect == 1:
                
                print("\nperm15K.txt Selected\n")
                fileName = ("perm15K.txt")
                outputFile = ("MS15K.txt")
                mergeFunction()
                
        if fileSelect == 2:

                print("\nperm30K.txt Selected\n")
                fileName = ("perm30K.txt")
                outputFile = ("MS30K.txt")
                mergeFunction()
                
        if fileSelect == 3:
                
                print("\nperm45K.txt Selected\n")
                fileName = ("perm45K.txt")
                outputFile = ("MS45K.txt")
                mergeFunction()
                
        if fileSelect == 4:

                print("\nperm60K.txt Selected\n")
                fileName = ("perm60K.txt")
                outputFile = ("MS60K.txt")
                mergeFunction()        
                
        if fileSelect == 5:
                
                print("\nperm75K.txt Selected\n")
                fileName = ("perm75K.txt")
                outputFile = ("MS75K.txt")
                mergeFunction()
                
        if fileSelect == 6:

                print("\nperm90K.txt Selected\n")
                fileName = ("perm90K.txt")
                outputFile = ("MS90K.txt")
                mergeFunction()
                
        if fileSelect == 7:
                
                print("\nperm105K.txt Selected\n")
                fileName = ("perm105K.txt")
                outputFile = ("MS105K.txt")
                mergeFunction()
                
        if fileSelect == 8:

                print("\nperm120K.txt Selected\n")
                fileName = ("perm120K.txt")
                outputFile = ("MS120K.txt")
                mergeFunction()         
                
        if fileSelect == 9:
                
                print("\nperm135K.txt Selected\n")
                fileName = ("perm135K.txt")
                outputFile = ("MS135K.txt")
                mergeFunction()
                
        if fileSelect == 10:

                print("\nperm150K.txt Selected\n")
                fileName = ("perm150K.txt")
                outputFile = ("MS150K.txt")
                mergeFunction()
                
        if fileSelect == 11:
                
                print("\nsorted15K.txt Selected\n")
                fileName = ("sorted15K.txt")
                outputFile = ("MS15K.txt")
                mergeFunction()
                
        if fileSelect == 12:

                print("\nsorted30K.txt Selected\n")
                fileName = ("sorted30K.txt")
                outputFile = ("MS30K.txt")
                mergeFunction()        
                
        if fileSelect == 13:
                
                print("\nsorted45K.txt Selected\n")
                fileName = ("sorted45K.txt")
                outputFile = ("MS45K.txt")
                mergeFunction()
                
        if fileSelect == 14:

                print("\nsorted60K.txt Selected\n")
                fileName = ("sorted60K.txt")
                outputFile = ("MS60K.txt")
                mergeFunction()
                
        if fileSelect == 15:
                
                print("\nsorted75K.txt Selected\n")
                fileName = ("sorted75K.txt")
                outputFile = ("MS75K.txt")
                mergeFunction()
                
        if fileSelect == 16:

                print("\nsorted90K.txt Selected\n")
                fileName = ("sorted90K.txt")
                outputFile = ("MS90K.txt")
                mergeFunction()         
                
        if fileSelect == 17:
                
                print("\nsorted105K.txt Selected\n")
                fileName = ("sorted105K.txt")
                outputFile = ("MS105K.txt")
                mergeFunction()
                
        if fileSelect == 18:

                print("\nsorted120K.txt Selected\n")
                fileName = ("sorted120K.txt")
                outputFile = ("MS120K.txt")
                mergeFunction()
                
        if fileSelect == 19:
                
                print("\nsorted135K.txt Selected\n")
                fileName = ("sorted135K.txt")
                outputFile = ("MS135K.txt")
                mergeFunction()
                
        if fileSelect == 20:

                print("\nsorted150K.txt Selected\n")
                fileName = ("sorted150K.txt")
                outputFile = ("MS150K.txt")
                mergeFunction()         

# INSERTIONSORT
if method == 3:
        print("\nInsertionSort Selected\n")
        fileSelect = float(input("Select File Type:\n1.  perm15K.txt\n2.  perm30K.txt\n3.  perm45K.txt\n4.  perm60K.txt\n5.  perm75K.txt\n6.  perm90K.txt\n7.  perm105K.txt\n8.  perm120K.txt\n9.  perm135K.txt\n10. perm150K.txt\n\n11. sorted15K.txt\n12. sorted30K.txt\n13. sorted45K.txt\n14. sorted60K.txt\n15. sorted75K.txt\n16. sorted90K.txt\n17. sorted105K.txt\n18. sorted120K.txt\n19. sorted135K.txt\n20. sorted150K.txt\n\nYour Selection: ")) 
        
        if fileSelect == 1:
                
                print("\nperm15K.txt Selected\n")
                fileName = ("perm15K.txt")
                outputFile = ("IS15K.txt")
                insertionFunction()
                
        if fileSelect == 2:

                print("\nperm30K.txt Selected\n")
                fileName = ("perm30K.txt")
                outputFile = ("IS30K.txt")
                insertionFunction()
                
        if fileSelect == 3:
                
                print("\nperm45K.txt Selected\n")
                fileName = ("perm45K.txt")
                outputFile = ("IS45K.txt")
                insertionFunction()
                
        if fileSelect == 4:

                print("\nperm60K.txt Selected\n")
                fileName = ("perm60K.txt")
                outputFile = ("IS60K.txt")
                insertionFunction()        
                
        if fileSelect == 5:
                
                print("\nperm75K.txt Selected\n")
                fileName = ("perm75K.txt")
                outputFile = ("IS75K.txt")
                insertionFunction()
                
        if fileSelect == 6:

                print("\nperm90K.txt Selected\n")
                fileName = ("perm90K.txt")
                outputFile = ("IS90K.txt")
                insertionFunction()
                
        if fileSelect == 7:
                
                print("\nperm105K.txt Selected\n")
                fileName = ("perm105K.txt")
                outputFile = ("IS105K.txt")
                insertionFunction()
                
        if fileSelect == 8:

                print("\nperm120K.txt Selected\n")
                fileName = ("perm120K.txt")
                outputFile = ("IS120K.txt")
                insertionFunction()         
                
        if fileSelect == 9:
                
                print("\nperm135K.txt Selected\n")
                fileName = ("perm135K.txt")
                outputFile = ("IS135K.txt")
                insertionFunction()
                
        if fileSelect == 10:

                print("\nperm150K.txt Selected\n")
                fileName = ("perm150K.txt")
                outputFile = ("IS150K.txt")
                insertionFunction()
                
        if fileSelect == 11:
                
                print("\nsorted15K.txt Selected\n")
                fileName = ("sorted15K.txt")
                outputFile = ("IS15K.txt")
                insertionFunction()
                
        if fileSelect == 12:

                print("\nsorted30K.txt Selected\n")
                fileName = ("sorted30K.txt")
                outputFile = ("IS30K.txt")
                insertionFunction()        
                
        if fileSelect == 13:
                
                print("\nsorted45K.txt Selected\n")
                fileName = ("sorted45K.txt")
                outputFile = ("IS45K.txt")
                insertionFunction()
                
        if fileSelect == 14:

                print("\nsorted60K.txt Selected\n")
                fileName = ("sorted60K.txt")
                outputFile = ("IS60K.txt")
                insertionFunction()
                
        if fileSelect == 15:
                
                print("\nsorted75K.txt Selected\n")
                fileName = ("sorted75K.txt")
                outputFile = ("IS75K.txt")
                insertionFunction()
                
        if fileSelect == 16:

                print("\nsorted90K.txt Selected\n")
                fileName = ("sorted90K.txt")
                outputFile = ("IS90K.txt")
                insertionFunction()         
                
        if fileSelect == 17:
                
                print("\nsorted105K.txt Selected\n")
                fileName = ("sorted105K.txt")
                outputFile = ("IS105K.txt")
                insertionFunction()
                
        if fileSelect == 18:

                print("\nsorted120K.txt Selected\n")
                fileName = ("sorted120K.txt")
                outputFile = ("IS120K.txt")
                insertionFunction()
                
        if fileSelect == 19:
                
                print("\nsorted135K.txt Selected\n")
                fileName = ("sorted135K.txt")
                outputFile = ("IS135K.txt")
                insertionFunction()
                
        if fileSelect == 20:

                print("\nsorted150K.txt Selected\n")
                fileName = ("sorted150K.txt")
                outputFile = ("IS150K.txt")
                insertionFunction()         

print("Sorting Complete!\n")    # message to let user know sorting is complete 
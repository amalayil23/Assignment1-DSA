#Importing Library for sound effect
from playsound import playsound

#Defining function merge sort
def MergeSort(array):
    #Checking if the array is is greater than 1
    if len(array) > 1:
        mid = len(array)//2 #Finding the middle of the array. 
        #Splitting the elements into 2 arrays.
        left = array[:mid] 
        right = array[mid:]
        print(left,"  ",right)


        # Recursively sort both halves. 
        MergeSort(left)
        MergeSort(right)
        

        # Merge the 2 halves. 
        print("Merging", left ," + ", right )
        i = j = k = 0
        while i < len(left) and j < len(right):
            #Comparing elements of left array to the right array. 
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                try:
                    playsound('C:\\Users\\malay\\swoosh.wav')
                except:
                    print("Couldn't play sound.. Swapping")
                    continue
                array[k] = right[j]
                j += 1
            k += 1

        # Merging remaining elements
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

        


test_array = [38, 27, 43, 3, 9, 82, 10,28,2,90,67,98,15,71]
MergeSort(test_array)
print("\nSorted array:", test_array)
exit  =  input("Press enter to exit... ")


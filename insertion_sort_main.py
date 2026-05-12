import insertion_sort as i
import sys

numbers = []
for x in range(1,len(sys.argv)):
    
    numbers.append(float(sys.argv[x]))

i.insertion_sort(numbers,x)

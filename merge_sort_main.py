import merge_sort as ms 
import sys

numbers = []
for x in range(1,len(sys.argv)):
    
    numbers.append(float(sys.argv[x]))
r=ms.merge_sort(numbers)
print(r)
import selection_sort as s
import sys
numbers = []
for i in range(1 , len(sys.argv)):
    numbers.append(int(sys.argv[i]))
s.selection_sort(numbers , i)
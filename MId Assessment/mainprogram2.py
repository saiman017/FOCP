import math
month = ['January','February','March','April','May','june','July','August','September','October','November','December']
values = [int(input("Enter rainfall for "+str(i))) for i in month]
maxmonth = values.index(max(values))
minmonth = values.index(min(values))
print(f"Max rainfall: {max(values)}mm in {month[maxmonth]}.")
print(f"Min rainfall: {min(values)}mm in {month[minmonth]}." )
total = 0
for i in values:
    total += i
average = total/len(values)
print(f"Average: {average:.2f}mm")
import statistics
print(f"Standard deviation: {statistics.stdev(values):.1f}mm")
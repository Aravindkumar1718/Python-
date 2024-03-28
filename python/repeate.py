arr=[1,2,1,2,3,4,1,1,1,1,2,1,1]
counter = 0
num = arr[0]   
for i in arr:
    curr_frequency = arr.count(i)
    if(curr_frequency> counter):
        counter = curr_frequency
        num = i
print(num,end="-")
print(counter)




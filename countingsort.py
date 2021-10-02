arr = [int(i) for i in input("Enter the list: ").split()] #taking the inputs
max = 0   
min = 0
for i in arr:  # findind maimum and the minimum values
    if i>max:
        max = i
    elif i<min:
        min = i
control = []
for i in range(0,(max-min)+1): # allocating a array 'control' of size (max-min)+1  and all the elements are zero
    control.append(0)
for i in arr:           # counting the array elemnts by using min right shifted values of them to find index of control
    control[i-min]=control[i-min]+1
j=0   #j will run through indicies of array
for i in range(0,(max-min)+1): # i runs thorough indices of control 
    while(control[i]!=0):   
        arr[j]=i+min      # replacing array j value with 'i+min' the correct value
        control[i]=control[i]-1
        j = j+1

print(arr)

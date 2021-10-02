# priority Queue using minheap here highest priority given to lowest value

class minheap:  #creating minheap class
    pq=list()   #heap array
    def __init__(self,arr=list()): #constructor function
        if(len(arr)==0):
            for i in input("Enter the enements for priority queue:").split():
                self.add(int(i))
        else:
            for i in arr:
                self.add(int(i))
    def swap(self,x,y):   # A swap function
        c=self.pq[x]
        self.pq[x]=self.pq[y]
        self.pq[y]=c
    def minheapify(self,i): # function to maintain the heap from top to down complexity O(logn)
        p = self.pq
        l = 2*i+1
        r = 2*i+2
        smallest = i
        if (l<len(p) and p[l]<p[i]):
            smallest = l
        if (r<len(p) and p[r]<p[smallest]):
            smallest = r
        if smallest != i :
            self.swap(smallest,i)
            self.minheapify(smallest)
    def printheap(self):  #displaying heap function in array form
        print(self.pq)
    def add(self,k): # Adding an element to heap complexity O(logn)
        i = len(self.pq)
        self.pq.append(k)
        while(i!=0 and self.pq[int(i/2)]>k ):  
            self.swap(i,int(i/2))
            i = int(i/2)
    def peek(self):  # peek the highest priority element complexity O(1)
        if(len(self.pq)==0):
            print("The priority queue is uderflow")
            return
        return self.pq[0]
    def remove(self): # Remove the highest priority element complexity O(logn)
        if(len(self.pq)==0):
            print("The priority queue is uderflow")
            return
        self.swap(0,len(self.pq)-1)
        c=self.pq.pop()
        self.minheapify(0)  # heap maintain complexity O(logn)
        return c
# The running body
a = minheap([20,-1,2,3,67,100,50]) # creating an object of class minheap
print("The given priority queue")
a.printheap()
while(True): # Program Running while loop 
    print("Choose any of the following the opperation:")
    print("1.To display the priority queue ")
    print("2. To add an element to queue ")
    print("3.To peek the highest priority element")
    print("4.To remove the highest prority element")
    print("5. To exit\n\n")
    t=int(input("Enter Here: "))
    if(t==1):
        a.printheap()
    elif(t==2):
        k=int(input("Enter the element to be enter: "))
        a.add(k)
    elif(t==3):
        print("The highest priority element is: ",a.peek())
    elif(t==4):
        print("Removed highest priority element is: ",a.remove())
    elif(t==5):
        print("Exiting the program.")
        break
    else:
        print("Invalid input.Please try again.")
    print("\n\n")
    
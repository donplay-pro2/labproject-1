class minheap:  #creating minheap class
    pq=list()   #heap array
    def swap(self,x,y):   # A swap function
        c=self.pq[x]
        self.pq[x]=self.pq[y]
        self.pq[y]=c
    def minheapify(self,i): # function to maintain the heap from top to down complexity O(logn)
        l = 2*i+1  #Left child
        r = 2*i+2  #Right child
        smallest = i
        if (l<len(self.pq) and self.pq[l][0]<self.pq[i][0]):
            smallest = l
        if (r<len(self.pq) and self.pq[r][0]<self.pq[smallest][0]):
            smallest = r
        if smallest != i :
            self.swap(smallest,i)
            self.minheapify(smallest)
    def add(self,d,x): # Adding an element to heap complexity O(logn)
        i = len(self.pq)
        self.pq.append([d,x])
        while(i!=0 and self.pq[int(i/2)][0]>d ):  
            self.swap(i,int(i/2))
            i = int(i/2)
    def remove(self): # Remove the highest priority element complexity O(logn)
        if(len(self.pq)==0):
            print("The priority queue is uderflow")
            return
        self.swap(0,len(self.pq)-1)
        c=self.pq.pop()
        self.minheapify(0)  # heap maintain complexity O(logn)
        return c[1]
    def empty(self):
        if len(self.pq)==0:
            return True
        return False
    def size(self):
      return len(self.pq)
class graph: #Graph Class
    n = int(input("Enter the number of nodes: ")) # Total number of nodes
    adjecencylist = [[] for i in range(0,n)]  #initial Adjency list
    q=minheap() # The priority queue
    distance=[float('inf') for i in range(0,n)] #initializing each node distance to infinity
    processed = [False for i in range(0,n)] # Processed of each node is false
    parent = [-1 for i in range(0,n)]
    def creategraph(self):  #Creation of Graph Time complexity O(m) where m = no. of edge
        m = int(input("Enter the number of node pair: "))
        print("Enter the node pairs and distance between them : ")
        for i in range(0,m):
            k,l,m=[int(i) for i in input().split()] #taking inputs k->l with distance m
            self.addgraph(k, l,m)
    def addgraph(self,x,y,z): # Adding elemnts in adjency list
        self.adjecencylist[x-1].append([y-1,z])
        #self.adjecencylist[y-1].append([x-1,z])
    def relax(self,a):
        for i in self.adjecencylist[a]: # realxing 
                b = i[0] # Adjecent nodes
                d = i[1] # distance between the adjecent nodes
                if(self.distance[a]+d < self.distance[b]): # Relaxing formula
                    self.distance[b]=self.distance[a]+d
                    self.q.add(self.distance[b], b)
                    self.parent[b]=a
    def dijkstrashortestpath(self,x): 
        self.distance[x-1]=0 # distance ofinitial node is 0
        self.q.add(0, x-1) # Add this to priority queue
        while(self.q.size()>0):
            a=self.q.remove()
            if(self.processed[a]):
                continue
            self.processed[a] = True # node A is processed
            self.relax(a) # realxing the adjecent nodes
        print("Vertices    Distance     Parent")
        for i in range(0,self.n):
          print("  ",i+1,"       ",self.distance[i],"           ",self.parent[i]+1)
        print("The path for each vertices: ")
        print("Vertices        Path ")
        for i in range(0,self.n):
          temp = []
          v=i
          temp.append(i)
          while v != 0:
            b = self.parent[v]
            temp.append(b)
            v = self.parent[v]
          temp.reverse()
          temp = [t+1 for t in temp]
          print("  ",i+1,"            ",end="")
          print(*temp,sep="-->")
g = graph()
g.creategraph()
x = int(input("Enter the node from where the distance to be calculated: "))
print("Shortest path between ",x," other nodes: ")
print(g.dijkstrashortestpath(x))
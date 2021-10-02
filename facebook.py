class graph: #Graph Class
    n = int(input("Enter the total number of people: ")) # Total number of people
    adjecencylist = [[] for i in range(1,n+1)]  #initial Adjency list
    def creategraph(self):  #Creation of Graph Time complexity O(m) where m = no. of edge
        m = int(input("Enter the number of friend pair: "))
        print("Enter the friend pairs: ")
        for i in range(0,m):
            k,l=[int(_) for _ in input().split()]
            self.addgraph(k, l)
    def addgraph(self,x,y): # Adding elemnts in adjency list
        self.adjecencylist[x-1].append(y-1)
        self.adjecencylist[y-1].append(x-1)
    def bfs(self,x): # The bfs Time complexity O(m+n)
        q = list()
        visited = [False for i in range(0,self.n)]
        distance = [0 for i in range(0,self.n)]
        visited[x]=True
        distance[x]=0
        q.append(x)
        while(len(q)!=0):
            s=q.pop(0)
            for u in self.adjecencylist[s]:
                if(visited[u]==True):
                    continue
                visited[u] = True
                distance[u] = distance[s] + 1
                q.append(u)
        return distance
    def recomendedfriend(self): # The recomended list complexity O(m+n)
        recomended = list()
        x = int(input("Enter the person to be recomended: "))
        distance = self.bfs(x-1)
        for i in range(0,len(distance)):
            if(distance[i]>=2):
                recomended.append(i+1)
        print("The recomended List : ",recomended)
g = graph()
g.creategraph()
g.recomendedfriend()

import collections
from enum import Enum

class Cherry():
    def __init__(self):
        self.neighbor = []
        self.visited = Visit.No

class Visit(Enum):
    No = 0
    In = 1
    Yes = 2




T = int(input())


for t in range(T):
    N, M = map(int, input().split())
    #print('N: %d, M: %d' %(N, M))
    table = {}
    for i in range(M):
        Ci, Di = map(int, input().split())
        if Ci not in table:
            table[Ci] = Cherry()
        if Di not in table:
            table[Di] = Cherry()
        table[Ci].neighbor.append(Di)
        table[Di].neighbor.append(Ci)

    cnt = 0
    q = collections.deque()

    for i in range(1,N+1):
        if i not in table:
            cnt += 2
        elif table[i].visited == Visit.No:
            table[i].visited = Visit.Yes
            cnt+=2
            
            q.append(i)
            
            while q:
                cur = q.popleft()
                table[cur].visited = Visit.Yes
                for nei in table[cur].neighbor:
                    if table[nei].visited == Visit.No:
                        q.append(nei)
                        table[nei].visited = Visit.In
                        cnt += 1
        else:
            continue



    cnt -=2 # no need for starting point
    print('Case #%d: %d'%(t+1, cnt))


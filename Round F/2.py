import numpy as np
import collections


T = int(input())


for t in range(T):
    N,S = [int(s) for s in input().split(" ")]
    skill = []
    have = {}
    for i in range(N):
        arr = [int(s) for s in input().split(" ")]
        skill.append(np.zeros(arr[0],dtype='int'))
        for j in range(arr[0]):
            skill[i][j] = arr[j+1]
        skill[i].sort()
        skill[i] = tuple(skill[i])
        if skill[i] in have:
            have[skill[i]]+=1
        else:
            have[skill[i]] = 1

    cnt = N * (N-1)
    for i in range(N):
        for j in range(len(skill[i])):
            for k in range(j+1,len(skill[i])+1):
                if skill[i][j:k] in have:
                    cnt -= have[skill[i][j:k]]
                print(j,k, skill[i][j:k])
        cnt+=1
        


    print('Case #%d: %d'%(t+1, cnt))


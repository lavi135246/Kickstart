
T = int(input())

for t in range(T):
    D, S = map(int, input().split())
    slot_dict = {}
    frac = []
    for s in range(S):
        C, E = map(int, input().split())
        slot_dict[s] = C/E
        frac.append((C,E))

    slot_dict = sorted(slot_dict.items(), key=lambda d: d[1])

    #print(slot_dict)

    result = ''
    for d in range(D):
        A, B = map(int, input().split())
        for k, v in slot_dict:
            C, E = frac[k]
            if B > 0:
                if B >= E:
                    B-=E
                else:
                    remain = (E-B)/E
                    A -= remain*C
                    B = 0
                    
            
            elif A > 0:
                A-=C

            else:
                break

        if A<=0 and B <= 0:
            result+='Y'
        else:
            result+='N'

    print('Case #%d: %s'%(t+1, result))


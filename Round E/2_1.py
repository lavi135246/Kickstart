import bisect
import numpy as np

T = int(input())

for t in range(T):
    D, S = map(int, input().split())
    slot_dict = {}
    frac = []
    for s in range(S):
        C, E = [int(s) for s in input().split(" ")]
        slot_dict[s] = E/C
        frac.append((C,E))

    slot_dict = sorted(slot_dict.items(), key=lambda d: d[1])
    code_sum = np.zeros(S)
    eat_sum = np.zeros(S)

    for i, kv in enumerate(slot_dict):
        C, E = frac[kv[0]]
        code_sum[i] = C
        eat_sum[i] = E

    for i in range(1, S):
        code_sum[i] += code_sum[i-1]
        eat_sum[S-i-1] += eat_sum[S-i]

    result = ''
    for d in range(D):
        A, B = [int(s) for s in input().split(" ")]
        if A > code_sum[-1] or B > eat_sum[0]:
            result += 'N'
            continue

        i = bisect.bisect_left(code_sum, A)

        if i-1>=0:
            A = A-code_sum[i-1]
            remain = 1 - A/(code_sum[i]-code_sum[i-1])
        else:
            remain = 1 - A/code_sum[i]
        # print(remain, i)
        if i+1<S:
            B -= eat_sum[i+1]
            B -= remain*(eat_sum[i]-eat_sum[i+1])

        else:
            B -= remain*eat_sum[i]

        if B<=0:
            result+='Y'
        else:
            result+='N'


    print('Case #%d: %s'%(t+1, result))


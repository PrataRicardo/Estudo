while True:
    try:
        N = int(input())
        if (N == 0):
            break
        
        P = list(map(int, input().split(' ')))
        picos = 0


        for i in range(0, N):
            prev = P[(i - 1) % N]
            nxt = P[(i + 1) % N]

            if (P[i] > prev and P[i] > nxt) or (P[i] < prev and P[i] < nxt):
                
                picos += 1

        print(f"{picos}")
    
    except EOFError:
        break
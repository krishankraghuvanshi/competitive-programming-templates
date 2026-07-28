
N = len(s)
#longest same character substring
def solver1():
    current = s[0]
    streak = 1
    best = 1
    for i in range(1, N):
        if s[i] == current:
            streak += 1
        else:
            best = max(best, streak)
            current = s[i]
            streak = 1
    best = max(best, streak)        
    return best   

#this part I keep forget 

#compute longest substring where x and y are equal in number x, y can be (a, b, c)
def solver2(x, y):
    f = Counter()
    cur = 0
    best = 0
    f[0] = -1
    for i in range(N):
        if s[i] == x:
            cur += 1
        elif s[i] == y:
            cur -= 1
        else:
            cur = 0
            f.clear()
            f[0] = i
        if cur in f:
            best = max(best, i-f[cur])   
        else:    
            f[cur] = i 
    return best    
#compute longest substring where a, b, c are in equal numbers    
def solver3():
    a, b, c = 0, 0, 0
    current = 0
    f = Counter()
    f[(0, 0, 0)] = -1
    best = 0
    for i in range(len(s)):
        if s[i] == 'a':
            a += 1
            c += 1
        elif s[i] == 'b':
            a -= 1
            b += 1
        else:
            b -= 1
            c -= 1
        if (a, b, c) in f:
            best = max(best, i-f[(a, b, c)])
        else:
            f[(a, b, c)] = i  
    return best              



def manacher(s):
    t = "^#"+"#".join(s)+"#$"

    center = right = 0

    max_length, max_center = 0, 0


    p = [0]*len(t)


    for i in range(1, len(t)-1):

        mirror = 2*center - i

        if i < right:
            p[i] = min(p[i], right-i)

        while t[i - (1+p[i])] == t[i + (1+p[i])]:
            p[i]+=1

        if i + p[i] > right:
            center = i
            right = i+p[i]

        if p[i] > max_length:
            max_length = p[i]
            max_center  = i

    start = (max_center - max_length)//2

    return s[start:start+max_length]                   


        

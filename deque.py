mxQ = deque()
mnQ = deque() 

left =  0

for right in range(n):
    while len(mxQ) and mxQ[-1][0] < nums[right]:
        mxQ.pop()
    mxQ.append((nums[right], right))
    while len(mnQ) and mnQ[-1][0] > nums[right]:
        mnQ.pop() 
    mnQ.append((nums[right], right))

    while len(mxQ) and len(mnQ) and mxQ[0][0] - mnQ[0][0] > k:
        if mxQ[0][1] == left:
            mxQ.popleft()
        if mnQ[0][1] == left:
            mnQ.popleft()
        remove(prefix_xor[left])
        left = left + 1
    
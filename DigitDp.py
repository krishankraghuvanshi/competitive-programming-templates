MOD = int(1e9)+7
@cache
def f(s, i, tight, started, ....):
    if i == len(s):
        return 1 if started else 0
    res = 0

    if not started:
        res = (res + f(s, i+1, 0, started, ....)) % MOD

    lb, ub = 0 if started else 1, int(s[i]) if tight else 9

    for digit in range(lb, ub+1):

        if SOME_CONDITION:
            ntight = 1 if digit == ub and tight else 0

            res = (res + f(s, i+1, ntight, 1, ....)) % MOD
    return res
# calls f as per the requirements

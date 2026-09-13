MAX = 100000

evens = []
odds = []

# x x
# x y x
# 9999 9 9999
for i in range(1, MAX):
    left = str(i)
    right = left[::-1]

    current = int(left + right)

    if current % 2 == 0:
        evens.append(current)
    else:
        odds.append(current)

    right = left[:-1][::-1]
    current = int(left + right)

    if current % 2 == 0:
        evens.append(current)
    else:
        odds.append(current)

evens = list(sorted(set(evens)))
odds = list(sorted(set(odds)))

haystack = input()
seed = input()

needles = []
for i in range(len(seed)):
    needles.append(seed)
    seed = seed[1:] + seed[0]

found = False
for needle in needles:
    if needle in haystack:
        found = True
        break

print("yes" if found else "no")
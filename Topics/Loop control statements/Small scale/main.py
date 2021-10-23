l = []
while True:
    a = input()
    if a == ".":
        break
    l.append(float(a))
print(min(l))

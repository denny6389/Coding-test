s = input()
r = []
for i in s:
    if i == "<":
        r.pop()
    else:
        r.append(i)
print("".join(r))
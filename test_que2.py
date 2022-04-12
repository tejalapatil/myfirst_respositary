f1 = ["U1,U2","U3,U4","U1,U5","U2,U1","U3,U4"]

f2 = map(lambda each: each.strip('"'), f1)  # remove double quotes

temp = []

for i in f2:
    # print(i)
    temp.append(i.split(','))  # split seprated comma

print(temp)

print(set(tuple(sorted(i)) for i in temp))
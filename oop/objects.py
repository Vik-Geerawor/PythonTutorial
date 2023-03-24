l = [1, 2, 3]

# print(dir(l))       # NOTE: same as print(l.__dir__())

for i in dir(l):
    print(f"{i} - {type(i)}")

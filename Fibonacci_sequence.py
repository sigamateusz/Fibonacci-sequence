def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

x=int(input("How many numers you need? "))
for i in range(x):
    print('{0:4d}.{1:10d}'.format(i+1,F(i)))

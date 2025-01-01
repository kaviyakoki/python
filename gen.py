def value():
    n=1
    while n<10:
        val=n*n
        yield val 
        n+=2
a=value()
for i in a:
        print(i)
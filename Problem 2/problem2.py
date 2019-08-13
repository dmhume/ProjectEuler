def fibo(limit):
    first = 1
    second = 1
    x = 0
    y = 0
    while(x <= limit):
        if x % 2 == 0:
            y += x
        x = first + second
        first = second
        second = x
    return y

print(fibo(4000000))
        

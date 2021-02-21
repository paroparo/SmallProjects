def index_fib(x):
    if x >= 3:
        return index_fib(x-1) + index_fib(x-2)
    return 1

i = index_fib(10)
print(i)

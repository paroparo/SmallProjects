def fibo(k):
    if k <= 1:
        return k
    else:
        return(fibo(k-1) + fibo(k-2))

# if '__name__' == '__main__':
#     fibo(5)

range_number = int(input('Enter Fibonacci range:\n'))
print(f'You entered {range_number}')

print('Fibonacci sequence:\n')
for i in range(range_number):
    print(fibo(i))

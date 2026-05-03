def print_pyramid(n:int):
    for i in range(0, n):
        for j in range(0, n-i):
            print(f'',end=' ')

        for k in range(0,i):
            print('*' ,end=' ')
        print()
def reverse_pyramid(n:int):

    for i in range(0, n):
        for k in  range(0, i):
            print('', end=' ')
        for j in range(0,n-i):
            print('*',end=' ')

        print()

def left_pyramid(n:int):
    for i in range(0,n):
        for j in range(0, n-i):
            print(f'*', end=" ")

        print()



print_pyramid(5)
reverse_pyramid(5)
left_pyramid(5)
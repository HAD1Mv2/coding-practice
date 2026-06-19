import time

def normal_fib(n):

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = normal_fib(n-1)+normal_fib(n-2)
    return result


def dynamic_fib(n, memo = {}):

    if n in memo.keys():
        result = memo[n]
    else:
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = dynamic_fib(n-1)+dynamic_fib(n-2)

        memo[n] = result
    return result

if __name__=="__main__":

    n = 31
    start = time.perf_counter()
    result = normal_fib(n)
    end = time.perf_counter()
    print(f'{result}, normal fibonacci func time: {end-start}')

    start = time.perf_counter()
    result = dynamic_fib(n)
    end = time.perf_counter()
    print(f'{result}, dynamic fibonacci func time: {end-start}')
            


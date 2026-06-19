import time

def normal_fib(n):

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = normal_fib(n-1)+normal_fib(n-2)
    return result

def tab_fib(n):

    array = [0 for i in range(n+1)]
    array[1] = 1

    # this solution is little bit different from the video, but essentially the time complexity is the same, 
    # and it still guarantee that we add the finished calculated fibonacci numbers of the previous two indexes to calculate the fib number for index n.

    for i in range(2, len(array)):
        array[i]+=(array[i-1]+array[i-2])

    return array[n]

if __name__=="__main__":

    n = 31

    start = time.perf_counter()
    result = normal_fib(n)
    end = time.perf_counter()
    print(f'{result}, normal fibonacci func time: {end-start}')

    start = time.perf_counter()
    result = tab_fib(n)
    end = time.perf_counter()
    print(f'{result}, tab fibonacci func time: {end-start}')
            


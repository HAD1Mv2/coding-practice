import time

def normal_fib(n: int) -> int:
    """Calculate fibonacci number using vanilla recursion function without memoization technique.

    Parameters
    ----------
    n : int
        Index of fibonacci number.

    Returns
    -------
    output: int
        The nth-fibonacci number. 
    """

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = normal_fib(n-1)+normal_fib(n-2)
    return result


def dynamic_fib(n: int, memo: dict = {}) -> int:
    """Calculate fibonacci number using recursion function with memoization technique.

    Parameters
    ----------
    n : int
        Index of fibonacci number.
    memo : dict, optional
        Placeholder for the memo, by default {}.

    Returns
    -------
    int
        The nth-fibonacci number. 
    """

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
            


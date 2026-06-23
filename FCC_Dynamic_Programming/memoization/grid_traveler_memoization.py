import time
from typing import Any, Callable



def normal_recursion_grid_traveler(m: int, n: int) -> int:
    """Count how many ways to travel from the top left corner to the bottom right corner
    in a m * n grid with only right or down direction move, using normal recursion technique.

    Parameters
    ----------
    m : int
        Number of rows on m * n grid.
    n : int
        Number of columns on m * n grid.

    Returns
    -------
    output: int
        Number of ways to travel with right or down direction move from the top left to the bottom right corner on a m * n grid.
    """

    if m == 1 and n == 1:
        num_ways = 1
    elif m == 0  or n ==0:
        num_ways = 0
    else:
        num_ways = normal_recursion_grid_traveler(m-1,n)+normal_recursion_grid_traveler(m, n-1)

    return num_ways

def dynamic_grid_traveler_type_1(m: int, n:int, memo: dict={}) -> int:
    """  Cunt how many ways to travel from the top left corner to the bottom right corner
    in a m * n grid with only right or down direction move, using dynamic programming technique (memoization).

    Parameters
    ----------
    m : int
        Number of rows on m * n grid.
    n : int
        Number of columns on m * n grid.
    memo : dict, optional
        Placeholder for the memo, by default {}.

    Returns
    -------
    output: int
        number of ways to travel with right or down direction move from the top left to the bottom right corner on a m * n grid.
    """
    
    if m == 1 and n == 1:
        num_ways = 1
    elif m == 0  or n ==0:
        num_ways = 0
    else:
        if (m,n) in memo.keys():
            return memo[(m,n)]
        else:
            num_ways = dynamic_grid_traveler_type_1(m-1,n)+dynamic_grid_traveler_type_1(m, n-1)
    memo[(m,n)] = num_ways
    return num_ways

def dynamic_grid_traveler_type_2(m: int, n: int, memo: dict={}) -> int:
    """Count how many ways to travel from the top left corner to the bottom right corner
    in a m * n  grid with only right or down direction move, using dynamic programming technique
    but with less memory in memo compared to type I (in type I key [m,n] != [n, m] in the memo), 
    since num of ways in (m, n)-grid is the same with (n,m)-grid.

    Parameters
    ----------
    m : int
        Number of rows on m * n grid.
    n : int
        Number of columns on m * n grid.
    memo : dict, optional
        Placeholder for the memo, by default {}.

    Returns
    -------
    output: int
        Number of ways to travel with right or down direction move from the top left to the bottom right corner on a m * n grid.
    """
    
    if m == 1 and n == 1:
        num_ways = 1
    elif m == 0  or n ==0:
        num_ways = 0
    else:
        if (m,n) in memo.keys():
            return memo[(m,n)]
        elif (n,m) in memo.keys():
            return memo[(n,m)]
        else:
            num_ways = dynamic_grid_traveler_type_2(m-1,n)+dynamic_grid_traveler_type_2(m, n-1)
    memo[(m,n)] = num_ways
    return num_ways

def eval_func_runtime(func_:Callable[..., Any], inputs: Any):
    """Measure running time of a function.

    Parameters
    ----------
    func_ : Callable[..., Any]
        A python function.
    inputs : Any
        Inputs of func_, must follow the input structure func_.
    """

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'there are {result} ways to travel in ({m}, {n})-grid, solved in: {end-start} seconds using {func_.__name__}')

if __name__=="__main__":

    m = 15
    n = 14

    eval_func_runtime(normal_recursion_grid_traveler, (m, n))
    eval_func_runtime(dynamic_grid_traveler_type_1, (m, n))
    eval_func_runtime(dynamic_grid_traveler_type_2, (m, n))   
import time

def normal_recursion_grid_traveler(m, n):
    """
    function to count how many ways to travel from the top left corner to the bottom right corner
    in a m rows times n columns grid with only right and down movement, using normal recursion technique
    """
    if m == 1 and n == 1:
        num_ways = 1
    elif m == 0  or n ==0:
        num_ways = 0
    else:
        num_ways = normal_recursion_grid_traveler(m-1,n)+normal_recursion_grid_traveler(m, n-1)

    return num_ways

def dynamic_grid_traveler_type_1(m, n, memo={}):
    """
    function to count how many ways to travel from the top left corner to the bottom right corner
    in a m rows times n columns grid with only right and down movement, using dynamic programming technique
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

def dynamic_grid_traveler_type_2(m, n, memo={}):
    """
    function to count how many ways to travel from the top left corner to the bottom right corner
    in a m rows times n columns grid with only right and down movement, using dynamic programming technique
    but with less memory in memo compared to type I, since num of ways in (m, n)-grid is the same with (n,m)-grid
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

def eval_func_runtime(func_, inputs):

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
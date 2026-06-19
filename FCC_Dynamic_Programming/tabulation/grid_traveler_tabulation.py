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

def tab_grid_traveler(m,n):

    array = [[0 for j in range(n+1)] for i in range(m+1)]

    array[1][1] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            array[i][j] += (array[i][j-1] + array[i-1][j])

    # print(array)
    return array[m][n]    

if __name__=="__main__":

    m = 3
    n = 3

    start = time.perf_counter()
    result = normal_recursion_grid_traveler(m, n)
    end = time.perf_counter()
    print(f'there are {result} ways to travel in ({m}, {n})-grid, solved in: {end-start} seconds using normal recursion')       

    start = time.perf_counter()
    result = tab_grid_traveler(m, n)
    end = time.perf_counter()
    print(f'there are {result} ways to travel in ({m}, {n})-grid, solved in: {end-start} seconds using tabulation method')       
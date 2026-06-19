from re import A
import time
import copy

def normal_howsum(target_sum, numbers):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        result = normal_howsum(target_sum-num, numbers)
        if result != None:
            result.append(num)
            return result
    
    return None

def tab_howsum(target_sum, numbers):

    arr = [None for i in range(target_sum+1)]
    arr[0] = []

    for i in range(0, len(arr)-1):
        if arr[i] != None:
            for n in numbers:
                if i+n <= target_sum:
                    a = copy.deepcopy(arr[i])
                    a.append(n)
                    # print(a)
                    arr[i+n] = a
        # print(arr)

    return arr[-1]

if __name__=="__main__":

    target_sum = 250
    numbers = [7, 14]

    start = time.perf_counter()
    result = normal_howsum(target_sum, numbers)
    end = time.perf_counter()
    print(f'{target_sum} is a combination of {result}, solved in: {end-start} seconds using recursion method')

    start = time.perf_counter()
    result = tab_howsum(target_sum, numbers)
    end = time.perf_counter()
    print(f'{target_sum} is a combination of {result}, solved in: {end-start} seconds using tabulation method')     

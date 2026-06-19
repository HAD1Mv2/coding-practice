import time
import copy

def normal_bestsum(target_sum, numbers):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        result = normal_bestsum(target_sum-num, numbers)
        if result != None:
            result.append(num)
            if (shortest_combination == None) or (len(shortest_combination)>len(result)):
                shortest_combination = result
    
    return shortest_combination

def tab_bestsum(target_sum, numbers):

    arr = [None for i in range(target_sum+1)]
    arr[0] = []

    for i in range(0, len(arr)-1):
        if arr[i] != None:
            for n in numbers:
                if i+n <= target_sum:
                    a = copy.deepcopy(arr[i])
                    a.append(n)
                    # print(a)
                    if arr[i+n]== None:
                        arr[i+n] = a
                    else:
                        if len(a)<len(arr[i+n]):
                            arr[i+n] = a
        # print(arr)

    return arr[-1]

if __name__=="__main__":

    target_sum = 250
    numbers = [7, 14]

    start = time.perf_counter()
    result = normal_bestsum(target_sum, numbers)
    end = time.perf_counter()
    print(f'best combination {result} with {target_sum}, solved in: {end-start} seconds using normal recursion') 

    start = time.perf_counter()
    result = tab_bestsum(target_sum, numbers)
    end = time.perf_counter()
    print(f'best combination {result} with {target_sum}, solved in: {end-start} seconds using tabulation') 
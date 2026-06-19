import time

def normal_cansum(target_sum, numbers):

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if normal_cansum(target_sum-num, numbers):
            return True
    
    return False

def tab_cansum(target_sum, numbers):
    
    table = [False for i in range(target_sum+1)]
    table[0]= True

    for i in range(len(table)):
        if table[i]:
            for j in numbers:
                if i+j<=target_sum:
                    table[i+j] = True

    # print(table)
    return table[-1]

if __name__=="__main__":

    target_sum = 8
    numbers = [2, 3, 5]

    start = time.perf_counter()
    result = normal_cansum(target_sum, numbers)
    end = time.perf_counter()
    print(f'it is {result} that {target_sum} can be a combination of {numbers}, solved in: {end-start} seconds using recursion method')

    start = time.perf_counter()
    result = tab_cansum(target_sum, numbers)
    end = time.perf_counter()
    print(f'it is {result} that {target_sum} can be a combination of {numbers}, solved in: {end-start} seconds using tabulation method')     
import time

def normal_cansum(target_sum, numbers, *args):

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if normal_cansum(target_sum-num, numbers):
            return True
    
    return False

def dynamic_cansum(target_sum, numbers, memo):

    if target_sum in memo.keys():
        return memo[target_sum]

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if dynamic_cansum(target_sum-num, numbers, memo):
            # print(memo)
            memo[target_sum] = True
            return True
    # print(memo)
    memo[target_sum] = False
    return False    


def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'{result} that \'{inputs[0]}\' can be summed from \'{inputs[1]}\', solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":


    inputs_set = [(8, [3, 7, 5], {}), (200, [7, 14], {})]
    funcs_set = [normal_cansum, dynamic_cansum] 

    for inputs in inputs_set:
        for func_ in funcs_set:
            eval_func_runtime(func_, inputs)
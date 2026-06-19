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

def dynamic_howsum(target_sum, numbers, memo):

    if target_sum in memo.keys():
        return memo[target_sum]

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    for num in numbers:
        result = copy.copy(dynamic_howsum(target_sum-num, numbers, memo))
        if result != None:
            result.append(num)
            memo[target_sum] = copy.copy(result)
            return result
    memo[target_sum] = None
    return None    

def eval_func_runtime(func_, args):

    start = time.perf_counter()
    result = func_(*args)
    end = time.perf_counter()
    print(f'{result}, solved in: {end-start} seconds using {func_.__name__}')


if __name__=="__main__":

    eval_func_runtime(normal_howsum, (26, [3, 7, 5]))
    eval_func_runtime(dynamic_howsum, (26, [3, 7, 5], {}))
    eval_func_runtime(normal_howsum,(250, [7, 14]))
    eval_func_runtime(dynamic_howsum, (250, [7, 14], {}))
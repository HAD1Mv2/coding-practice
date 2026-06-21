import time
from typing import Any, Callable

def normal_cansum(target_sum: int, numbers: list[int], *args) -> bool:

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if normal_cansum(target_sum-num, numbers):
            return True
    
    return False

def dynamic_cansum(target_sum: int, numbers: list[int], memo: dict) -> bool:

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


def eval_func_runtime(func_:Callable[..., Any], inputs: Any):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'{result} that \'{inputs[0]}\' can be summed from \'{inputs[1]}\', solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":


    inputs_set: list[tuple[int, list[int], dict]] = [(8, [3, 7, 5], {}), (200, [7, 14], {})]
    funcs_set: list[Callable[..., Any]] = [normal_cansum, dynamic_cansum] 

    for inputs in inputs_set:
        for func_ in funcs_set:
            eval_func_runtime(func_, inputs)
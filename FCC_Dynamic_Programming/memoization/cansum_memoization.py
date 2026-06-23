import time
from typing import Any, Callable

def normal_cansum(target_sum: int, numbers: list[int], *args) -> bool:
    """Check whether target_sum is a summation of numbers, an element of numbers can be used multiple times.

    Parameters
    ----------
    target_sum : int
        Target number.
    numbers : list[int]
        List of number used in summation operation to get target_sum.

    Returns
    -------
    output : bool
        True or False whether the solution exist.
    """

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False

    for num in numbers:
        if normal_cansum(target_sum-num, numbers):
            return True
    
    return False

def dynamic_cansum(target_sum: int, numbers: list[int], memo: dict) -> bool:
    """Check whether target_sum is a summation of numbers, an element of numbers can be used multiple times.
    The function use memoization technique.

    Parameters
    ----------
    target_sum : int
        Target number.
    numbers : list[int]
        List of number used in summation operation to get target_sum.
    memo : dict
        Placeholder for memo.

    Returns
    -------
    output : bool
        True or False whether the solution exist.
    """

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
    print(f'{result} that \'{inputs[0]}\' can be summed from \'{inputs[1]}\', solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":


    inputs_set: list[tuple[int, list[int], dict]] = [(8, [3, 7, 5], {}), (200, [7, 14], {})]
    funcs_set: list[Callable[..., Any]] = [normal_cansum, dynamic_cansum] 

    for inputs in inputs_set:
        for func_ in funcs_set:
            eval_func_runtime(func_, inputs)
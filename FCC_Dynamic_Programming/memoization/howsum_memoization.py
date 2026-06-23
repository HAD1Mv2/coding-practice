import time
import copy
from typing import Any, Callable


def normal_howsum(target_sum: int, numbers: list[int]) -> list[int] | None:
    """Check whether target_sum is a summation of numbers and return the solution, an element of numbers can be used multiple times.


    Parameters
    ----------
    target_sum : int
        Target number.
    numbers : list[int]
        List of number used in summation operation to get target_sum.

    Returns
    -------
    list[int] | None
        The solution in the form of numbers combination, return None if there isn't any.
    """

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

def dynamic_howsum(target_sum: int, numbers: list[int], memo: dict) -> list[int] | None:
    """Check whether target_sum is a summation of numbers and return the solution, an element of numbers can be used multiple times.
    This function use memoization technique.

    Parameters
    ----------
    target_sum : int
        Target number.
    numbers : list[int]
        List of number used in summation operation to get target_sum.
    memo : dict
        A placeholder for memo.

    Returns
    -------
    list[int] | None
        The solution in the form of numbers combination, return None if there isn't any solution.
    """

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

def eval_func_runtime(func_:Callable[..., Any], args: Any):
    """Measure running time of a function.

    Parameters
    ----------
    func_ : Callable[..., Any]
        A python function.
    args : Any
        Inputs of func_, must follow the input structure func_.
    """

    start = time.perf_counter()
    result = func_(*args)
    end = time.perf_counter()
    print(f'{result}, solved in: {end-start} seconds using {func_.__name__}')


if __name__=="__main__":

    eval_func_runtime(normal_howsum, (26, [3, 7, 5]))
    eval_func_runtime(dynamic_howsum, (26, [3, 7, 5], {}))
    eval_func_runtime(normal_howsum,(250, [7, 14]))
    eval_func_runtime(dynamic_howsum, (250, [7, 14], {}))
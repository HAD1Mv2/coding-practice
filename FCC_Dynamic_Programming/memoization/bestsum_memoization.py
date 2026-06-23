import time
import copy
from typing import Any, Callable

def normal_bestsum(target_sum: int, numbers: list[int], *args) -> list[int] | None:
    """Check whether target_sum is a summation of numbers, 
    return the best solution (shortest solution), an element of numbers can be used multiple times.

    Parameters
    ----------
    target_sum : int
        Target number.
    numbers : list[int]
        List of number used in summation operation to get target_sum.

    Returns
    -------
    output : list[int] | None
        The shortest solution or None of there isn't any.
    """

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination: list[int] | None = None

    for num in numbers:
        result = normal_bestsum(target_sum-num, numbers)
        if result != None:
            result.append(num)
            if (shortest_combination == None) or (len(shortest_combination)>len(result)):
                shortest_combination = result
    
    return shortest_combination

def dynamic_bestsum(target_sum: int, numbers: list[int], memo:dict) -> list[int] | None:
    """Check whether target_sum is a summation of numbers, 
    return the best solution (shortest solution), an element of numbers can be used multiple times.
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
    output : list[int] | None
        The shortest solution or None of there isn't any.
    """

    if target_sum in memo.keys():
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination: list[int] | None = None

    for num in numbers:
        # need to use copy so that fixed info in memo not accidentaly modified
        result = copy.copy(dynamic_bestsum(target_sum-num, numbers, memo))
        if result != None:
            result.append(num)
            if (shortest_combination == None) or (len(shortest_combination)>len(result)):
                shortest_combination = result
    memo[target_sum] = copy.copy(shortest_combination)
    return shortest_combination    


def eval_func_runtime(func_: Callable[..., Any], inputs: Any):
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
    print(f'given target sum {inputs[0]} and building blocks numbers {inputs[1]}, the best combination is {result}, solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":


    inputs_set: list[tuple[int, list[int], dict]]=[(8, [1, 4, 5], {}), (75, [2, 5, 25], {})]
    func_set: list[Callable] = [normal_bestsum, dynamic_bestsum]

    for inputs in inputs_set:
        for func_ in func_set:
            eval_func_runtime(func_, inputs)
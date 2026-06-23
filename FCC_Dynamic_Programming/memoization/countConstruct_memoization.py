import time
import re
from typing import Any, Callable

def regular_count_construct(target_string: str, word_bank: list[str], *args) -> int:
    """Count number of ways target_string can be constructed from word_banks.
    every element in word_bank can be used multiple times.

    Parameters
    ----------
    target_string : str
        String we want to reconstruct.
    word_bank : list[str]
        List of strings used to try reconstruct target_string. Every element in word_bank are unique.

    Returns
    -------
    out : int
        Number of solutions. 
    """
    if target_string =='':
        return 1

    num = 0
    for word in word_bank:
        x = re.search(r'\b{}'.format(word), target_string)
        if x:
            new_target_string = target_string[x.span()[1]:]
            # print(new_target_string)
            num += regular_count_construct(new_target_string, word_bank)
    
    return num

def dynamic_count_construct(target_string: str, word_bank: list[str], memo: dict) -> int:
    """Count number of ways target_string can be constructed from word_banks.
    every element in word_bank can be used multiple times. This function use memoization technique.

    Parameters
    ----------
    target_string : str
        String we want to reconstruct.
    word_bank : list[str]
        List of strings used to try reconstruct target_string. Every element in word_bank are unique.
    memo : dict
        Placeholder for memo.

    Returns
    -------
    out : int
        Number of solutions. 
    """

    if target_string in memo.keys():
        return memo[target_string]

    if target_string =='':
        return 1

    num = 0
    for word in word_bank:
        x = re.search(r'\b{}'.format(word), target_string)
        if x:
            new_target_string = target_string[x.span()[1]:]
            # print(new_target_string)
            num += dynamic_count_construct(new_target_string, word_bank, memo)

    memo[target_string] = num
    return num

def eval_func_runtime(func_: Callable[..., Any], inputs: Any):
    """Measure running time of a function.

    Parameters
    ----------
    func_ : Callable[..., Any]
        A python function.
    inputs : Any
        Input of func_. Follow the structure of can_construct functions above.
    """

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'there are {result} ways to construct string \'{inputs[0]}\' from {inputs[1]}, solved in: {end-start} seconds using {func_.__name__}')

if __name__=="__main__":

    inputs_set: list[tuple[str, list[str], dict]]=[("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}),
               ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}),
               ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {})]
    
    func_list: list[Callable] = [regular_count_construct, dynamic_count_construct]

    for inputs in inputs_set:
        for func_ in func_list:
            eval_func_runtime(func_, inputs)
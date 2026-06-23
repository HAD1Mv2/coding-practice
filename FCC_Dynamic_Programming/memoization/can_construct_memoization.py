import time
import re
from typing import Any, Callable

def regular_can_construct(target_string: str, word_bank: list[str], *args) -> bool:
    """Given a word(target_string) and a list of words(word_bank), check whether target_string can be reconstruct using words in word_bank.
    An element in word_bank may be used multiple times.

    Parameters
    ----------
    target_string : str
        String we want to reconstruct.
    word_bank : list[str]
        List of strings used to try reconstruct target_string. Every element in word_bank are unique.

    Returns
    -------
    output : bool
        True or False, whether the target_string can be reconstruct from word_banks.
    """

    if target_string =='':
        return True

    for word in word_bank:
        x = re.search(r'\b{}'.format(word), target_string)
        if x:
            new_target_string = target_string[x.span()[1]:]
            # print(new_target_string)
            if regular_can_construct(new_target_string, word_bank):
                return True
    
    return False

def dynamic_can_construct(target_string: str, word_bank: list[str], memo: dict) -> bool:
    """Given a word(target_string) and a list of words(word_bank), 
    check whether target_string can be reconstruct using words in word_bank.
    An element in word_bank may be used multiple times.
    This function use memoization technique.

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
    output : bool
        True or False, whether the target_string can be reconstruct from word_banks.
    """

    if target_string in memo.keys():
        return memo[target_string]

    if target_string =='':
        return True

    for word in word_bank:
        x = re.search(r'\b{}'.format(word), target_string)
        if x:
            new_target_string = target_string[x.span()[1]:]
            # print(new_target_string)
            if dynamic_can_construct(new_target_string, word_bank, memo):
                memo[target_string] = True
                return True

    memo[target_string] = False
    return False

def eval_func_runtime(func_: Callable[..., Any], inputs: tuple[str, list[str], dict]):
    """Measure running time of a function.

    Parameters
    ----------
    func_ : Callable[..., Any]
        A python function.
    inputs : tuple[str, list[str], dict]
        Input of func_. Follow the structure of can_construct functions above.
    """

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'it is {result} that \'{inputs[0]}\' can be constructed from \'{inputs[1]}\', solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":

    inputs_set: list[tuple[str, list[str], dict]]=[("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}), 
                ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {})]

    func_set: list[Callable[..., bool]] = [regular_can_construct, dynamic_can_construct]

    for inputs in inputs_set:
        for func_ in func_set:
            eval_func_runtime(func_, inputs)
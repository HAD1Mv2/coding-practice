import time
import re

def regular_can_construct(target_string, word_bank, *args):

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

def dynamic_can_construct(target_string, word_bank, memo):

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

def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'it is {result} that \'{inputs[0]}\' can be constructed from \'{inputs[1]}\', solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":

    inputs_set=[("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}), 
                ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {})]

    func_set = [regular_can_construct, dynamic_can_construct]

    for inputs in inputs_set:
        for func_ in func_set:
            eval_func_runtime(func_, inputs)
import time
import re

def regular_count_construct(target_string, word_bank, *args):

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

def dynamic_count_construct(target_string, word_bank, memo):

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

def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'there are {result} ways to construct string \'{inputs[0]}\' from {inputs[1]}, solved in: {end-start} seconds using {func_.__name__}')

if __name__=="__main__":

    inputs_set=[("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}),
               ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}),
               ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], {})]
    
    for inputs in inputs_set:
        for func_ in [regular_count_construct, dynamic_count_construct]:
            eval_func_runtime(func_, inputs)
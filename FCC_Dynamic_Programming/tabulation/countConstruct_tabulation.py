import time
import re

def regular_count_construct(target_string, word_bank):

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

def tab_count_construct(target_string, word_bank):

    table = [0 for i in range(len(target_string)+1)]
    table[0] = 1

    for i in range(len(table)):
        if table[i]>0:
            for word in word_bank:
                if target_string[i:i+len(word)]==word:
                    table[i+len(word)]+=table[i]

    return table[-1]

def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'there are {result} ways to construct string \'{inputs[0]}\' from {inputs[1]}, solved in: {end-start} seconds using {func_.__name__}')

if __name__=="__main__":


    # correctness test
    # print(tab_count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
    # print(tab_count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    # print(tab_count_construct("skateboard",[]))
    # print(tab_count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    # print(tab_count_construct("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))    

    inputs_set=[("abcdef", ["ab", "abc", "cd", "def", "abcd"]),
                ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]),
                ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]),
                ]
    
    # running time comparison test
    for inputs in inputs_set:
        for func_ in [regular_count_construct, tab_count_construct]:
            eval_func_runtime(func_, inputs)
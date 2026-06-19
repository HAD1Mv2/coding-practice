import time
import re

def regular_can_construct(target_string, word_bank):

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

def tab_can_construct(target_string, word_bank):

    table = [False for i in range(len(target_string)+1)]
    table[0] = True

    for i in range(len(table)):
        if table[i]:
            for word in word_bank:
                if target_string[i:i+len(word)]==word:
                    table[i+len(word)]=True

    return table[-1]

def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'it is {result} that \'{inputs[0]}\' can be constructed from \'{inputs[1]}\', solved in: {end-start} seconds using {func_.__name__}') 

if __name__=="__main__":

    # #correctness test
    # print(tab_can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True
    # print(tab_can_construct("skateboard",[])) # False
    # print(tab_can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    # print(tab_can_construct("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False

    inputs_set=[("abcdef", ["ab", "abc", "cd", "def", "abcd"]), 
                ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])]

    func_set = [regular_can_construct, tab_can_construct]

    for inputs in inputs_set:
        for func_ in func_set:
            eval_func_runtime(func_, inputs)


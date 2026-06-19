import time
import re
import copy

def print_all_combination(combinations):

    for comb in combinations:
        print(comb)

def regular_all_construct(target_string, word_bank):

    if target_string =='':
        return [[]]

    all_combs= []
    for word in word_bank:
        x = re.search(r'\b{}'.format(word), target_string)
        if x:
            new_target_string = target_string[x.span()[1]:]
            # print(new_target_string)
            combs = copy.deepcopy(regular_all_construct(new_target_string, word_bank))
            for i in range(len(combs)):
                combs[i].insert(0, word)
            all_combs.extend(combs)

    return all_combs


def tab_all_construct(target_string, word_bank):

    table = [[] for i in range(len(target_string)+1)]
    table[0] = [[]]

    for i in range(len(table)):
        if len(table[i]) != 0:
            for word in word_bank:
                if target_string[i:i+len(word)]==word:
                    new_comb = copy.deepcopy(table[i])
                    for e in new_comb:
                        e.append(word)
                    table[i+len(word)]+=new_comb

    return table[-1]

def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print('\n===================================================\n')
    if len(result)>0:
        print(f'there are {len(result)} the combinations, solved in: {end-start} seconds using {func_.__name__}')
        print("list of combinations:\n")
        print_all_combination(result)
    else:
        print(f"there is no combination, solved in: {end-start} seconds using {func_.__name__}")
    print('\n===================================================\n') 


if __name__=="__main__":

    inputs_set=[("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]), 
                ("purple", ["purp", "p", "ur", "le", "purpl"]),
                ("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]), 
                ("aaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]),
                ("abcdef", ["ab", "abc", "cd", "def", "abcd"]),
                ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]),
                ("eeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])]
    
    func_set = [regular_all_construct, tab_all_construct]


    for inputs in inputs_set:
        for func_ in func_set:
            eval_func_runtime(func_, inputs)
import time
import copy

def normal_bestsum(target_sum, numbers, *args):

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        result = normal_bestsum(target_sum-num, numbers)
        if result != None:
            result.append(num)
            if (shortest_combination == None) or (len(shortest_combination)>len(result)):
                shortest_combination = result
    
    return shortest_combination

def dynamic_bestsum(target_sum, numbers, memo):

    if target_sum in memo.keys():
        return memo[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    shortest_combination = None

    for num in numbers:
        # need to use copy so that fixed info in memo not accidentaly modified
        result = copy.copy(dynamic_bestsum(target_sum-num, numbers, memo))
        if result != None:
            result.append(num)
            if (shortest_combination == None) or (len(shortest_combination)>len(result)):
                shortest_combination = result
    memo[target_sum] = copy.copy(shortest_combination)
    return shortest_combination    


def eval_func_runtime(func_, inputs):

    start = time.perf_counter()
    result = func_(*inputs)
    end = time.perf_counter()
    print(f'given target sum {inputs[0]} and building blocks numbers {inputs[1]}, the best combination is {result}, solved in: {end-start} seconds using {func_.__name__}') 


if __name__=="__main__":


    inputs_set=[(8, [1, 4, 5], {}), (75, [2, 5, 25], {})]
    func_set = [normal_bestsum, dynamic_bestsum]

    for inputs in inputs_set:
        for func_ in func_set:
            eval_func_runtime(func_, inputs)
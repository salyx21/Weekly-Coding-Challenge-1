def second_max(num_inputs, ls):
    result = ""
    for i in ls: 
        num_inputs -= 1
        result += f"{(sorted(list(map(int,i.split())))[-2])}" if num_inputs == 0 else f"{(sorted(list(map(int,i.split())))[-2])}\n"
    return result

def sum_digits_in_string(num_inputs, ls):
    result = ""
    for i in ls:
        num_inputs -= 1
        total = sum(list(map(int,([num for num in i if num.isnumeric()]))))
        result += f"{total}" if num_inputs == 0 else f"{total}\n"
    return result
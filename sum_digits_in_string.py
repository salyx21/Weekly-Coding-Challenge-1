num_inputs = int(input())
ls = [input() for i in range(num_inputs)]
for i in ls: 
    print(sum(list(map(int,([num for num in i if num.isnumeric()])))))
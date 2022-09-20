num_inputs = int(input())
ls = [input() for i in range(num_inputs)]
for i in ls: 
    print(sorted(list(map(int,i.split())))[-2])
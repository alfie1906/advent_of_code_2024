data_path = 'input.txt'
with open(data_path, 'r') as file:
    data = file.read().splitlines()

left_list = sorted([int(line.split('   ')[0]) for line in data])
right_list = sorted([int(line.split('   ')[1]) for line in data])

distance = sum([abs(right_list[i] - left_list[i]) for i in range(len(left_list))])
print("p1 solution:", distance)

total_similarity = sum([num * right_list.count(num) for num in left_list])
print("p2 solution:", total_similarity)
from collections import defaultdict, deque

data_path = 'input.txt'
with open(data_path, 'r') as file:
    data = file.read().splitlines()

page_orders = [entry for entry in data if '|' in entry]
updates = [entry for entry in data if ',' in entry]

graph = defaultdict(list)
in_degree = defaultdict(int)

for pair in page_orders:
    before, after = pair.split('|')
    graph[before].append(after)
    in_degree[after] += 1
    in_degree[before] += 0

sort_key = []
queue = deque([node for node in in_degree if in_degree[node] == 0])

while queue:
    node = queue.popleft()
    sort_key.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

correctly_sorted_update_scores = 0
for update in updates:
    page_numbers = list(map(int, update.split(',')))

    sorted_page_numbers = sorted(page_numbers, key=lambda x: sort_key.index(x))
    if page_numbers == sorted_page_numbers:
        middle_value = page_numbers[len(page_numbers) // 2]
        correctly_sorted_update_scores += middle_value

print("p1 solution:", correctly_sorted_update_scores)
        

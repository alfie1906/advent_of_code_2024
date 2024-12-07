data_path = 'input.txt'
with open(data_path, 'r') as file:
    horizontal_lines = file.read().splitlines()

vertical_lines = ["".join([line[index] for line in horizontal_lines]) for index in range(len(horizontal_lines[0]))]
diagonal_lines = []
for i, letter in enumerate(horizontal_lines[0]):
    right_diagonal = "".join([line[i+j] for j, line in enumerate(horizontal_lines) if i+j < len(line)])
    left_diagonal = "".join([line[i-j] for j, line in enumerate(horizontal_lines) if i-j >= 0])
    diagonal_lines += [right_diagonal, left_diagonal]

for i, letter in enumerate(horizontal_lines[-1]):
    right_diagonal = "".join([line[i+j] for j, line in enumerate(horizontal_lines[::-1]) if i+j < len(line)])
    left_diagonal = "".join([line[i-j] for j, line in enumerate(horizontal_lines[::-1]) if i-j >= 0])
    if i == 0:
        pass
    elif i == len(horizontal_lines) - 1:
        pass
    else:
        diagonal_lines += [right_diagonal, left_diagonal]

all_lines = horizontal_lines + vertical_lines + diagonal_lines

xmas_count = 0
for line in all_lines:
    xmas_count += line.count("XMAS")
    xmas_count += line.count("SAMX")

print("p1 solution:", xmas_count)

xmas_cross_count = 0
for i, row in enumerate(horizontal_lines):
    for j, letter in enumerate(row):
        if letter == "A":
            if i == 0 or j == 0:
                continue
            elif i == len(horizontal_lines) - 1 or j == len(row) - 1:
                continue
            elif horizontal_lines[i-1][j-1] == "M" and horizontal_lines[i+1][j+1] == "S" and horizontal_lines[i-1][j+1] == "M" and horizontal_lines[i+1][j-1] == "S":
                xmas_cross_count += 1
            elif horizontal_lines[i-1][j-1] == "S" and horizontal_lines[i+1][j+1] == "M" and horizontal_lines[i-1][j+1] == "M" and horizontal_lines[i+1][j-1] == "S":
                xmas_cross_count += 1
            elif horizontal_lines[i-1][j-1] == "M" and horizontal_lines[i+1][j+1] == "S" and horizontal_lines[i-1][j+1] == "S" and horizontal_lines[i+1][j-1] == "M":
                xmas_cross_count += 1
            elif horizontal_lines[i-1][j-1] == "S" and horizontal_lines[i+1][j+1] == "M" and horizontal_lines[i-1][j+1] == "S" and horizontal_lines[i+1][j-1] == "M":
                xmas_cross_count += 1

print("p2 solution:", xmas_cross_count)
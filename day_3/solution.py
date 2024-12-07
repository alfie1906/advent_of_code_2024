import re

data_path = 'input.txt'
with open(data_path, 'r') as file:
    data = file.read().splitlines()

def mul(a, b):
    return a * b

instructions = ''.join(data)
mul_commands = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)

results = sum(eval(command) for command in mul_commands)
print("p1 solution:", results)

disabled_instructions = re.findall(r"(?<=don't).*?(?=do)", instructions)
for instruction in disabled_instructions:
    instructions = instructions.replace(instruction, '')

mul_commands = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)
results = sum(eval(command) for command in mul_commands)
print("p2 solution:", results)

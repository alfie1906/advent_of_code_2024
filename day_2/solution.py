data_path = 'input.txt'
with open(data_path, 'r') as file:
    data = file.read().splitlines()

def report_safe(report_line: str, remove_index: int = None) -> bool:
    report_numbers = list(map(int, report_line.split(' ')))
    
    if remove_index == 0:
        report_numbers = report_numbers[1:]
    elif remove_index:
        report_numbers.pop(remove_index)

    distances = [current - report_numbers[index] for index, current in enumerate(report_numbers[1:])]
    max_distance = max(abs(distance) for distance in distances)
    if not all([distance < 0 for distance in distances]) and not all([distance > 0 for distance in distances]):
        return False
    elif max_distance > 3:
        return False
    else:
        return True
    
safe_reports = sum([report_safe(report) for report in data])
print("p1 solution:", safe_reports)

safe_reports = 0
for report in data:
    if report_safe(report):
        safe_reports += 1
    else:
        for index in range(len(report.split(' '))):
            if report_safe(report, index):
                safe_reports += 1
                break

print("p2 solution:", safe_reports)

    


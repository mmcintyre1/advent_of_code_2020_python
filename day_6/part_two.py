import pathlib


data = pathlib.Path('puzzle_input.txt').read_text().replace('\n', ' ')

groups = [
    x.strip().split(' ')
    for x in data.split('  ')
    if x.strip()
]

count = 0
for group in groups:
    if len(group) == 1:
        count += len(set(group[0]))
    else:
        count += len(set.intersection(*map(set, group)))

print(count)

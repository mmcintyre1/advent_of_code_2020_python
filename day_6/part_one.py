import pathlib

data = pathlib.Path('puzzle_input.txt').read_text().replace('\n', ' ')
counts = sum([
    len(set("".join(x.strip().split(' '))))
    for x in data.split('  ')
    if x.strip()
])

print(counts)

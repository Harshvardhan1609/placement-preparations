counts = {'L': 0, 'R': 0}
s = input()

for char in s:
    if char in counts:
        counts[char] += 1

if counts['L'] == counts['R']:
    print(True)
else:
    print(False)

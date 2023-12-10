#%%
# Puzzle 1
import re
file_path = 'data.txt'
write_file_path = 'manipulated.txt'

pattern = re.compile(r'(\D+?(\d+)\D+?)')
content = []

with open(file_path, 'r') as file:
    for line in file:
        content.append(line.strip())

for index, line in enumerate(content[1:-1]): # Starting on line 2
    # Initialize a list to store positions
    symbol_positions = []
    
    # Dictionary to store positions of digits and the recorded digit
    positions_and_digits = {}

    # Iterate through the characters and store positions
    for index, char in enumerate(line):
        if not (char.isdigit() or char == '.'):
            symbol_positions.append(index)
    
    # Looking for parts in the line above
    for position in symbol_positions:
        position_diagonal_left = position - 1
        position_diagional_right = position + 1
        match = pattern.search(content[index - 1][position_diagonal_left])

        if match:
            digit = match.group(1)
            positions_and_digits[position] = digit
with open(write_file_path, 'w') as write_file:
    for line in content:
        write_file.write(line)
# %%

#%%
file_path = 'data.txt'

pattern = re.compile(r'(\D+?(\d+)\D+?)')

with open(file_path, 'r') as file:
    content = file.read()
    print(content)
# %%

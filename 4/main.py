#%%
# Puzzle 1
import re
file_path = 'data.txt'

total = 0

with open(file_path, 'r') as file:
    for line in file:
        matches = 0
        winning_numbers_string = line.split(':')[1].split('|')[0].strip()
        text_numbers_list = re.split(r'\s+', winning_numbers_string)
        winning_numbers = list(map(int, text_numbers_list))
        
        my_numbers_string = line.split(':')[1].split('|')[1].strip()
        my_text_numbers_list = re.split(r'\s+', my_numbers_string)
        my_numbers = list(map(int, my_text_numbers_list))
        
        for number in winning_numbers:
            if number in my_numbers:
                matches += 1
        
        if matches > 0:
            total += 2 ** (matches - 1)

print(total)
# %%

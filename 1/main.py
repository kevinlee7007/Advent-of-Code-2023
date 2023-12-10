#%%
# Puzzle 1
file_path = 'data.txt'

with open(file_path, 'r') as file:  
    total = 0
    
    for line in file: # Iterates through each line of data
        digit1 = next((c for c in line if c.isdigit()), None) # Grabs first digit encountered in the line
        digit2 = next((c for c in reversed(line) if c.isdigit()), None) # Grabs first digit encountered in the reversed line aka the last digit
        
        sub_total = int(digit1) * 10 + int(digit2)
        total += sub_total
    
    print(total)
# %% 
# Puzzle 2
file_path = 'data.txt'

with open(file_path, 'r') as file:  
    total = 0
    num_dict = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    
    for line in file: # Iterates through each line of data
        snippet_length = 1 # Start with a snippet of 3 and go until we equal the size of the line
        # while loop to take care of going from the start to the end
        replacement_detected = False
        digit1 = ""
        snippet = ""
        while (snippet_length < len(line)):
            snippet = line[:snippet_length]
            for key, value in num_dict.items():
                if key in snippet:
                    snippet = snippet.replace(key, value)
                    replacement_detected = True
                    break
            if replacement_detected or snippet_length == len(line):
                break
            snippet_length += 1
        
        digit1 = next((c for c in snippet if c.isdigit()), None) # Grabs first digit encountered in the line

        
        snippet_length = 1 # Start with a snippet of 3 and go until we equal the size of the line
        # while loopo to take care of going from the end to the start
        replacement_detected = False
        digit2 = ""
        snippet = ""
        while (snippet_length < len(line) + 1):
            snippet = line[-snippet_length:]
            for key, value in num_dict.items():
                if key in snippet:
                    snippet = snippet.replace(key, value)
                    replacement_detected = True
                    break
            if replacement_detected or snippet_length == len(line):
                break
            snippet_length += 1
        
        digit2 = next((c for c in reversed(snippet) if c.isdigit()), None) # Grabs first digit encountered in the reversed line aka the last digit
        
        print(line)
        
        print(f"digit1: {digit1}")
        print(f"digit2: {digit2}")
        
        sub_total = int(digit1) * 10 + int(digit2)
        total += sub_total
        print(f"Sub: {sub_total}")
        print(f"Total: {total}")
    
    print(total)
# %%

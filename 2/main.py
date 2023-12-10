#%%
# Puzzle 1
file_path = 'data.txt'

with open(file_path, 'r') as file:
    max_red = 12
    max_green = 13
    max_blue = 14
    total = 0
    
    for line in file:
        game_number = int(line.split(':')[0].replace("Game ",""))
        games = line.split(':')[1].split(';')
        valid_game = True
        
        for game in games:
            color_split = game.split(",")
            num_red = 0
            num_green = 0
            num_blue = 0
            for color in color_split:
                if ("red" in color):
                    num_red = int(color.split("red")[0].strip())
                    if (num_red > max_red):
                        valid_game = False
                        break
                if ("green" in color):
                    num_green = int(color.split("green")[0].strip())
                    if (num_green > max_green):
                        valid_game = False
                        break
                if ("blue" in color):
                    num_blue = int(color.split("blue")[0].strip())
                    if (num_blue > max_blue):
                        valid_game = False
                        break
            if (not valid_game):
                break
        if (valid_game):
            total += game_number
    
    print(total)
# %%

# %%
# Puzzle 2
file_path = 'data.txt'

with open(file_path, 'r') as file:
    total = 0
    
    for line in file:
        game_number = int(line.split(':')[0].replace("Game ",""))
        games = line.split(':')[1].split(';')
        min_red = 0
        min_green = 0
        min_blue = 0
        
        for game in games:
            color_split = game.split(",")
            for color in color_split:
                if ("red" in color):
                    num_red = int(color.split("red")[0].strip())
                    if (num_red > min_red):
                        min_red = num_red
                if ("green" in color):
                    num_green = int(color.split("green")[0].strip())
                    if (num_green > min_green):
                        min_green = num_green
                if ("blue" in color):
                    num_blue = int(color.split("blue")[0].strip())
                    if (num_blue > min_blue):
                        min_blue = num_blue
        total += min_red * min_green * min_blue
    
    print(total)
# %%

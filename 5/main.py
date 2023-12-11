#%%
# Puzzle 1
file_path = 'data.txt'

def find_line(data, number):
    for i, inner_list in enumerate(data):
        start_of_map = inner_list[1]
        end_of_map = inner_list[1] + inner_list[2] - 1

        if start_of_map <= number <= end_of_map:
            return i  # Return the index of the line

    return None  # Return None if the number is not found in any line

def next_mapping(map, input):
    map_line_seek = find_line(map, input)
    if map_line_seek == None:
        return input
    else:
        source_diff = input - map[map_line_seek][1]
        return source_diff + map[map_line_seek][0]


with open(file_path, 'r') as file:
    data = file.read()
    # Split the data into three parts based on the section headers
    sections = data.split('\n\n')
    
    # Separate the first line of seeds
    seeds_header, seeds_line = sections[0].strip().split(':')
    seeds_list = list(map(int, seeds_line.split()))

    # Seed to Soil Map
    seed_to_soil_header, seed_to_soil_line = sections[1].strip().split(':')
    seed_to_soil_list = seed_to_soil_line.strip().split('\n')
    seed_to_soil_list = [line.split(' ') for line in seed_to_soil_list]
    seed_to_soil_list = [[int(num) for num in sub_list] for sub_list in seed_to_soil_list]
    
    # Soil to Fertilizer Map
    soil_to_fertilizer_header, soil_to_fertilizer_line = sections[2].strip().split(':')
    soil_to_fertilizer_list = soil_to_fertilizer_line.strip().split('\n')
    soil_to_fertilizer_list = [line.split(' ') for line in soil_to_fertilizer_list]
    soil_to_fertilizer_list = [[int(num) for num in sub_list] for sub_list in soil_to_fertilizer_list]
    
    # Fertilizer to Water Map
    fertilizer_to_water_header, fertilizer_to_water_line = sections[3].strip().split(':')
    fertilizer_to_water_list = fertilizer_to_water_line.strip().split('\n')
    fertilizer_to_water_list = [line.split(' ') for line in fertilizer_to_water_list]
    fertilizer_to_water_list = [[int(num) for num in sub_list] for sub_list in fertilizer_to_water_list]
    
    # Water to Light Map
    water_to_light_header, water_to_light_line = sections[4].strip().split(':')
    water_to_light_list = water_to_light_line.strip().split('\n')
    water_to_light_list = [line.split(' ') for line in water_to_light_list]
    water_to_light_list = [[int(num) for num in sub_list] for sub_list in water_to_light_list]
    
    # Light to Temperature Map
    light_to_temperature_header, light_to_temperature_line = sections[5].strip().split(':')
    light_to_temperature_list = light_to_temperature_line.strip().split('\n')
    light_to_temperature_list = [line.split(' ') for line in light_to_temperature_list]
    light_to_temperature_list = [[int(num) for num in sub_list] for sub_list in light_to_temperature_list]
    
    # Temperature to Humidity Map
    temperature_to_humidity_header, temperature_to_humidity_line = sections[6].strip().split(':')
    temperature_to_humidity_list = temperature_to_humidity_line.strip().split('\n')
    temperature_to_humidity_list = [line.split(' ') for line in temperature_to_humidity_list]
    temperature_to_humidity_list = [[int(num) for num in sub_list] for sub_list in temperature_to_humidity_list]
    
    # Humidity to Location Map
    humidity_to_location_header, humidity_to_location_line = sections[7].strip().split(':')
    humidity_to_location_list = humidity_to_location_line.strip().split('\n')
    humidity_to_location_list = [line.split(' ') for line in humidity_to_location_list]
    humidity_to_location_list = [[int(num) for num in sub_list] for sub_list in humidity_to_location_list]
    
    locations = []
    for seed in seeds_list:
        soil = next_mapping(seed_to_soil_list, seed)
        fertilizer = next_mapping(soil_to_fertilizer_list, soil)
        water = next_mapping(fertilizer_to_water_list, fertilizer)
        light = next_mapping(water_to_light_list, water)
        temperature = next_mapping(light_to_temperature_list, light)
        humidity = next_mapping(temperature_to_humidity_list, temperature)
        location = next_mapping(humidity_to_location_list, humidity)
        locations.append(location)
    
    print(min(locations))
# %%

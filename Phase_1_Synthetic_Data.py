import numpy as np
import random

#Gives the sets of rules that the luggage should meet
LUGGAGE_SIZE_RANGE = [(40, 30, 15), (55, 40, 23)]  # (L, W, H) in cm
LUGGAGE_WEIGHT_RANGE = (2, 12)  # kg

# Simulation 
def generate_luggage(num_items):
    luggage_data = []
    for _ in range(num_items):
        length = random.randint(LUGGAGE_SIZE_RANGE[0][0], LUGGAGE_SIZE_RANGE[1][0])
        width = random.randint(LUGGAGE_SIZE_RANGE[0][1], LUGGAGE_SIZE_RANGE[1][1])
        height = random.randint(LUGGAGE_SIZE_RANGE[0][2], LUGGAGE_SIZE_RANGE[1][2])
        weight = round(random.uniform(LUGGAGE_WEIGHT_RANGE[0], LUGGAGE_WEIGHT_RANGE[1]), 2)
        luggage_data.append((length, width, height, weight))
    return luggage_data

#Generates amount of luggage you want 
luggage_items = generate_luggage(15)
for item in luggage_items:
    print(f"Dimensions: {item[0]}x{item[1]}x{item[2]} cm, Weight: {item[3]} kg")

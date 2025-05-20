import random

# Define parameters for luggage size and weight based on Airbus A320
LUGGAGE_SIZE_RANGE = [(40, 30, 15), (55, 40, 23)]  # (L, W, H) in cm (Personal item and Cabin bag sizes)
LUGGAGE_WEIGHT_RANGE = (7, 12)  # kg for carry-ons

# Simulate luggage data
def generate_luggage(num_items):
    luggage_data = []
    for _ in range(num_items):
        length = random.randint(LUGGAGE_SIZE_RANGE[0][0], LUGGAGE_SIZE_RANGE[1][0])
        width = random.randint(LUGGAGE_SIZE_RANGE[0][1], LUGGAGE_SIZE_RANGE[1][1])
        height = random.randint(LUGGAGE_SIZE_RANGE[0][2], LUGGAGE_SIZE_RANGE[1][2])
        weight = round(random.uniform(LUGGAGE_WEIGHT_RANGE[0], LUGGAGE_WEIGHT_RANGE[1]), 2)
        luggage_data.append((length, width, height, weight))
    return luggage_data

# Define the First Fit Decreasing (FFD) bin packing algorithm
def first_fit_decreasing(luggage_data, bin_capacity, num_bins):
    # Sort luggage by volume (L * W * H) in descending order
    luggage_data = sorted(luggage_data, key=lambda x: x[0] * x[1] * x[2], reverse=True)

    bins = [[] for _ in range(num_bins)] 
    
    # Iterate through each luggage item and try to fit it into the bins
    for item in luggage_data:
        item_volume = item[0] * item[1] * item[2]
        item_weight = item[3]
        
        placed = False
        
        for bin in bins:
            #This checks if the item can fit the bin 
            total_volume = sum(i[0] * i[1] * i[2] for i in bin)
            total_weight = sum(i[3] for i in bin)
            
            if total_volume + item_volume <= bin_capacity[0] and total_weight + item_weight <= bin_capacity[1]:
                #Places item in bin 
                bin.append(item)
                placed = True
                break
        
        if not placed:
            # If no bin could fit the item, check the next available bin or stop if out of bins
            for bin in bins:
                if len(bin) == 0:  # Empty bin
                    bin.append(item)
                    placed = True
                    break

    return bins

#Generate luggage 
luggage_items = generate_luggage(20)

# Define bin capacity (volume in cubic cm, weight in kg)
#Bin dimensions: 230cm (Width) x 95cm (Depth) x 70cm (Height)
bin_capacity = (230 * 95 * 70, 50)  # Bin capacity is volume and a maximum weight limit

# Specify the number of bins you want to use
num_bins = 12 


bins = first_fit_decreasing(luggage_items, bin_capacity, num_bins)

#Prints the results of the dimensions and Weight of each item in each bin
for i, bin in enumerate(bins):
    print(f"Bin {i+1}:")
    if len(bin) == 0:
        print("  (Empty bin)")
    else:
        for item in bin:
            length, width, height, weight = item
            print(f"  Dimensions: {length}x{width}x{height} cm, Weight: {weight} kg")

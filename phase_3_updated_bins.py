import random

#luggage size and weight based on the Airbus A320
LUGGAGE_SIZE_RANGE = [(40, 30, 15), (55, 40, 23)]  # (L, W, H) in cm 
LUGGAGE_WEIGHT_RANGE = (7, 12)  

# Simulates all the luggage data 
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
def first_fit_decreasing(luggage_data, bin_capacity):
    # Sort luggage by volume (L * W * H) in descending order
    luggage_data = sorted(luggage_data, key=lambda x: x[0] * x[1] * x[2], reverse=True)

    bins = []  # List to hold bins (each bin is a list of items it contains)
    
    # Iterate through each luggage item and try to fit it into the bins
    for item in luggage_data:
        item_volume = item[0] * item[1] * item[2]
        item_weight = item[3]
        
        placed = False
        
        for bin in bins:
            # Check if this bin can fit the item
            total_volume = sum(i[0] * i[1] * i[2] for i in bin)
            total_weight = sum(i[3] for i in bin)
            
            if total_volume + item_volume <= bin_capacity[0] and total_weight + item_weight <= bin_capacity[1]:
                # Place the item in this bin
                bin.append(item)
                placed = True
                break
        
        if not placed:
            # If no bin could fit the item, create a new bin
            bins.append([item])

    return bins

# Generate 20 luggage items as an example
luggage_items = generate_luggage(376)

# Define bin capacity 
bin_capacity = (230 * 95 * 70, 50)  

# Run the bin packing algorithm
bins = first_fit_decreasing(luggage_items, bin_capacity)


for i, bin in enumerate(bins):
    print(f"Bin {i+1}:")
    for item in bin:
        print(f"  Dimensions: {item[0]}x{item[1]}x{item[2]} cm, Weight: {item[3]} kg")

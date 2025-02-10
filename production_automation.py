import time
import random
import pandas as pd

# Input: Basic production setup
def get_production_details():
    print("Welcome to the Production Process Automation System!")
    try:
        units = int(input("Enter the number of units to produce: "))
        speed = float(input("Enter production speed (units per second): "))
        return units, speed
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return get_production_details()

# Stage 1: Raw Material Processing
def raw_material_processing(units):
    print("Processing raw materials...")
    time.sleep(1)
    return units

# Stage 2: Manufacturing
def manufacturing(units, speed):
    print("Manufacturing in progress...")
    time.sleep(units / speed)
    return units

# Stage 3: Quality Check
def quality_check(units):
    print("Performing quality check...")
    defective_items = random.randint(0, units // 10)
    good_units = units - defective_items
    print(f"Defective units: {defective_items}")
    return good_units, defective_items

# Generate Report
def generate_report(total_units, good_units, defective_units, time_taken):
    data = {
        "Total Units": [total_units],
        "Good Units": [good_units],
        "Defective Units": [defective_units],
        "Time Taken (s)": [time_taken]
    }
    report = pd.DataFrame(data)
    print("\nProduction Report:")
    print(report)

# Main Function
def automate_production():
    total_units, speed = get_production_details()
    start_time = time.time()

    raw_units = raw_material_processing(total_units)
    manufactured_units = manufacturing(raw_units, speed)
    good_units, defective_units = quality_check(manufactured_units)

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    generate_report(total_units, good_units, defective_units, time_taken)

# Run the program
if __name__ == "__main__":
    automate_production()

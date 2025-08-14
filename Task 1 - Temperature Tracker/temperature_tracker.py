# temperature_tracker.py
# Hassaan Ahmed - Certura Internship Task 1

def get_temperatures():
    print("Enter daily temperatures for the week (7 values):")
    temps = []
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Day {i + 1}: "))
                temps.append(temp)
                break
            except ValueError:
                print("Please enter a valid number.")
    return temps

def calculate_average(temps):
    return sum(temps) / len(temps)

def get_max_temperature(temps):
    return max(temps)

def get_min_temperature(temps):
    return min(temps)

def display_statistics(temps):
    print("\n--- Weekly Temperature Stats ---")
    print(f"Temperatures: {temps}")
    print(f"Average Temperature: {calculate_average(temps):.2f}°C")
    print(f"Maximum Temperature: {get_max_temperature(temps):.2f}°C")
    print(f"Minimum Temperature: {get_min_temperature(temps):.2f}°C")
    print("--------------------------------")


temperatures = get_temperatures()
display_statistics(temperatures)
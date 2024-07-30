# Sample data for a week

weather_data = [
    {"date": "2024-07-22", "max_temp": 35, "min_temp": 25, "humidity": 80},
    {"date": "2024-07-23", "max_temp": 32, "min_temp": 24, "humidity": 70},
    {"date": "2024-07-24", "max_temp": 30, "min_temp": 22, "humidity": 65},
    {"date": "2024-07-25", "max_temp": 28, "min_temp": 21, "humidity": 60},
    {"date": "2024-07-26", "max_temp": 33, "min_temp": 23, "humidity": 75},
    {"date": "2024-07-27", "max_temp": 36, "min_temp": 26, "humidity": 85},
    {"date": "2024-07-28", "max_temp": 34, "min_temp": 24, "humidity": 77}
]

# Function to find the highest and lowest temperatures recorded during the week
def find_extreme_temperatures(data):
    max_temp = max(day['max_temp'] for day in data)
    min_temp = min(day['min_temp'] for day in data)
    return max_temp, min_temp

# Function to determine the number of days with temperatures above 30°C
def count_days_above_30(data):
    count = sum(1 for day in data if day['max_temp'] > 30)
    return count

# Function to compute the average humidity over the specified period
def average_humidity(data):
    total_humidity = sum(day['humidity'] for day in data)
    average = total_humidity / len(data)
    return average

# Main
highest_temp, lowest_temp = find_extreme_temperatures(weather_data)
days_above_30 = count_days_above_30(weather_data)
avg_humidity = average_humidity(weather_data)

print(f"Highest Temperature: {highest_temp}°C")
print(f"Lowest Temperature: {lowest_temp}°C")
print(f"Number of days above 30°C: {days_above_30}")
print(f"Average Humidity: {avg_humidity:.2f}%")
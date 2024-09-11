import json
import datetime


ONE_MILE_IN_METERS = 1609.34

# Open and load the JSON file
with open('Activity.json', 'r') as file:
    data = json.load(file) 


# Task 1: Print total distance, in miles
    # Extract the distances in meters from JSON
    # Calculate total distance in meters
    # Convert meters to miles. 1 mile = 1609.34 meters
    # Print the total distance 

def get_total_distance_in_miles(data):
    distance_in_meters = data['distance']['data'][-1]
    distance_in_miles = round(distance_in_meters / ONE_MILE_IN_METERS, 2)
    return distance_in_miles

# print(f"Total distance in miles: {get_total_distance_in_miles(data)} miles")


# Task 2: Print mile splits for each mile, in minute:second format (e.g. “6:09”)
    # Time format conversion
    # extract data for distance and time from JSON
    # init results to store mile splits
    # init a variable to keep track of the current mile, starts at 1
    # init a variable to keep track of where the last mile ended, set to 0
    # iterate through the disatnce data
    # check if the mile is completed
        # calc the time it was completed by subtracting from where the last mile ended
        # format the time 
        # add it to results
        # increment the current mile so it can calculate the next 
        # update the previous mile, so it becomes the next starting point
    

# Function to convert time in seconds to min:sec format
def format_time(seconds):
    return str(datetime.timedelta(seconds=seconds))


def get_mile_splits(data):
    distance_data = data['distance']['data'] # distance in meters
    time_data = data['time']['data'] # time in seconds

    result = []
    current_mile = 1
    prev_mile = 0

    for i, distance in enumerate(distance_data):
        if distance >= current_mile * ONE_MILE_IN_METERS:
            time_for_mile = time_data[i] - time_data[prev_mile]
            split_time = format_time(time_for_mile)
            result.append(split_time)

            current_mile += 1
            prev_mile = i

    return result

# print(get_mile_splits(data))


output = {
    "total_distance_miles": get_total_distance_in_miles(data),
    "mile_splits": get_mile_splits(data)
}

# Convert the combined dictionary to a JSON string with indentation for readability
json_output = json.dumps(output, indent=4)

# Print the JSON output
print(json_output)


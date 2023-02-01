from flask import (
    Flask, jsonify,abort
)
# Calculate velocity using distance/time
def calculate_velocity(distance,time):
    int_distance, int_time = verify_type_of_data(distance,time)
    print(type(int_distance),type(int_time))
    return int_distance*int_time

# Transform values of query params in int values
def verify_type_of_data(distance,time): 
    try:
        distance = float(distance)
        time = float(time)
    except :
        abort(404)
    return distance,time
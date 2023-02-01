from flask import (
    Flask, jsonify,request
)
from Services.calculate_distance import *

app = Flask("application")

# Define error when status code is 404 
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error_message":"This page doesn't exist"}),404

# Define error when status code is 500
@app.errorhandler(500)
def page_not_found(error):
    return jsonify({"error_message":"This time cant'n be zero in divisor"}),500

# Home route to 
@app.route('/',methods=['GET'])
def index():
    return jsonify({"status":"API is up","version":"3"})

@app.route('/api/speed',methods=['GET'])
def getDistance():
    # Get data of query params
    time = request.args.get('time')
    distance = request.args.get('distance')
    
    if (time == None):
        return jsonify({"error_message":"The parameter 'time' is required"}),400 
    if (distance == None):
        return jsonify({"error_message":"The parameter 'distance' is required"}),400 

    velocity = calculate_velocity(distance,time)
   
    return jsonify({"speed":"{:.2f}m/s".format(velocity)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


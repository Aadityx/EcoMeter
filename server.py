from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

TRIPS_FILE = "trips.json"

def load_trips():
    if os.path.exists(TRIPS_FILE):
        with open(TRIPS_FILE, "r") as file:
            return json.load(file)
    return []

def save_trips(trips):
    with open(TRIPS_FILE, "w") as file:
        json.dump(trips, file, indent=4)

@app.route("/record_trip", methods=["POST"])
def record_trip():
    trip_data = request.json
    trips = load_trips()
    trips.append(trip_data)
    save_trips(trips)
    return jsonify({"message": "Trip recorded successfully!"}), 200

@app.route("/get_trips", methods=["GET"])
def get_trips():
    trips = load_trips()
    return jsonify(trips)

if __name__ == "__main__":
    app.run(debug=True)

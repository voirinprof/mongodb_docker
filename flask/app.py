from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import json_util
import os
import json

app = Flask(__name__)

client = MongoClient(os.environ.get('MONGO_URI'))
db = client.spatial_db

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = list(db.locations.find())
    return jsonify(json.loads(json_util.dumps(locations)))

@app.route('/locations/near', methods=['GET'])
def get_nearby_locations():
    try:
        lon = float(request.args.get('lon'))
        lat = float(request.args.get('lat'))
        max_distance = float(request.args.get('max_distance', 1000))  # meters
        
        locations = list(db.locations.find({
            "location": {
                "$near": {
                    "$geometry": {
                        "type": "Point",
                        "coordinates": [lon, lat]
                    },
                    "$maxDistance": max_distance
                }
            }
        }))
        return jsonify(json.loads(json_util.dumps(locations)))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
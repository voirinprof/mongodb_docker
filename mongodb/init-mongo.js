db = db.getSiblingDB('spatial_db');
db.createCollection('locations');
db.locations.createIndex({ location: "2dsphere" });
db.locations.insertMany([
    {
        name: "Central Park",
        location: {
            type: "Point",
            coordinates: [-73.965355, 40.782865]
        }
    },
    {
        name: "Times Square",
        location: {
            type: "Point",
            coordinates: [-73.985130, 40.758896]
        }
    }
]);
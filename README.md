# Ammo API Documentation

This API allows you to retrieve, add, update, and delete ammo types and their stats.

## Endpoints

### Get All Ammo Types and Stats

#### GET /ammo

This endpoint retrieves all available ammo types and their stats.

##### Example Request

GET http://localhost:5000/ammo

shell


##### Example Response

{
"5.45x39mm": {
"7N39 'Igolnik'": {
"penetration": 62,
"damage": 37,
"armor_damage": 68
},
"BS": {
"penetration": 50,
"damage": 40,
"armor_damage": 48
},
"BT": {
"penetration": 37,
"damage": 40,
"armor_damage": 44
}
},
"5.56x45mm": {
"M995": {
"penetration": 53,
"damage": 40,
"armor_damage": 68
},
"M855A1": {
"penetration": 37,
"damage": 40,
"armor_damage": 44
}
},
"7.62x51mm": {
"M61": {
"penetration": 68,
"damage": 80,
"armor_damage": 70
},
"M62": {
"penetration": 58,
"damage": 79,
"armor_damage": 56
}
}
}

shell


### Get Specific Ammo Type Stats

#### GET /ammo/{caliber}/{ammo_type}

This endpoint retrieves the stats of a specific ammo type.

##### Example Request

GET http://localhost:5000/ammo/5.56x45mm/M995

shell


##### Example Response

{
"penetration": 53,
"damage": 40,
"armor_damage": 68
}

shell


### Add New Ammo Type

#### POST /ammo

This endpoint adds a new ammo type to the dataset.

##### Example Request

POST http://localhost:5000/ammo
Content-Type: application/json

{
"caliber": "9x19mm",
"ammo_type": "AP 6.3",
"penetration": 30,
"damage": 70,
"armor_damage": 20
}

shell


##### Example Response

{
"message": "Ammo type added successfully."
}

shell


### Update Ammo Type Stats

#### PUT /ammo/{caliber}/{ammo_type}

This endpoint updates the stats of an existing ammo type.

##### Example Request

PUT http://localhost:5000/ammo/5.56x45mm/M995
Content-Type: application/json

{
"penetration": 60,
"damage": 35,
"armor_damage": 60
}

shell


##### Example Response

{
"message": "Ammo type updated successfully."
}

shell


### Delete Ammo Type

#### DELETE /ammo/{caliber}/{ammo_type}

This endpoint deletes an existing ammo type.

##### Example Request

DELETE http://localhost:5000/ammo/5.56x45mm/M995

shell


##### Example Response

{
"message": "Ammo type deleted successfully."
}

shell


## Additional Information

### Firebase Database

This API uses the Firebase Realtime Database to store and retrieve ammo types and their stats.

### Required Fields
Required Fields for Adding or Updating Ammo Type

When adding or updating an ammo type, the following fields are required:

    caliber: The caliber of the ammo type, e.g. "5.56x45mm"
    ammo_type: The name of the ammo type, e.g. "M995"
    penetration: The penetration value of the ammo type
    damage: The damage value of the ammo type
    armor_damage: The armor damage value of the ammo type
    
### Error Responses

The API returns the following error responses:

    400 Bad Request: The request was invalid or missing required fields.
    404 Not Found: The requested resource was not found.
    500 Internal Server Error: The server encountered an error while processing the request.
    
### Authentication

Authentication is not required to access the Ammo API endpoints.

### Rate Limiting

There is no rate limiting currently implemented for this API.

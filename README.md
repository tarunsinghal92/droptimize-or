# Droptimize OR API

Steps to run the service -

1. Clone the Repository - git clone https://github.com/tarunsinghal92/droptimize-or.git

2. Move to the directory - cd src

3. pip install cryptography && pip install pipenv && pipenv install

4. Navigate to http://0.0.0.0:5000/ to get started

#### Routes

```
POST /v1/api

Body 
{
  "data": {
      "deliveries": [
          {
              "location_id": "A",
              "address": "181 Dundas St East, Toronto",
              "quantity": 5
          },
          {
              "location_id": "B",
              "address": "83 Lilian Drive, Scarborough",
              "quantity": 8
          },
          {
              "location_id": "C",
              "address": "57 Medway Cres, Scarborough",
              "quantity": 12
          }
      ],
      "depot": {
          "location_id": "O",
          "address": "220 Yonge St, Toronto, ON M5B 2H1, Canada",
          "vehicle_capacity": 15
      }
  }
}

```

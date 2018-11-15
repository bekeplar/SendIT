# Project Overview
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.


[![Build Status](https://travis-ci.org/bekeplar/SendIT.svg?branch=ft-user-cancel-parcel)](https://travis-ci.org/bekeplar/SendIT)
[![Coverage Status](https://coveralls.io/repos/github/bekeplar/SendIT/badge.svg?branch=ft-user-cancel-parcel)](https://coveralls.io/github/bekeplar/SendIT?branch=ft-user-cancel-parcel)

### Required Features
- User can signup

- User can login

- Create a parcel delivery order

- Get all parcel delivery orders

- Get a specific parcel delivery order

- Cancel a parcel delivery order

- Fetch all parcel delivery orders by a specific user

### Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/orders|Create a parcel
GET|api/v1/orders|Fetch all parcel orders
GET|api/v1/orders|Fetch a specific parcel order
PUT|api/v1/orders/<int:id>|Cancel a specific parcel order
GET|api/v1/users/<int:id>|Fetch all parcels by userid

### Requirements

- Python
- Flask
- Virtualenv
- Postman

### Getting started
* Clone the project to your local machine
```
git clone https://github.com/bekeplar/SendIT.git
```
* Change to the cloned directory
```
cd SendIT
pip install virtualenv
source venv/bin/activate
git checkout ft-api
pip install -r requirements.txt
python run.py
```
* For those on windows
```
cd SendIT
pip install virtualenv
venv\Scripts\activate
git checkout ft-api
pip install -r requirements.txt
python run.py
```
* Run tests by
```
pip install pytest
pytest

```

## Authors:
Bekalaze Joseph

### Courtesy of :
Andela Bootcamp 14


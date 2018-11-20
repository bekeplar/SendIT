# Project Overview
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.


[![Build Status](https://travis-ci.org/bekeplar/SendIT.svg?branch=ft-user-cancel-parcel)](https://travis-ci.org/bekeplar/SendIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/3572e2c0da5d9b0127e5/maintainability)](https://codeclimate.com/github/bekeplar/SendIT/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/bekeplar/SendIT/badge.svg?branch=ft-get-user)](https://coveralls.io/github/bekeplar/SendIT?branch=ft-get-user)

### Required Features
- User can signup

- User can login

- Create a parcel delivery order

- Get all parcel delivery orders

- Get a specific parcel delivery order

- Cancel a parcel delivery order

- Fetch all parcel delivery orders by a specific user

- The user can change the destination of a parcel delivery order.

- Admin can view all parcel delivery orders in the application.

- Admin can change the status of a parcel delivery order.



### Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/orders|Create a parcel
GET|api/v1/orders|Fetch all parcel orders
GET|api/v1/orders|Fetch a specific parcel order
PUT|api/v1/orders/<int:id>|Cancel a specific parcel order
GET|api/v1/users/<int:id>|Fetch all parcels by userid
POST|api/auth/login|Login a user
POST|api/auth/signup|create a user
PUT|api/v1/orders/<parcelId>/status|Change the status of a specific parcel
PUT|api/v1/orders/<parcelId>/destination|Change the location of a specific parcel
PUT|api/v1/orders/<parcelId>/PresentLocation|Change the present location parcel




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
* Testing Endpoints
```
copy the url in the terminal
paste it in postman
Use the following sample data
orders = [
    {
        'destination': 'Mukono',
        'date': '23-11-2018',
        'Pickup_location': 'Nakawa',
        'price': 80000,
        'weight': 75,
        'name': 'Bekalaze',
        'id': 1
    }
]

```


## Authors:
Bekalaze Joseph

### Courtesy of :
Andela Bootcamp 14


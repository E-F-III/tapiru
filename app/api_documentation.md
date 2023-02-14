# API Documentation

## FEATURE 0: USER AUTHORIZATION

### All endpoints that require authentication

All endpoints that require a current user to be logged in.

- Request: endpoints that require authentication
- Error Response: Require authentication

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Authentication required",
      "statusCode": 401
    }
    ```

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

- Request: endpoints that require proper authorization
- Error Response: Require proper authorization

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Forbidden",
      "statusCode": 403
    }
    ```

### Get the Current User

Returns information about the current user that is logged in.

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/session
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "username": "jsmith",
      "email": "john.smith@gmail.com",
    }
    ```

### Log In a User

Logs in a current user with valid credentials and returns the current user's
information.

- Require Authentication: false
- Request

  - Method: POST
  - URL: /api/session
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "email": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "username": "jsmith",
      "email": "john.smith@gmail.com",
      "token": ""
    }
    ```

- Error Response: Invalid credentials

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Invalid credentials",
      "statusCode": 401
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "email": "Email is required",
        "password": "Password is required"
      }
    }
    ```

### Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

- Require Authentication: false
- Request

  - Method: /POST
  - URL: /api/users
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "username": "jsmith"
      "email": "john.smith@gmail.com",
      "password": "secret password",
      "is_business": true
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "username": "jsmith"
      "email": "john.smith@gmail.com",
      "is_business": true,
      "token": ""
    }
    ```

- Error response: User already exists with the specified email

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "User already exists",
      "statusCode": 403,
      "errors": {
        "email": "User with that email already exists",
        "username": "User with that username already exists"
      }
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "email": "Invalid email",
        "username": "Invalid username"
      }
    }
    ```

## FEATURE 1: BUSINESSES

### Create a business

- Require Authentication: true
- Request

  - Method: /POST
  - URL: /api/businesses
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "owner": 1,
      "name": "business name",
      "logo": "img.png",
      "street_address": "123 Street",
      "city": "City",
      "region": "Region",
      "postcode": "12345",
      "country": "Country",
      "website": "www.website.com",
      "phone": "123-456-7890",
      "timezone": "America/New_York",
      "currency": "USD",
      "about_location": "About location",
      "payment_types": ["cash", "card"]
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "owner": 1,
      "name": "business name",
      "logo": "img.png",
      "street_address": "123 Street",
      "city": "City",
      "region": "Region",
      "postcode": "12345",
      "country": "Country",
      "website": "www.website.com",
      "phone": "123-456-7890",
      "timezone": "America/New_York",
      "currency": "USD",
      "about_location": "About location",
      "payment_types": ["cash", "card"]
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "name": "Invalid name",
        "logo": "Invalid logo",
        "street_address": "Invalid street address",
        "city": "Invalid city",
        "region": "Invalid region",
        "postcode": "Invalid postcode",
        "country": "Invalid country",
        "website": "Invalid website",
        "phone": "Invalid phone",
        "timezone": "Invalid timezone",
        "currency": "Invalid currency",
        "about_location": "Invalid about location",
        "payment_types": "Payment types must be of the following: "
      }
    }
    ```

### Get business by id

Returns information about a business by id

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/businesses/:id
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "owner": 1,
      "name": "business name",
      "logo": "img.png",
      "street_address": "123 Street",
      "city": "City",
      "region": "Region",
      "postcode": "12345",
      "country": "Country",
      "website": "www.website.com",
      "phone": "123-456-7890",
      "timezone": "America/New_York",
      "currency": "USD",
      "about_location": "About location",
      "payment_types": ["cash", "card"]
    }
    ```

## Update business by id

Update business data by id

- Require Authentication: true
- Require proper authorization: Business must belong to the current user
- Request

  - Method: /PUT
  - URL: /api/businesses
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "owner": 1,
      "name": "business name",
      "logo": "img.png",
      "street_address": "123 Street",
      "city": "City",
      "region": "Region",
      "postcode": "12345",
      "country": "Country",
      "website": "www.website.com",
      "phone": "123-456-7890",
      "timezone": "America/New_York",
      "currency": "USD",
      "about_location": "About location",
      "payment_types": ["cash", "card"]
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "owner": 1,
      "name": "business name",
      "logo": "img.png",
      "street_address": "123 Street",
      "city": "City",
      "region": "Region",
      "postcode": "12345",
      "country": "Country",
      "website": "www.website.com",
      "phone": "123-456-7890",
      "timezone": "America/New_York",
      "currency": "USD",
      "about_location": "About location",
      "payment_types": ["cash", "card"]
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "name": "Invalid name",
        "logo": "Invalid logo",
        "street_address": "Invalid street address",
        "city": "Invalid city",
        "region": "Invalid region",
        "postcode": "Invalid postcode",
        "country": "Invalid country",
        "website": "Invalid website",
        "phone": "Invalid phone",
        "timezone": "Invalid timezone",
        "currency": "Invalid currency",
        "about_location": "Invalid about location",
        "payment_types": "Payment types must be of the following: "
      }
    }
    ```
- Error response: Couldn't find business with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Business could not be found",
        "statusCode": 404
    }

## Delete business by id

Delete a business by id

- Require Authentication: true
- Require proper authorization: Business must belong to the current user
- Request

  - Method: /DELETE
  - URL: /api/businesses/:id
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Business deleted"
    }
    ```

- Error response: Business not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Business not found",
      "statusCode": 404
    }
    ```

### FEATURE 2: MENUS

### Create menu

Create a menu for a business

- Require Authentication: true
- Require proper authorization: Business must belong to the current user
- Request

  - Method: POST
  - URL: /api/business/:businessId/menus
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "name": "Menu name",
      "description": "Menu description",
      "active": true
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "business_id": 1,
      "name": "Menu name",
      "description": "Menu description",
      "active": true
    }
    ```
- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "name": "Invalid name",
        "description": "Description required"
      },
      "active": "expected a boolean"
    }
    ```

- Error response: Couldn't find business with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Business could not be found",
        "statusCode": 404
    }
    ```

### Get menu by id

Returns information about a menu by id

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/menus/:menuId
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "business_id": 1,
      "name": "Menu name",
      "description": "Menu description",
      "active": true
    }
    ```
- Error response: Couldn't find a menu with the specified id

  - Status Code: 404

  - Headers:
    - Content-Type: application/json
  - Body:
    ```json
    {
        "message": "Business could not be found",
        "statusCode": 404
    }
    ```

### Get menus of a business

Returns information about all menus of a business

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/businesses/:businessId/menus
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    [
      {
        "id": 1,
        "business_id": 1,
        "name": "Menu name",
        "description": "Menu description",
        "active": true
      },
      {
        "id": 2,
        "business_id": 1,
        "name": "Menu name 2",
        "description": "Menu description 2",
        "active": true
      }
    ]
    ```

- Error response: Couldn't find business with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Business could not be found",
        "statusCode": 404
    }
    ```

### Update menu by id

Update menu data by id

- Require Authentication: true
- Require proper authorization: Menu must be owned a business created by the current user
- Request

  - Method: /PUT
  - URL: /api/menus/:menuId
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "name": "Menu name",
      "description": "Menu description",
      "active": true
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "business_id": 1,
      "name": "Menu name",
      "description": "Menu description",
      "active": true
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "name": "Invalid name",
        "description": "Invalid description",
        "active": "Invalid active"
      }
    }
    ```

- Error response: Couldn't find menu with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Business could not be found",
        "statusCode": 404
    }
    ```

### Delete menu by id

Delete a menu by id

- Require Authentication: true
- Request

  - Method: /DELETE
  - URL: /api/businesses/:businessId/menus/:menuId
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Menu deleted"
    }
    ```

- Error response: Menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Menu not found",
      "statusCode": 404
    }
    ```

### FEATURE 3: ITEMS

### Create item for a menu

Create an item for a menu

- Require Authentication: true
- Request

  - Method: POST
  - URL: /api/menus/:menuId/items
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "name": "Item name",
      "description": "Item description",
      "prices": {
        "8oz": 5.99,
        "12oz": 6.99,
        "16oz": 7.99
      },
      "type": "Milk Tea",
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "menu_id": 1,
      "name": "Item name",
      "description": "Item description",
      "prices": {
        "8oz": 5.99,
        "12oz": 6.99,
        "16oz": 7.99
      },
      "type": "Milk Tea",
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "name": "Invalid name",
        "description": "Invalid description",
        "prices": "Price/s required",
        "type": "Type must be of the following: "
      }
    }
    ```

- Error response: Couldn't find menu with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Menu could not be found",
        "statusCode": 404
    }
    ```

### Get items of a menu by id

Returns information about all items of a menu

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/menus/:menuId/items
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    [
      {
        "id": 1,
        "menu_id": 1,
        "name": "Item name",
        "description": "Item description",
        "prices": {
          "8oz": 5.99,
          "12oz": 6.99,
          "16oz": 7.99
        },
        "type": "Milk Tea",
      },
      {
        "id": 2,
        "menu_id": 1,
        "name": "Item name 2",
        "description": "Item description 2",
        "prices": {
          "8oz": 5.99,
          "12oz": 6.99,
          "16oz": 7.99
        },
        "type": "Milk Tea",
      }
    ]
    ```
- Error response: Couldn't find menu with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Menu could not be found",
        "statusCode": 404
    }
    ```
### Update item by id

Update item data by id

- Require Authentication: true
- Request

  - Method: /PUT
  - URL: /api/items/:itemId
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "name": "Item name",
      "description": "Item description",
      "prices": {
        "8oz": 5.99,
        "12oz": 6.99,
        "16oz": 7.99
      },
      "type": "Milk Tea",
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "menu_id": 1,
      "name": "Item name",
      "description": "Item description",
      "prices": {
        "8oz": 5.99,
        "12oz": 6.99,
        "16oz": 7.99
      },
      "type": "Milk Tea",
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "name": "Invalid name",
        "description": "Invalid description",
        "prices": "Invalid prices",
        "type": "Invalid type"
      }
    }
    ```

- Error response: Couldn't find item with the specified id

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
        "message": "Item could not be found",
        "statusCode": 404
    }

### Delete item by id

Delete an item by id

- Require Authentication: true
- Request

  - Method: /DELETE
  - URL: /api/items/:itemId
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Item deleted"
    }
    ```

- Error response: Item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Item not found",
      "statusCode": 404
    }
    ```

## FEATURE 4: WISH LIST

### Add item to wishlist

Add an item to a user's wishlist

- Require Authentication: true
- Request

  - Method: POST
  - URL: /api/users/:userId/wishlist
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "item_id": 1
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "user_id": 1,
      "item_id": 1
    }
    ```

- Error response: Item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Item not found",
      "statusCode": 404
    }
    ```

### Get wishlist by user id

Get a user's wishlist by user id

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/users/:userId/wishlists
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    [
      {
        "id": 1,
        "user_id": 1,
        "item_id": 1
      },
      {
        "id": 2,
        "user_id": 1,
        "item_id": 2
      }
    ]
    ```

- Error Response
  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:
    ```json
    {
        "message": "User could not be found",
        "statusCode": 404
    }
    ```

### Delete item from wishlist

Delete an item from a user's wishlist

- Require Authentication: true
- Require proper authorization: Wishlist must belong to the current user
- Request

  - Method: /DELETE
  - URL: /api/users/:userId/wishlists/:wishlistItemId
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Item deleted"
    }
    ```

- Error response: Item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Item not found in the wishlist",
      "statusCode": 404
    }
    ```

## FEATURE 5: CHECK-INS

### Add check-in

- Require Authentication: true
- Request

  - Method: POST
  - URL: /api/users/:userId/checkins
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "item_id": 1,
      "ice_level": "0%",
      "sugar_level": "100%",
      "toppings": ["Boba", "Popping Boba"]
    }
    ```

- Successful Response

  - Status Code: 201
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "user_id": 1,
      "item_id": 1,
      "ice_level": "0%",
      "sugar_level": "100%",
      "toppings": ["Boba", "Popping Boba"],
      "date_created": "2020-01-01T00:00:00.000Z"
    }
    ```

- Error Response: Body validations

### Read users check-ins

Get a user's check-ins by user id

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/users/:userId/checkins
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    [
      {
        "id": 1,
        "user_id": 1,
        "item_id": 1,
        "ice_level": "0%",
        "sugar_level": "100%",
        "toppings": ["Boba", "Popping Boba"],
        "date_created": "2020-01-01T00:00:00.000Z"
      },
      {
        "id": 2,
        "user_id": 1,
        "item_id": 2,
        "ice_level": "0%",
        "sugar_level": "100%",
        "toppings": ["Boba", "Popping Boba"],
        "date_created": "2020-01-01T00:00:00.000Z"
      }
    ]
    ```


### Update a users check-in

Update a user's check-in by check-in id

- Require Authentication: true
- Require proper authorization: Check-in must belong to the current user
- Request

  - Method: PUT
  - URL: /api/checkins/:checkinId
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "ice_level": "0%",
      "sugar_level": "100%",
      "toppings": ["Boba", "Popping Boba"]
    }
    ```

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "id": 1,
      "user_id": 1,
      "item_id": 1,
      "ice_level": "0%",
      "sugar_level": "100%",
      "toppings": ["Boba", "Popping Boba"],
      "date_created": "2020-01-01T00:00:00.000Z",
      "date_modified": "2020-01-01T00:00:00.000Z"
    }
    ```

### Delete a users check-in

Delete a user's check-in by check-in id

- Require Authentication: true
- Require proper authorization: Check-in must belong to the current user
- Request

  - Method: DELETE
  - URL: /api/checkins/:checkinId
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Check-in deleted"
    }
    ```

- Error response: Check-in not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Check-in not found",
      "statusCode": 404
    }
    ```

## FEATURE 6: SEARCH

- A logged in user is able to search for a business by name

### Search for a business

Search for a business by name

- Require Authentication: true
- Request

  - Method: GET
  - URL: /api/businesses/search?
  - Headers:
    - Content-Type: application/json
  - Body: none

- Successful Response

  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    [
      {
        "id": 1,
        "name": "Bobas",
        "address": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
        "phone": "123-456-7890",
        "website": "www.bobas.com"
      },
      {
        "id": 2,
        "name": "Boba Tea",
        "address": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
        "phone": "123-456-7890",
        "website": "www.bobatea.com"
      }
    ]
    ```

# Mock API

ExpressJS server created using the [https://expressjs.com/en/starter/generator.html](Express Generator).

## Usage

`npm install` to install dependencies (NodeJS is required).

`npm start` to start the web server. Runs on port 3000 by default.

The API is found in `/routes/api.js`. The following endpoints and behaviour is currently implemented:

- `/login`: log in
  - If email or password is `LOGIN`, it will return successfully and set the JSESSIONID cookie (although this is not used by any endpoints as of now)
  - Otherwise, it will return a 400 error
- `/users`: registration
  - If email is `used@example.com`, it will return a 409 error
  - If any field is equal to `ERROR`, it will return a 400 error
  - If one of "firstName", "lastName", "email", "dateOfBirth", "homeAddress" or "password" are undefined, it will return a 400 error
  - Otherwise, it will succeed with a 201 code
- `/users/{id}`: get information on a user
  - If the id is 1000, it will return a 401 error (unauthorized)
  - If the id is between 0 and 104 inclusive, it will return a user with all fields (except password) defined in the v1 API specification
    - Calling `/users` adds the user to the user array, so if this has been called, values greater than 104 may return a valid response
  - Otherwise (e.g. id is not an integer), it will return a 405 error

### Using cURL

#### JSON payload

```bash
curl --header "Content-Type: application/json" -i --request POST --data '{"key": "value", ...}' localhost:3000/path
```

Example: for `POST /users`:

```bash
curl --header "Content-Type: application/json" --request POST --data '{"firstName": "FName", "lastName": "LName", "email": "bla@bla.com", "password": "pw", "dateOfBirth": "42", "homeAddress": "bla street"}' -i localhost:3000/api/users
```

#### GET Request

```bash
curl -i localhost:3000/path
```

var express = require('express');
var router = express.Router();

var users = require("./../users");

const SESSION_COOKIE_NAME = "JSESSIONID";
const SESSION_COOKIE_LOGGED_IN = "LOGGED_IN";
const HTTP_ONLY_COOKIE_OPTION = {
  HttpOnly: true
};
Object.freeze(HTTP_ONLY_COOKIE_OPTION);

const ACCOUNT_LOGIN_SUCCESS = "LOGIN";

const ACCOUNT_CREATION_USED_EMAIL = "used@example.com";
const ACCOUNT_CREATION_ERROR = "ERROR";

const GET_USER_ACCOUNT_UNAUTHORIZED = 1000;

/**
 * Returns true if login is successful
 * // TODO
 * @param {*} sessionCookie
 */
// const isLoggedIn = (req) => {}

/**
 * Given an object, checks returns true if one or more values are equal to the passed parameter
 * @param {*} object
 * @param {*} value
 */
const anyValuesEqualTo = (object, value) => Object.values(object).filter(val => val == value).length;


/**
 * Login to user account. Sets cookie if successful
 * For successful, email or password should be set to ACCOUNT_LOGIN_SUCCESS. Cookie is set in this case
 */
router.post("/login", (req, res, next) => {
  const successful = Object.keys(req.body).filter(key => req.body[key] == ACCOUNT_LOGIN_SUCCESS).length > 0;
    console.log(req.body);
  // Iterates through the keys (email, password) and finds the number of keys where the value is equal to ACCOUNT_LOGIN_SUCCESS.

  if (!successful) {
    return res.status(400).send();
  }

  return res.status(200).cookie(
    SESSION_COOKIE_NAME,
    SESSION_COOKIE_LOGGED_IN,
    HTTP_ONLY_COOKIE_OPTION
  ).send();
});


/**
 * Create new account
 * For email already in used, set email to ACCOUNT_CREATION_USED_EMAIL
 * For an error:
 *  - Set any value to ACCOUNT_CREATION_ERROR
 *  - One of "firstName", "lastName", "email", "dateOfBirth", "homeAddress", "password" are not defined
 * Otherwise, will return successfully
 */
router.post("/users", (req, res, next) => {
  const { email } = req.body;

  if (email == ACCOUNT_CREATION_USED_EMAIL) return res.status(409).send();

  else if (anyValuesEqualTo(req.body, ACCOUNT_CREATION_ERROR)) return res.status(400).send();

  for(let mandatoryKey of ["firstName", "lastName", "email", "dateOfBirth", "homeAddress", "password"]) {
    if (req.body[mandatoryKey] == "undefined") {
      return res.status(400).send();
    }
  }

  let id = 0;
  if (users.length != 0) id = users[users.length - 1].id + 1;

  users.push({
    ...req.body,
    id
  });

  return res.status(201).send();
});


/**
 * Get info on a account
 * For NotAcceptableError, pass a non-integer or a number greater than or equal to 105 (number of mock users in the JSON file. NB: POST /users adds the user to the array, so it may be useful to use a very large number)
 * For a UnauthorizedError, pass GET_USER_ACCOUNT_UNAUTHORIZED as the ID
 * TODO does not check cookies at all
 */
router.get("/users/:id", (req, res, next) => {
  let id = -1;
  try {
    id = parseInt(req.params.id, 10);
  } catch(err) {
    // NotAcceptableError
    return res.status(405).send();
  }
  if (id == GET_USER_ACCOUNT_UNAUTHORIZED) {
    return res.status(401).send();
  }

  const user = users.find(el => el.id == id);
  if (user == undefined) return res.status(405).send();

  return res.status(200).json(user);
});

module.exports = router;

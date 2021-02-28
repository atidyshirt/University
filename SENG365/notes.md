> [TOC]

# Web Computing Architecture

### Course Information

### Grading Structure

### Lectures

#### Lecture One: Introduction to HTTP and JavaScript

**What is a web application?**

- Uses `HTTP` server to interact
- Runs in a web-browser
- Generally interacts with a server back-end

We will be using a restful approach to building our JavaScript web application's.

**Here is how we will structure a web-app**

![structure](./Diagrams/structure-webapp.png)

In _Assignment One_ we will need to do the following

- Create `HTTP` server + application
- `HTTP` requests and response cycle
- `URL` e.g. protocol, path, endpoints, query parameters
- `HTTP` headers and body
  - Headers: e.g. using Cookies
  - Headers: e.g. `CORS`
  - Body e.g. `JSON` data
- `HTTP` methods e.g. `GET, PUT, DELETE`
- `HTTP` status codes e.g. `201`, `404`
- Authentication and authorization
- Asynchronous requests
- Database connectivity
- Conform to `API` specification
  - You will be given an `API` specification to implement

> NOTE: When we do the assignment we will all be assigned a port number to connect to on the test server

In _Assignment Two_ we will need to do the following

**HTTP Client**

- `HTML` + `CSS` + `JS` app
- Modern browser
- Implementing user story backlog
- Authentication and authorization
- Asynchronous requests
- `RESTful API` calls

`HTTP` messages are how data is exchanged between the server and the client, there are two types of
messages: _requests_ sent by the client to trigger a _response_ from the server.

`HTTP` messages are composed of a textual information encoded in `ASCII`, and span over multiple
lines. In `HTTP/1.1` and earlier versions of the protocol, these messages were **openly** sent across
the connection.

**Uniform Resource Identifiers (URI's)**

- A string of characters to identify (name, or name and location) resource.
- A `URL` is a `URI` that also specifies the means of acting upon or obtaining representation
- A `URN` is a historic `URI` term that has since been depreciated

- The `HTML` path is increasingly becoming an abstraction as unlike an `HTML` path, the ever more growing
  language `JavaScript` does not show the local path, and instead uses a server to generate the html that
  is being used to pass parameter calls for functions, id numbers, versioning information etc.

**Anchors**

- Anchors are used as bookmarks within a classic `HTML` file.

> NOTE: There are many `JS` libraries to achieve the above functionality, we will mostly be implementing
> these libraries rather than building this functionality from scratch.

As well as the `URL`, there are `HTTP` headers:

- General headers: required and additional
- Entity headers: applies to the body of the request
- Request headers
- Response headers
- Cookies are implemented within the header using `set-cookie: <...>`

We use headers and cookies in order to:

- Maintain session
- Personalise
- Track data (e.g. advertising)

**Header structures**

**Structure and example of `HTTP` requests**

`HTTP` request form:

```
HTTP-method SP Request-URL SP HTTP-Version CRLF

Request body...
```

**Example GET request**

```
GET /pub/blah.html HTTP/1.1
HOST: www.w3.org

Body of post (e.g. form fields; this is usually in the form of JSON data)
```

**HTTP Responses**

```
HTTP-Version SP Status-Code SP Reason-Phrase CRLF
Response body
```

**Successful response (GET/POST)**

```
HTTP/1.1 200 OK
Data: Mon, 04 Jul 2011 06:00:01 GMT
Server: Apache
Accept-Rangers: bytes
Content-Length 1240
Connection: close
Content-Type: test/html; charset=UTF-8

<HTML body>
```

**Response Codes**

- 1xx: Informational issues
- 2xx: Success
- 3xx: Redirections
- 4xx: Client error
- 5xx: Server error

> We will be using the Express Package in order to build our server, this will allow us to listen
> for requests on an endpoint, below is a diagram of how this might work:

![Express structure](./Diagrams/express.png)

**The body of an HTTP request**

- Three types of body data:
  - Single resource bodies: consisting of single file of known length, defined by the two headers `Content-Type` and `Content-Length`.
  - Single resource bodies: consisting of sing files of unknown length, encoded using chunks with `Transfer-Encoding`.
  - Multiple-resource bodies: consisting of multipart body, each containing a different section of information. These are relatively rare.

There are a number of `HTTP` verbs:

1. `GET`
2. `PUT`
3. `POST`
4. `DELETE`
5. `HEAD`
6. `PATCH`

**REST (Representational State Transfer)**

`REST` is a way for developers to use `HTTP` methods/verbs explicitly and consistently with the `HTTP` protocol
definition. `REST` and `CRUD` are used together, rest implies that we should only use these `HTTP` verbs ONLY when
we want to implement `CRUD`, we should not use these verbs for other tasks, `REST` implies that it is bad practice
to use `HTTP` methods in unconventional ways.

##### JavaScript Introduction

**JavaScript has the following things**

- Objects, methods and functions
- Expressions, statements and declarations
- Functions
  - Immediately invoked function expression
- Scoping issues
- Variables and (variable hoisting)
- Closures
- this keyword
- Method chaining (cascading
- `use strict`; mode
- Modularisation: export and require
- Node.js
- Asynchronous (event) handling
  - Callbacks, Promises Async/Await

**JavaScript is object orientated, however it is not strictly OOP**

- An object is a collection of properties and a property is an association between a name or key and a value
- A property can itself be an object
- A method is a function associated with an object or alternatively a method is a property that is a function
- Functions are first-class objects
- They can have properties and methods, just like an other object
- Unlike other objects, functions can be called
- Functions are, technically, function objects
- Functions can be called like a lambda function by putting () around the whole function
- Functions can be unnamed

**Expressions, statements and declarations**

- An expression produces a value
- A statement does not return a value
- Declarations are creations of net things
- JavaScript also has
  - Expression statements: where it expects a statement you can also write an expression
  - The reverse does not hold: you cannot write a statement where JavaScript expects an expression

Example of this in implementation:

```JavaScript
var result = function aFunction () {
    return -1
}
```

> This will assign result = aFunction(), it is NOT equal to -1 (in this case it is because there is no parameter being passed)

To execute a function immediately we can call it using the following syntax

```JavaScript
+function functionName () {
    console.log('Hello, World!')
} (); // These end brackets call the function immediately defined above
```

Anything defined within a function is within its scope, nested functions will contain the same
scope as the outer function.

> IMPORTANT NOTE: Functions will use the scope of where they are declared, not where they are called or implemented.

Using the following code will avoid these idiosyncrocies as they are blocked scoped:

```JavaScript
let x = 1;
const y = 2;
```

Use `this` keyword carefully, it references different objects depending on the context it is implemented in:

- In a browser it references the window
- in node.js it references a global object
- and in other context it works differently

Chaining functions can make your code more readable.



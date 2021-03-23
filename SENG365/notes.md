> [TOC]

# Web Computing Architecture

### Course Information

### Grading Structure

- Assignment One (25%)
    * No extension
- Mid-semester test (20%)
    * Wednesday 24 March, 7:00 pm
    * Topics
        + HTTP
        + REST API
        + JavaScript
        + Web databases
    * paper exam, closed book
    * 24 short answer questions
    * 2 hours (should take less)
- Assignment 2 (25%)
    * Compulsory lab in final week
    * No extension
- Exam (30%)
    * 2 hours

# Lab Notes

<details close="">
  <summary>Lab One</summary>
</details>

### Lectures

<details close="">
  <summary> Lecture One: Introduction to HTTP and JavaScript</summary>

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

Using the following code will avoid these idiocies as they are blocked scoped:

```JavaScript
let x = 1;
const y = 2;
```

Use `this` keyword carefully, it references different objects depending on the context it is implemented in:

- In a browser it references the window
- in node.js it references a global object
- and in other context it works differently

Chaining functions can make your code more readable.

</details>

<details close="">
  <summary>Lecture Two: Asynchronous behaviour</summary>

A problem that we commonly face is when we have some set of actions, but we do not know in what
order these tasks/actions are going to be completed in. `JavaScript` is a single threaded language,
it has a single call stack, a heap and the message queue which records a list of messages to be processed and the associate callbakc
functions to execute.

It also has an event loop, this is the order of operations the heap is called in, understanding this
is crucial to understanding odd errors that may occur.


The term `Blocking` really just means, we don't want to fill the call stack, when we have blocking code is JS
it is just when the call stack is too full (a while loop if it is not running too long will not be blocking)

We need to structure our code into different modules, there are different ways of managing this.
Modular JavaScript files, we will be using the `CommonJS` approach.

`CommonJS:`

- One specification for managing module dependencies
- maps well to `Node.js`

We can use the `require()` function in order to use local modules, and we are able to install
external modules using the Node Package Manager (`npm`) *commands - install, upgrade, status, -v*

```javascript
// Syntax for require function
var importJson = require('./path/to/data.json');
```

We will use the `express` library as a public interface module to use the web.

</details>

<details close="">
  <summary>Lecture Three: data persistence with SQL, memory stores and Graph DB</summary>

**Using JSON data**

- JSON is a lightweight data-interchange format
- A syntax for serializing data, objects, arrays, numbers, strings
- Data only, does not support comments except as a data field
- Non specific to JavaScript
    * Was originally intended for data interchange between Java and JavaScript
- No versioning for JSON
    * Enables consistency
    * Data gets updated all the time, it means that the syntax will always remain stable
- JSON has many variants (maintained by different people)
    * JSON-T (template JSON)
    * Many other forms of JSON
- JSON rules:
    * All key-names are double-quoted
    * Values
        + Strings are double quoted
        + Non-strings are not quoted
    * Escape uses \
    * Works with a set of values contained (can be mapped to a large dictionary)

**Relational Databases**

- One of the few situations where a theoretical contribution led to use case in the industry
- Relational Model
    * Data is presented as relations
    * Collections of tables with columns and rows (tuples)
    * Each tuple has attributes
    * Unique key per row
    * Relational model is built off of Relational Calculus (formal notation of key points)
- ACID transactions
    * Atomicity: if one part of a transaction fails, then transaction fails
    * Consistency: the database is kept in a consistent state before and after transaction execution
    * isolation: one transaction should not see the effects of another in progress
    * Durability: ensures transactions, once committed, are persistent

**CAP Theorem**
- In distributed computing, choose two of:
    * Consistency - every read receives the most recent data
    * Availability - every read receives a response
    * Partition tolerance - system continues if network goes down
- Situation is actually more subtle than implied
- BASE
    * Give up consistency and instead get:
        + Basic Availability - through replication
        + Soft state - state of the system may change over time
        + Eventual consistency - the data will be consistent eventually

**Memory Data Store**
- Whole database stored in RAM
    * Very fast access
    * Useful for cached storage
- Key value store where the value can be complex data structure
    * Strings, Bit arrays, lists, sets, hashes
    * streams
    * binary safe keys
    * command set for optimized load, storing and changing data values
- Useful for logging

**Document Databases**
- Storing in local files (JSON/XML or any other unstructured data format) 
- Tends to be stored with meta data (security, providence)
- Builds index from contexts and meta data
- storage of raw program types
- Complex data easily stored
- No need for costly schema
- Same data can be replicated (loads of redundancy)

**Graph Databases**
- Nodes: represent an entity
- Edge: represents relationship between nodes
- Properties: describe attributes of the node or edge
- Hyper graph: one edge can join multiple nodes

</details>

<details closed="">
  <summary>Lecture Four: REST</summary>

A REST service has the following benefits

- Platform independent
- Language independent
- Standards based (runs on top of http)
- Can easily be used in presence of firewalls
- RESTful systems typically
    * communicate over HTTP
    * with the same HTTP verbs (GET, POST, PUT, DELETE)
- Use URL to navigate between the API instances

</details>

## Notes Summary First Semester (Mid-term Prep) Mar 23, 2021

**HTTP Protocol**

HTTP messages are how data is exchanged between a sever and a client. There
are two types of messages: *requests* are sent by the client to trigger an action
from the server. *responses* are the answer sent back from the server.

HTTP messages are composed of **textual** information encoded in ASCII, and span
over multiple lines. In HTTP/1.1 and earlier versions, these messages were openly
sent across the connection.

**Uniform Resource Identifiers (URI's)**

1. URI (Uniform Resource Identifier)
  a. String of characters to identify (name, or name and location) resource.
2. URL (Uniform Resource Locator)
  a. A URI that also specifies the means of acting apon or obtaining representation.
3. URN (Uniform Resource Name)
  a. Depreciated: historical name for URI

**Some default Ports**

- Default HTTP port: 80
- Default HTTPS port: 433
- Default MySQL port: 3306

**The Path**

- Path is increasingly becoming an abstraction
- Not a physical path to a file location
- A path to an HTML file is not the same thing as a path to an endpoint
- An API endpoint uses the standard URI path structure to achieve something different
  * In particular, parameter information
- The path may need to include information about the version of the API

**Query Parameters**

The API can be designed to accept parameters via:
- The URI `?` query parameters
- The URI path (:id)
- The body of the HTTP request (JSON)
- Via some combination of the above

**Anchors**

- Anchors are used as bookmarks within a classic HTML webpage
  * i.e. point to a subsection of the page
- We don't need to use anchors for our APE requests

**Headers**

- General headers: required and `additional`
- Entity headers: (that apply to the body of the request)
- Request headers:
- Response headers:
- Cookies are implemented in the header
  * Set-Cookie: <...> in the header of the servers HTTP response
  * Cookie: <...> in the header of the subsequent client HTTP request
- Use headers to:
  * Maintain session
  * Personalise
  * Track (advertising)

**Response codes**
- 100: informational (rare)
- 200: success
- 300: redirections
- 400: client errors (very common)
- 500: server errors


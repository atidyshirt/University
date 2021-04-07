### Past Exam Papers -- Midterm

1. AJAX (Asynchronous JavaScript and XML) which letter is no longer relevant?
  a. XML is no longer used
2. name the three standard technologies for presentation, styling and computation in an SPA?
  a. HTML, JavaScript, and CSS
3. In one or two sentences, identify the key differences between a static website that enabled SPAs. (Concepts not technologies)
  a. In an SPA, when reloading or re-directing to different 'pages/routing points', we do not have to reload the whole page.
  b. SPA's also map well to large scale businesses.
  c. has high initial loading times, then small loading after
  d. Easier to deploy on behalf of a team, easier versioning and rollback. Due to server side configuration deciding on which version to build.
4. Two reasons to implement an SPA over static website in the front end.
  a. In order to increase flow after initial load for the user (not having to reload website html) times for the user.
  b. Because it is easier to deploy and version control an SPA, (due to server side configuration options)
5. Is event loop for JS single or multi-threaded?
  a. Single threaded
6. Give output from segment

> 1 \
> 3

1. Complete DOCTYPE statement from scripting snippet
  a. `<!DOCTYPE html>`
2. Povide CSS rule to make input field yellow

```css
#score {
  color: yellow;
}
```

1. value = 3
2. `use strict` ensures that thee are no undeclared or undefined variables in addScore() function (runs strict mode)
3. `const` is only available in Es and `arrow functions`.
4. `onclick='addScore'`

```Javascript
const addScore = () => {
  const score = document.getElementById('score');
  document.getElementById('result').innerHTML = score;
}
```

**Section C: Client side Security**

1. 1, 4
2. To cross site attack your own site
3. Allows restricted resources to be shared between domains
4. XXS is the stealing of cookies through a script injection on a vulnerable website
  a. Cross site scripting is done by sending malicious code to another users computer (via vulnerability)
5. Automated testing lets us test multiple things at once, allows us to re-test quickly after making changes to the code, and much easier to use in teams in order to pass acceptance criteria, grantees quality.


**REST (Representational State Transfer)**

- CRUD: Create, Retrieve, Update, Delete
- Don't have to map CRUD operands to HTTP methods

BAD PRACTICE: GET /path/?action=delete

**ES6** 

- var is lexically scoped (scoped where declared)
- let is block scoped (scoped where initilized)
- const is block scope (scoped where initilized)

**Use strict**

- modifies semantics of code
  * this is undefined
  * less lenient about variable declorations
  * throws errors rather than tolerating warnings
  * rejects `with` statements and octel notation
  * Prevents words like eval from being assigned 
  * warnings throw errors with linter
  * can be applied to a script or at function level

### Asynchronous Coding in JavaScript 

```JavaScript
// setTimeout example
setTimeout(() => {
  console.log('waiting 1 second');

}, 1000);
```

> Will call this after a second, however this cam result in callback hell as we nest lots of callback loops

```Javascript
// Using fs module (file)
fs.readFile('./test', {encoding: 'utf-8'}, {err, data} => {
  if (err) {
    console.log(err);
  } else {
    console.log('Do something');
  }
});

// old style of dealing with callbacks (async code, this is called error first callback methods)
```

**Promises**

```JavaScript
const somePromise = new Promise((resolve, reject) => {
  if(rand == 0) {
    resolve();
  } else {
    reject();
  }
});

somePromise
  .then(() => console.log("Happy"));
  .catch(() => console.error('not so happy'));
```

**Async and Await**

```JavaScript
// Async and Await
const loadFile = async () => {
  try {
    const data = await fs.promises.readFile("./test.txt", {
      encoding: "utf-8",
    });
    console.log(data);
  } catch (err) {
    console.error(err);
  }
};
```

JavaScript is the following:
- Single threaded
- Single concurrent language
  * Meaning JavaScript can handle one task at a time or piece of code at a time
* single call stack bundled with heap and queue. 

**Call Stack**
- A data structure to maintain record of function calls
- Call a function to execute: push something on to the stack

Here is the coding example for async and await supplied by Uni:

```JavaScript
console.log("Start");

function g(input) {
  return input + 1;
}

let a_function = g;
console.log(a_function);
console.log("The result of g(2) is :", g(2));

async function f(input) {
  return input + 1;
}

let another_function = f;
console.log(another_function);
console.log("The result of f(2) is: ", f(2));

f(10).then(function(result) {
  console.log("The result of f() is: " + result);
});

another_function(100).then(function(result) {
  console.log("The result of another_function (f()) is: " + result);
});
```

**JSON**

- lightweight data-interchange format
- A syntax for serializing data
- Not specific to JS
- No versioning for JSON (to remain consistent)
- Has variants and extentions (JASON-T)
- keys must be double quoted 

**Relational DB**

- One of the few situations where a theoretical thesis led to innovation in the industry
- Relational Model:
  * Data is presented as relations
  * Collections of tables with columns and rows (tuples
  * Each tuple has the same attributes
  * Unique key per tuple
  * Relational algebra defines operations in a formal sense
- ACID database transactions
  * Atomicity: all or nothing
  * Consistency: the database must be in a consistent state before and after the transaction has executed
  * Isolation: One transaction should not see the effects of another transaction in progress
  * Durability: ensures transactions once committed are persistent.

Shared vs Shared nothing approaches 

- Main RAM sizes: 1MiB, 2020: 4Tib
- Resource control
- Grid commuting
- High availability 
- Tuning
- Many areas are moving towards a distributed model

**CAP Theorem**

- In distributed computing, choose two of:
  * Consistency: every read receives the most recent data
  * Availability: every read receives a response
  * Partition tolerance: system continues if network goes down
- Situation is actually more subtle than implied
  * Can adaptively chose appropriate trade-offs
  * Can understand semantics of data to choose safe operations

**BASE**

- Give up consistency and we get instead:
  * Basic availability: through replication 
  * Soft state: the state of the system may change over time
  * Eventual consistency: data will be consistent eventually 

**ACID vs BASE comparison**

- Suppose we wanted to track peoples bank accounts
  * CREATE TABLE user (uid,name,amt_sold,amt_bought)
  * CREATE TABLE transaction (tid,seller_id,buyer_id,amount)
- ACID transactions may look something like this:

```sql
BEGIN
  INSERT INTO transaction (tid,seller_id,buyer_id,amount);
  UPDATE user SET amt_sold=amt_sold + amount where id=seller_id;
  UPDATE user SET amt_bought=amt_bought + amount where id=buyer_id;
END
```

- A BASE transaction may be split as the following:

```sql
BEGIN
  INSERT INTO transaction(tid, seller_id, buyer_id, amount);
END

BEGIN
  UPDATE user SET amt_sold=amt_sold + amount WHERE id=seller_id;
  UPDATE user SET amt_bought=amt_bought + amount WHERE id=buyer_id;
END
```

REST

- Platform independent
- Language independent
- Standards based (runs on HTTP)
- Can be easily used with firewalls
- RESTful systems are typically hypertext transfer protocols
- with the same HTTP verbs (GPPD)
- Goal: to retrieve web pages and send them over remote servers
- subset of web-app's 
- CRUD maps to REST
- use PATCH for partial change, PUT maps to UPDATE in crud

**Adding example:**

1: bad

2: xml is a bit cryptic to use

3: best, uses JSON and correct HTTP `POST` method

REST has no inbuilt security of QoS features
These can be built on top of the REST api

For encryption REST can use (secure sockets) ontop of HTTPS.

REST has replaced SOAP, because it works nicely with AJAX / XHR, has network advantages

**Stateless Requests**

- A complete independent request doesn't require the server to while processing the request
 to retrieve any kind of application context or state.
- A RESTFUL web service or client includes within the HTTP headers and body of a request all of the parameters, context and data needed by the server side component to generate a response
- The entire resource is returned not part of it.
- Statelessness
  * Improves web service performances
  * Simplifies the design and implementation of server-side components
  * because the absence of state on the server removes the need to synchronize session data with an external application
  * Hide the server-side scripting technology file extensions within the URLS
  * Be consistent in the singularity/plurality of resource names 
  * keep everything lowercase
  * use hyphens instead of spaces
  * instead of using 404 not found code, if the request for a URI is for a partial path, always provide a default page or resource as a resonse
    + Not required for assignment
  * Tightly coupled to HTTP
  * Request response format
    + Multiple requests and responses needed
    + Under fetching and over fetching
    + Latency increases for full set of request and responses
    + Implied tree-structure


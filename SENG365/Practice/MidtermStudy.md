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

```
1

3
```

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



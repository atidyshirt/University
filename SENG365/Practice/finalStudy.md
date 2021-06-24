# 2019 Past Paper

1. AJAX 

AJAX stands for Asyncronous Javascript And XML

- The X part of this is no longer true due to the fact that most people have
  switched from using XML to JSON.

2. The three standard technologies for an SPA are the following

- HTML for presentation
- CSS for styling
- Javascript for computation

3. Address main differences between SPA's and static multipage websites

- SPA's allow for updating one component and not having to redraw the entire
  page, this leads to more efficient websites and quicker usage for end users
- SPA's send data between components rather than between pages, a webpage can
  be made up of multiple components
- Components in an SPA are loaded as different URL links over the template HTML
  (these URL's can contain multiple components).
- Data is fetched using AJAX/JSON.

4. Why might we choose SPA rather than static website? 

- Because they want there users to have a faster and better user experience
  due to the fact that we can update small parts of the webpage without updating
  the whole webpage.
- To contain the client side rendering of information and UI updating all within
  the browser.

5. Is the event loop for Javascript in the browser single or multi-threaded?

- Single threaded

6. Give output of following code

```javascript
console.log("1");
setTimeout(() => console.log("2"), 0);
console.log("3");
```

> Output: 1 \n 2 \n 3 \n

7. Complete DOCTYPE

<!DOCTYPE HTML>

8. Provide css rule in line 8 to set color of input field to yellow

```javascript
<style>
  .score {
    background-color: yellow;
  }
</style>
<input id='score' type='number' min=1 max=5 value=3 name='score'>
```

9. If the user did not enter a value into the form, and simply pressed the 
   'Go' button, state the value that would be passed by default:

> 3 would be parsed in

10. `use strict` at the top of a function will enable strict mode, meaning
    that certain things JS will treat as errors, such as undefined variables
    within the function. Leads to nicer code and conforms to more best practices.

11. Identify the part or parts of the code fragment that indicate that this is ES6 code

Line 18: `const addScore = () => {}`

12. Complete the onclick attribute in the button element in line 15:

```<button onclick=’addScore()' name='button'>Go</button>```

13. Complete the onScore() function, displays on line 10

```javascript
function onScore() {

}
```



That's a great solution! The `requestPromise` wrapper helps manage asynchronous operations more cleanly by using Promises and `async/await`, which can make the code more readable and easier to debug compared to nested callbacks.

To further break it down:

1. **Promise Wrapper**:
   - The `requestPromise` function takes a URL and returns a Promise.
   - Inside the Promise, the `request` function is called.
   - If there's an error, the Promise is rejected.
   - If the request is successful, the Promise is resolved with the response body.

2. **Async/Await**:
   - The IIFE (Immediately Invoked Function Expression) is declared as an `async` function.
   - Inside this async function, `await` is used to wait for the Promises to resolve.
   - The `try...catch` block is used to handle errors that may occur during the asynchronous operations.

Here's the complete code for reference:

```javascript
const requestPromise = (url) => {
  return new Promise((resolve, reject) => {
    request(url, function (err, response, body) {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
};

(async () => {
  try {
    const body = await requestPromise(url);
    characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      const character = await requestPromise(characters[i]);
      console.log(JSON.parse(character).name);
    }
  } catch (err) {
    console.error('code:', err.statusCode);
  }
})();
```

### Key Points:

- **Promises**: They represent the eventual completion (or failure) of an asynchronous operation and its resulting value.
- **Async/Await**: Syntactic sugar built on Promises that allows you to write asynchronous code that looks synchronous.
- **Error Handling**: Using `try...catch` to handle errors in asynchronous code.

This approach ensures that the order of the characters remains consistent with the order provided in the API response. It avoids the "callback hell" problem by flattening the code structure and making it more readable.
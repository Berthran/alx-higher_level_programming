#!/usr/bin/node
const request = require('request');
const url = 'http://jsonbin.io/b/591a64459208345676e6a1ed';
request (url, function (error, response, body) {
 if (error) {
  console.log(error);
 } else {
  console.log(JSON.parse(body));
 }
});
To access the respective attributes, say the “name”, you simply add that attribute to the code accordingly.

```javascript
#!/usr/bin/node
const request = require('request');
const url = 'http://jsonbin.io/b/591a64459208345676e6a1ed';
request (url, function (error, response, body) {
 if (error) {
  console.log(error);
 } else {
  console.log(JSON.parse(body).name);
 }
});
>>> TCP
```

To access the respective an element in the array of “likes” attribute, say the first element [which is of course the 0th element], you simply add that attribute and the element you are trying to grab, to the code accordingly. [can print out all elements of the “likes” array by simply not specifying the element].

```javascript
#!/usr/bin/node
const request = require('request');
const url = 'http://jsonbin.io/b/591a64459208345676e6a1ed';
request (url, function (error, response, body) {
 if (error) {
  console.log(error);
 } else {
  console.log(JSON.parse(body).likes[0]);
 }
});
>>> Reliability
```

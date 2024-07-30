const request = require('request')
const id = process.argv[2]
console.log(id)
// Request URL
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
 
request(url, (error, response, body) => {
    // Printing the error if occurred
    if (error) console.log(error)
 
    // Printing status code
    console.log(response.statusCode);
 
    // Printing body
    console.log(JSON.parse(body)["title"]);
});

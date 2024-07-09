## How to confirm that header sent with request is successful

To confirm that your script is correctly sending the HTTP request with the header `X-School-User-Id` set to `98`, you can use a few methods:

1. **Using a Local Server to Inspect Requests**:
   - Set up a local server that can log incoming requests. For example, using Python's built-in HTTP server, you can write a simple server that logs the headers of incoming requests.

2. **Using a Request Inspection Service**:
   - Use an online service like [httpbin.org](http://httpbin.org) or [requestbin.com](https://requestbin.com) which echoes back the headers it receives.

Here, I'll show you both methods.

### Method 1: Local Server to Inspect Requests

Create a simple Python script to start an HTTP server that logs request headers:

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request on {self.path}")
        print(f"Headers:\n{self.headers}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Received')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=3000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
```

Run this script to start the server:

```sh
python3 server.py
```

Then, execute your script that makes the HTTP request to `http://localhost:3000/`. Check the output in the terminal where your server is running to see if the `X-School-User-Id` header is logged.

### Method 2: Using httpbin.org

Use `httpbin.org` to test your request. `httpbin.org` provides an endpoint `/headers` that returns the headers it received in the request.

Here is the curl command you can use to confirm your script:

```sh
curl -i -H "X-School-User-Id: 98" http://httpbin.org/headers
```

### Explanation:

- `-i`: Include the HTTP response headers in the output.
- `-H "X-School-User-Id: 98"`: Add the `X-School-User-Id` header with the value `98`.

### Example Output:

```sh
HTTP/1.1 200 OK
Date: Tue, 09 Jul 2024 10:00:00 GMT
Content-Type: application/json
Content-Length: 250
Connection: keep-alive
Server: gunicorn/19.9.0

{
  "headers": {
    "Accept": "*/*",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.68.0",
    "X-School-User-Id": "98"
  }
}
```

In the JSON output, you should see the `X-School-User-Id` header with the value `98` under `"headers"`.

### Verifying Your Script

If you have a script that makes this request, run the script and use either the local server method or the httpbin method to verify the headers sent. For example:

```sh
./your_script.sh
```

Then, check the output in your local server or the response from `httpbin.org` to confirm the presence of the `X-School-User-Id` header with the value `98`.

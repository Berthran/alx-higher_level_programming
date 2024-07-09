## Handling redirections
curl option  `-L, --location`
              (HTTP) If the server reports that the requested page has moved to a different location (indicated  with
              a  Location:  header  and  a 3XX response code), this option will make curl redo the request on the new
              place. If used together with -i, --include or -I, --head, headers from  all  requested  pages  will  be
              shown.  When authentication is used, curl only sends its credentials to the initial host. If a redirect
              takes curl to a different host, it will not be able to intercept the user+password.  See  also  --loca‐
              tion-trusted on how to change this. You can limit the amount of redirects to follow by using the --max-
              redirs option.

              When curl follows a redirect and if the request is a POST, it will send the following  request  with  a
              GET  if  the HTTP response was 301, 302, or 303. If the response code was any other 3xx code, curl will
              re-send the following request using the same unmodified method.

              You can tell curl to not change POST requests to GET after a 30x response by using  the  dedicated  op‐
              tions for that: --post301, --post302 and --post303.

              The method set with -X, --request overrides the method curl would otherwise select to use.

              Example:
               curl -L https://example.com

              See also --resolve and --alt-svc.

To solve this task, the status code of must be checked before the final response body is displayed.

## Check status code
```sh
curl -s -w "%{http_code}" https://example.com | grep -q 200
```
This checks if the status code of the URL is 200.
The `-s` flag hides the progress meter.
`http_code` is a variable that holds the response status code.

## Handle redirections and check status code
```sh
curl -s -L -w "%{http_code}" https://example.com | grep -q 200 && curl -s -L https://example.com
```

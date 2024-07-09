## Write out
--write-out or just -w for short, outputs text and information after a transfer is completed. It offers a large range of variables that you can include in the output, variables that have been set with values and information from the transfer.

Instruct curl to output a string by passing plain text to this option:

curl -w "formatted string" http://example.com/
…and you can also have curl read that string from a given file instead if you prefix the string with '@':

```sh
curl -w @filename http://example.com/
```
…or even have curl read the string from stdin if you use '-' as filename:


curl -w @- http://example.com/

As an example, we can output the Content-Type and the response code from an HTTP transfer, separated with newlines and some extra text like this:

```
curl -w "Type: %{content_type}\nCode: %{response_code}\n" \
  http://example.com
```
The output is sent to stdout by default so you probably want to make sure that you do not also send the downloaded content to stdout as then you might have a hard time to separate out the data; or use %{stderr} to send the output to stderr.

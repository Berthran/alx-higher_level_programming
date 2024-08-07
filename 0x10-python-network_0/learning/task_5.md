## POST method

       -d, --data <data>
              (HTTP  MQTT)  Sends  the  specified  data  in a POST request to the HTTP server, in the same way that a
              browser does when a user has filled in an HTML form and presses the submit button. This will cause curl
              to pass the data to the server using the content-type application/x-www-form-urlencoded. Compare to -F,
              --form.

              --data-raw is almost the same but does not have a special interpretation of the @  character.  To  post
              data  purely binary, you should instead use the --data-binary option. To URL-encode the value of a form
              field you may use --data-urlencode.

              If any of these options is used more than once on the same command line, the data pieces specified will
              be merged with a separating &-symbol. Thus, using '-d name=daniel -d skill=lousy' would generate a post
              chunk that looks like 'name=daniel&skill=lousy'.

              If you start the data with the letter @, the rest should be a file name to read the data from, or -  if
              you  want  curl to read the data from stdin. Posting data from a file named 'foobar' would thus be done
              with -d, --data @foobar. When -d, --data is told to read from a file like that,  carriage  returns  and
              newlines  will be stripped out. If you do not want the @ character to have a special interpretation use
              --data-raw instead.

              Examples:
               curl -d "name=curl" https://example.com
               curl -d "name=curl" -d "tool=cmdline" https://example.com
               curl -d @filename https://example.com

              See also --data-binary, --data-urlencode and --data-raw. This  option  overrides  -F,  --form  and  -I,
              --head and -T, --upload-file.

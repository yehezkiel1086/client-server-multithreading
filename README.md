# Client Server Multithreading

## Description

- Open a port on port 45000 with TCP transport
- The server must be able to serve concurrent requests (multithreading)
- Terms of requests served
  - Starting with the string "TIME and ending with character 13 and character 10"
  - Each request can end with the string “QUIT” ending with characters 13 and 10
  - The server will respond with hours with conditions
  - In string form (UTF-8)
  - Starting with "JAM\<space\>\<hour\>"
  - <hour> contains hour information in the format "hh:mm:ss" and ends with character 13 and character 10

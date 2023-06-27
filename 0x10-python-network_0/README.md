Using HTTP cookies
An HTTP cookie (web cookie, browser cookie) is a small piece of data that a server sends to a user's web browser. The browser may store the cookie and send it back to the same server with later requests. Typically, an HTTP cookie is used to tell if two requests come from the same browser—keeping a user logged in, for example. It remembers stateful information for the stateless HTTP protocol.

Cookies are mainly used for three purposes:

Session management
Logins, shopping carts, game scores, or anything else the server should remember

Personalization
User preferences, themes, and other settings

Tracking
Recording and analyzing user behavior

Cookies were once used for general client-side storage. While this made sense when they were the only way to store data on the client, modern storage APIs are now recommended. Cookies are sent with every request, so they can worsen performance (especially for mobile data connections). Modern APIs for client storage are the Web Storage API (localStorage and sessionStorage) and IndexedDB.

Note: To see stored cookies (and other storage that a web page can use), you can enable the Storage Inspector in Developer Tools and select Cookies from the storage tree.

Creating cookies
After receiving an HTTP request, a server can send one or more Set-Cookie headers with the response. The browser usually stores the cookie and sends it with requests made to the same server inside a Cookie HTTP header. You can specify an expiration date or time period after which the cookie shouldn't be sent. You can also set additional restrictions to a specific domain and path to limit where the cookie is sent. For details about the header attributes mentioned below, refer to the Set-Cookie reference article.

The Set-Cookie and Cookie headers
The Set-Cookie HTTP response header sends cookies from the server to the user agent. A simple cookie is set like this:

HTTP
Copy to Clipboard

Set-Cookie: <cookie-name>=<cookie-value>
This instructs the server sending headers to tell the client to store a pair of cookies:

HTTP
Copy to Clipboard

HTTP/2.0 200 OK
Content-Type: text/html
Set-Cookie: yummy_cookie=choco
Set-Cookie: tasty_cookie=strawberry

[page content]
Then, with every subsequent request to the server, the browser sends all previously stored cookies back to the server using the Cookie header.

HTTP
Copy to Clipboard

GET /sample_page.html HTTP/2.0
Host: www.example.org
Cookie: yummy_cookie=choco; tasty_cookie=strawberry
Note: Here's how to use the Set-Cookie header in various server-side applications:

PHP
Node.JS
Python
Ruby on Rails
Define the lifetime of a cookie
The lifetime of a cookie can be defined in two ways:

Session cookies are deleted when the current session ends. The browser defines when the "current session" ends, and some browsers use session restoring when restarting. This can cause session cookies to last indefinitely.
Permanent cookies are deleted at a date specified by the Expires attribute, or after a period of time specified by the Max-Age attribute.

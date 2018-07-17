## Internet!
What is it?
- The Internet is basically just a marriage of hardware and protocols.
- ARPANET - the grandfather to the internet. It’s just a network but the internet is a internet of internets. This started in the 1970s.
- The internet is always changing as new networks come and old ones go. There are satellite networks and land networks connected via submarine cables. This can be even as small as a home network, or local area network (like an office).
- The difference between the web and the internet.

## Clients and Servers
The internet is made up of two types of machines clients and server. Every machine is ether a client or a server but many machines can be both.
- The client requests information from a server. The client starts with the local server and goes to a regional and than national server. It goes up the chain until it gets the information you need is.
- A server is a computer program or a device that provides functionality for other programs or devices(clients).
- When the information is being sent it needs to broken into many small pieces which are called packet. Packets don't always go in order and sometimes the same packets are sent separately in different places. Packets are reassembled based on the instructions that get sent.
- When you go to a website what happens?
The domain name system (DNS) translates hostnames such as (www.google.com) the ip address to a domain name. This happens via an DNS resolver.

## What happens when you go to google
- [An answer to an interview question](https://github.com/alex/what-happens-when)

## Requests
We use requests everyday:
- When you view a facebook post you use the GET method.
- When you write a facebook post you use the POST method.
- When you delete a facebook you use the DELETE method.
- When you edit a facebook post you use the PATCH method.  

## Other types of Requests
- HEAD - Same as GET but returns only HTTP headers and no document body
- PUT - Uploads a representation of the specified URI
- DELETE - Deletes the specified resource
- OPTIONS - Returns the HTTP methods that the server supports
- CONNECT - Converts the request connection to a transparent TCP/IP tunnel

## HTTP Messages
- 100 level - Information
- 200 level - Successful
- 300 level - Redirection
- 400 level - Client Error
- 500 level - Server Errors

## Why Does This Matter?
If we connect to an API to receive live data this becomes important. Also if you want to write code that makes websites you will also need to know this.

## Resources
- [How does the internet work?](https://www.codenewbie.org/podcast/how-does-the-internet-work)
- [How the internet works](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)
- [How the internet works - Django Girls](https://tutorial.djangogirls.org/en/how_the_internet_works/)
- [Video on how the internet works](https://www.youtube.com/watch?v=zaH7rtqkY10)
- [How internet works](http://www.rookiemag.com/2016/11/how-internet-works/)
- [How servers work](https://computer.howstuffworks.com/web-server.htm)
- [A podcast on the subject](https://www.codenewbie.org/podcast/how-does-the-internet-work)
- [Interneting is Hard](https://internetingishard.com/html-and-css/)

- If you feel like reading a book on this subject [here is one I recommend](http://web.csulb.edu/~rlaster/docs/cecs572.pdf)

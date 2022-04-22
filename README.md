# PythonSocket-Client-Server

This project implements a simple communication between machines with a server

## How does it work ?

This project contains two modules : the server part and the client part.
The server creates connections between two clients by creating a channel on which the two clients can connect to.

The communication use Sockets to make the link between the server and the client.
In the end, one channel opens four sockets, two by client : one is for the uplink and one for the downlink.
Each message a client send is recieved by the server, and transmitted to the other client, which recieves it.

## How to use it ?

===== This part is still under construction ======

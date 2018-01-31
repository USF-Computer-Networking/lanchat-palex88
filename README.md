# LAN Scan and Chat

There are three main parts to this package. The scanner, chat server, and  the chat client.

## scan.py

- The scanner povides helpful functions that wrap bash `arp -a`, and creates a python dictionary with the results.

## chat_server.py

- The chat server listens for UDP messages from a certain IP address and port.

## chat_client.py

- The chat client allows a user to send messages to a specific IP address over a specific port.
- Default IP is set to the broadcast IP, 255.255.255.255.
- Default port is set 9999.
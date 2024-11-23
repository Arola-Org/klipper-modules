# Klipper Modules

A Klipper module extends the functionality of what Klipper/Klippy can provide by default

Read the docs here - https://www.klipper3d.org/Code_Overview.html

## General instructions

1. Copy the module in question to the klippy/extras directory on your printer, to do this you will need to SSH into your 3D printer. Logins will vary
2. Find the location by running `find / -name klippy.py` and genrally within the same location will be the extras directory
3. Update the printer.cfg to the relevent section for your module, specific details below.


## Included modules

- gotify.py

### Gotify (https://gotify.net/)

Gotify is a self hosted messaging server for being able to send and receive messages.

So the gotify.py module is used to interact with a server and be able to send messages directly from your printer

#### Examples

##### printer.cfg:

```
[gotify]
token: xxxx
endpoint: xxxx
protocol: https | http
verify: False | True (Default if unset and using https)
```

token (required): The login token associated with an app on your Gotify server
endpoint (required): The address of your gotify server, this can be an DNS resolvable name or an IP address
protocol (required): Whether your server is hosted over http (insecure) or https (secure)
verify (optional): If you are self hosting your own gotify server over https and the printer doesnt trust your certificate you an can set verify to False, by default this will be True if the protocol is https and you dont set this option.

##### Usage

```
[gcode_macro PRINT_START]         
gcode:
    SAVE_VARIABLE VARIABLE=was_interrupted VALUE=True
	G92 E0                                         
	G90             
    CLEAR_PAUSE
    M117 Printing
    GOTIFY_SEND TITLE="Elegoo Neptune 4 Pro" MSG="Print starting"
```
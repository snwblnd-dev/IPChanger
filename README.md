# IPChanger

A simple Python command-line utility to check your public IP address and route requests through either a custom proxy or the Tor network. Uses Ipify to check your IP address


Setup:

Required Dependencies: requests, PySocks, and stem (pip install requests stem PySocks)

To route through the Tor network, you must have Tor installed on your system.

By default, the script assumes the tor executable is in your system’s PATH
If it is not, you can specify the path to the executable using –torcmd

Usage:

Running the program without flags will just show your current public IP address.

Command-line flags:
-t: route traffic through a local Tor instance on port 9050

-p: specify a proxy server IP address to route traffic through (format as ip:port); supports http/https proxy connections.

–torcmd: specify the path to the tor browser executable


If flags are used to route traffic through a service, they will display your public IP after traffic has been routed. This allows you to confirm your public IP is not what websites are receiving.

# Traffic-Ghost
  This is an IOT device traffic attack research tool, easy to extend and portable framework, designed to monitor and tamper IOT device traffic, with reconnaissance and attack features to provide one-stop services for security researchers. It is easy to use, anyone can use it to achieve their own hijacking attack.

## Concept

- Performs a MITM attack to all selected victims
- Hijack the video stream and replay the set video stream
- The video stream has been hijacked successfully and has been replayed as a set video screen.

## Document description

- The content in the traffic_script file is the script to be replayed and the data to be replaced.

## Use

- install.sh

  ```
  ./install.sh
  ```

- Add the target ip you want to hijack in the victims with one IP per line 

- execute trafficGhost.py

  ```
  python3 trafficGhost.py gateway_ip
  ```

- The video stream has been hijacked successfully 

## Mitmproxy

[mitmproxy](https://mitmproxy.org/) is a  tool that allows us to analyze the traffic that goes through a host, and allows to edit that traffic. In our case, we will use it to achieve playback of video streams

mitmproxy requires python 3.6 or higher


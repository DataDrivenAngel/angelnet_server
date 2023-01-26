# Angel Net Server
This repository contains the server code for my home IoT sensor network.

## Power BI Streaming

The Angel Net server running on the raspberry pi was sending event data to the Power BI streaming dataset service via API.
 
Example:
![Power BI Dashboard](/AngelNetDashboard.gif)

## Sensors

The Raspberry Pi server receives data from three ESP8266 NodeMCU based custom sensor nodes. Each node has a DHT-11 Sensor and photoresister to record temperature, humidity, and light levels. The sensor code can be found [at this location.](https://github.com/DataDrivenAngel/angelnet
)



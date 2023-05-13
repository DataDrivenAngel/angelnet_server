# Angel Net Server
This repository contains the server code for my home IoT sensor network.
 
Example:
![Power BI Dashboard](/AngelNetDashboard.gif)

## Sensors

The Raspberry Pi server receives data from three ESP8266 NodeMCU based custom sensor nodes. Each node has a DHT-11 Sensor and photoresister to record temperature, humidity, and light levels.

## ESP8266 NodeMCU  Sensors

Each board is an ESP8266 NodeMCU with a DHT-11 sensor and a photoresister to measure relative light levels.

## Power BI Streaming

The Angel Net server running on the raspberry pi was sending event data to the Power BI streaming dataset service via API. This has been deprecated and the dashboards have been replaced with Metabase running on my home server.


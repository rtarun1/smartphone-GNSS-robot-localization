**Introduction** 

In this we use an iPhone as an GNSS receiver and stream the NMEA data using its hotspot (acting as a server), which is then captured using a laptop which is connected to the iPhone's WiFi (acting as a client). Python 3 is used to receive and decode the NMEA data into latitude and longitude.

**Phone setup**

- Install the GPS2IP mobile app in your iPhone (I am using the lite version) <https://apps.apple.com/us/app/gps-2-ip/id408625926>
- I am not sure, but the ShareGPS app must work similarly with Android devices.
- In settings:
  - Time between sending position
    - No Delay
    - Disable when static – Toggled off
  - GPS Accuracy 
    - The very best 
  - Protocol Type 
    - NMEA
  - NMEA messages to send
    - RMC – Toggled on
  - Other messages – Toggled off
  - General settings – your wish
  - Connection Method – Socket (port – 5050)
  - Network selection – Hotspot (use Wifi if you’re connecting to an external router)
- Now you must be able to see the iPhone server IP and port information in the home screen of the application.
- Lastly, toggle the Enable GPS2IP Lite to transmit GPS data.

**Computer setup**

- Use <https://github.com/semuconsulting/pynmeagps/blob/master/examples/nmeasocket.py>
- Don't forget to put your IP.

**Credits** 

<https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python>

<https://github.com/semuconsulting/pynmeagps/tree/master>

<https://www.capsicumdreams.com/gps2ip/>


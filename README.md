Velo_Time
=========

Get Timestamp and GPS fix out of a Velodyne and into ROS

To use, ensure your ROS machine has nmea_navsat (http://wiki.ros.org/nmea_navsat_driver) installed.
Then run the following in two seperate terminals:
rosrun nmea_navsat_driver nmea_topic_driver _useRMC:=true
./Velo_Time.py

The python code simply looks for GPRMC data on the Velodyne UDP port (8308), and publishes it to nmea navsat driver.
This way, the included GPS receiver with the Velodyne can be used to generate a rough fix and timing as well.

#!/usr/bin/env python
# license removed for brevity
import rospy
import socket
import nmea_msgs.msg
from nmea_msgs.msg import Sentence
import std_msgs.msg

UDP_IP = "255.255.255.255"
UDP_PORT = 8308

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def velodyne_Dat():
    pub = rospy.Publisher('nmea_sentence', Sentence, queue_size=1)
    rospy.init_node('velodyne_Dat', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data, addr = sock.recvfrom(1206) # buffer size is 1206 bytes
        if (addr[0] == "192.168.1.201"): # Ensure message is from Velodyne HDL32-E
            val = data[206:278].encode('ascii')
            #print val
            #print data[206:278].encode("hex")
            h = std_msgs.msg.Header()
            h.stamp = rospy.Time.now()
            h.frame_id = "velodyne" 
            Sen = nmea_msgs.msg.Sentence()
            Sen.header = h
            Sen.sentence = val # "$GPRMC,192326,A,4324.2427,N,08028.2217,W,000.0,000.0,080914,009.7,W,D*1F"
            pub.publish(Sen)
            r.sleep()

if __name__ == '__main__':
    try:
        velodyne_Dat()
    except rospy.ROSInterruptException: pass
    


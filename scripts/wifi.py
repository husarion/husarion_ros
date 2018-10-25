#!/usr/bin/env python
import subprocess
import time
from pythonwifi.iwlibs import Wireless
import commands
from ifparser import Ifcfg
import rospy
from std_msgs.msg import String
from diagnostic_msgs.msg import DiagnosticArray
from diagnostic_msgs.msg import DiagnosticStatus
from diagnostic_msgs.msg import KeyValue
import copy


def getWiFiList():
    ifdata = Ifcfg(commands.getoutput('ifconfig -a'))
    wifiList = []
    for interface in ifdata.interfaces:
        try:
            wifi = Wireless(interface)
            essid = wifi.getEssid()
            cmd = subprocess.Popen('iwconfig %s' %
                                   interface, shell=True, stdout=subprocess.PIPE)
            for line in cmd.stdout:
                if 'Link Quality' in line:
                    sigIndex = line.find("Signal level")
                    levelStr = line[sigIndex+13:]
                    value = 0
                    dBm_value = 0
                    percent = 0
                    if 'dBm' in levelStr:
                        value = int(levelStr.split(" ")[0])
                        dBm_value = value
                        # -35 dBm < signal 100%
                        # -95 dBm > signal 0%
                        if dBm_value > -35:
                            percent = 100
                        elif dBm_value < -95:
                            percent = 0
                        else:
                            percent = (value + 95) * 100 / 60
                            pass
                    if '/' in levelStr:
                        value = int(levelStr.split("/")[0])
                        percent = value
                        dBm_value = (value * 60 / 100) - 95
                    wifiDescriptor = [
                        interface, essid, dBm_value, percent]
                    wifiList.append(wifiDescriptor)
        except IOError:
            pass
    return wifiList


def wifi_main():
    wifi_pub = rospy.Publisher('wifi_status', DiagnosticArray, queue_size=1)
    rospy.init_node('wifi_status')
    rate = rospy.Rate(2)  # 10hz
    diagArrayWiFi = DiagnosticArray()
    diagArrayWiFi.header.frame_id = "robot_name"
    kv = KeyValue()
    rospy.loginfo("wifi_status publisher node started")

    while not rospy.is_shutdown():
        diagArrayWiFi.header.stamp = rospy.get_rostime()
        del(diagArrayWiFi.status[:])
        for wifi_status in getWiFiList():
            diagStatusWiFi = DiagnosticStatus()
            del(diagStatusWiFi.values[:])
            diagStatusWiFi.level = DiagnosticStatus.OK
            diagStatusWiFi.name = wifi_status[1]
            diagStatusWiFi.hardware_id = wifi_status[0]
            diagStatusWiFi.message = "Device is up"
            kv.key = "siglevel"
            kv.value = str(wifi_status[2])
            diagStatusWiFi.values.append(copy.copy(kv))
            kv.key = "percentage"
            kv.value = str(wifi_status[3])
            diagStatusWiFi.values.append(copy.copy(kv))
            diagArrayWiFi.status.append(copy.copy(diagStatusWiFi))
        wifi_pub.publish(diagArrayWiFi)
        rate.sleep()


if __name__ == '__main__':
    try:
        wifi_main()
    except rospy.ROSInterruptException:
        pass

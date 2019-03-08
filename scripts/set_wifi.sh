#!/bin/sh

if [ $# -gt 2 ]; then
NETWORK_SSID="$1"
NET_PASSWD="$2"
INTERFACE="$3"
else
    echo "Pelase run this script with arguments:"
    echo "set_wifi.sh <NetworkSSID> <Password> <ifname>"
    return 0
fi

echo "Will connect to $NETWORK_SSID with passowrd $NET_PASSWD on $INTERFACE device"

echo "Add connection"
nmcli c add type wifi save yes autoconnect yes con-name $NETWORK_SSID ifname $INTERFACE ssid $NETWORK_SSID
echo "Set password"
nmcli c modify $NETWORK_SSID wifi-sec.key-mgmt wpa-psk wifi-sec.psk $NET_PASSWD

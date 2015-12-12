#!/bin/bash

if [[ $EUID -ne 0 ]]; then
   echo "This script. must be run as root" 1>&2
   exit 1
fi

sed -i "s/cn\.archive\.ubuntu\.com/mirrors\.163\.com/" /etc/apt/sources.list
apt-get update
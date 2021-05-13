#!/bin/sh

recup=`ssh jmf@192.168.1.24   systemctl is-active jenkins`
echo $recup
if [ $recup = 'inactive' ]
then
 exit 1
fi


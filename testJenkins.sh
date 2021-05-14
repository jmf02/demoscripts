#!/bin/sh

recup=`${urljenkins}`
echo $recup
if [ $recup = 'inactive' ]
then
 exit 1
fi


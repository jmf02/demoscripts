#!/bin/sh

recup=`${urljenkins}`
if [ $recup = 'inactive' ]
then
 echo Jenkins $recup	
 exit 1
else
 echo Jenkins $recup 
fi


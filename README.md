# personal-earbud-script
a set of utilities to sync, connect and disconnect ANY airbuds

this utilities consist on:

-A bash script for connect, sync and disconnect the airbuds by bluetoothctl (you must add your earbud's mac direction)
    this are the steps to get the mac direction from any bluetooth device:
        * first you must install bluez on your respective distro
        * then you do the following command:
         ```bluetoothctl scan on```
        * when you see the the mac direction associated to your devices name, then you copy it to the combine.sh script on the pertinent sections
-A python script which takes all the action from bash script

-A glade script (you must install glade if you don't have it) which provides all the (very few) ui components

thanks for reading lad!

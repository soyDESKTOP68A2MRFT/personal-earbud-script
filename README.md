![SCREENGITHUB](https://github.com/user-attachments/assets/7b603180-033e-41be-8d67-82db0c4d7de7)
# personal-earbud-script
a set of utilities to sync, connect and disconnect ANY airbuds

this utilities consist on:

-A bash script for connect, sync and disconnect the airbuds by bluetoothctl (you must add your earbud's mac direction)
    this are the steps to get the mac direction from any bluetooth device:
    
* first you must install bluez on your respective distro
* then you do the following command:


        
      bluetoothctl scan on


* when you see the mac asociated to your device you must copy it to the bash script on pertinent sections
  
* the script is thought for the cases in which we have 2 earbuds with failiures on syncronization, feel free to do modifications on the script (BY YOURSELF) and if you have any problem with the script, let me know by creating an issue describing the problem 
-A python script which takes all the action from bash script

-A glade script (you must install glade if you don't have it) which provides all the (very few) ui components

thanks for reading lad!

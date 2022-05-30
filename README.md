
# CAN Listener
This is Python script that listens to the CAN-Bus and writes the data into SQLite database
```sh
sudo cp CAN_Listener.service /etc/systemd/system/CAN_Listener.service
sudo systemctl enable CAN_Listener.service
sudo systemctl start CAN_Listener.service
systemctl status CAN_Listener.service
```
configuration help:
https://experimentalavionics.com/raspberry-pi-can-bus-interface/

# Stratux Listener
This is Python script that listens to Stratux GDL90 messages and writes the data into SQLite database (soon). 
```sh
sudo cp Stratux_Listener.service /etc/systemd/system/Stratux_Listener.service
sudo systemctl enable Stratux_Listener.service
sudo systemctl start Stratux_Listener.service
systemctl status Stratux_Listener.service
```

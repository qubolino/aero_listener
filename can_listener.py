#!/usr/bin/python3
#

import can
import time
import os
import sqlite3
import struct

#get the database ready
memdb = sqlite3.connect('/memdb/memdb.db')
cursor = memdb.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS  messages(id INTEGER PRIMARY KEY AUTOINCREMENT, CANid INT, Param_Text varchar(50), Param_Value REAL,  msg TEXT, timestamp REAL)
''')
memdb.commit()
cursor.execute('''
    CREATE UNIQUE INDEX IF NOT EXISTS data_idx ON messages(CANid, Param_Text)
''')
memdb.commit()


cursor.execute('''PRAGMA journal_mode=WAL''')

# populate table with known parameters

#Msg. 25 Time broadcast
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (25, "TimeSync", 0, time.time() ))
#Msg. 40 from Module A (Air pressure and stuff)
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (40, "Airspeed", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (40, "Altitude", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (40, "VerticalSpeed", 0, time.time() ))
#Msg. 41 from Module A (Angle of Attack)
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (41, "AoA", 0, time.time() ))
#Msg. 42 Outside Air Temperature, and Humidity
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (42, "OAT", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (42, "Humidity", 0, time.time() ))
#Msg. 43 from Module A (Raw Statick pressure and the sensor's temperature)
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (43, "RawStaticPressure", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (43, "RawSensorTemperature", 0, time.time() ))
#Msg. 46 QNH
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (46, "QNH", 0, time.time() ))
#Msg. 50 Engine stuff
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (50, "RPM", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (50, "FuelPressure", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (50, "FuelFlow", 0, time.time() ))
#Msg. 72 Giro data
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (72, "Heading", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (72, "Roll", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (72, "Pitch", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (72, "TurnRate", 0, time.time() ))
#Msg. 73 Acceleration
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (73, "AccX", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (73, "AccY", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (73, "AccZ", 0, time.time() ))
#Msg. 80 Fuel Levels
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (80, "FuelTank1", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (80, "FuelTank2", 0, time.time() ))
#Msg. 81 Oil Temperature and pressure
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (81, "OilPressure", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (81, "OilTemperature", 0, time.time() ))
#Msg. 82 EGT 1&2 + CHT 1&2
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (82, "EGT1", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (82, "EGT2", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (82, "CHT1", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (82, "CHT2", 0, time.time() ))
#Msg. 83 EGT 3&4 + CHT 3&4
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (83, "EGT3", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (83, "EGT4", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (83, "CHT3", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (83, "CHT4", 0, time.time() ))
#Msg. 84 EGT 5&6 + CHT 5&6
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (84, "EGT5", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (84, "EGT6", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (84, "CHT5", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (84, "CHT6", 0, time.time() ))
#Msg. 85 Electric stuff Voltage and Current
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (85, "Volts", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (85, "AmpsAlternator", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (85, "AmpsBattery", 0, time.time() ))
#Msg. 99 GPS Lat/Lon
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (99, "GPS_Lat", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (99, "GPS_Lon", 0, time.time() ))
#Msg. 100 GPS GS, ALT, Tracking True and Magnetic
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (100, "GPS_GS", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (100, "GPS_Alt", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (100, "GPS_TRK_T", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (100, "GPS_TRK_M", 0, time.time() ))
#Msg. 112 Engine Time and Flight Switch time
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (112, "EngineTimeTacho", 0, time.time() ))
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (112, "EngineTimeClock", 0, time.time() ))
#Msg. 114 Airswitch (Flight time)
cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (120, "Airswitch", 0, time.time() ))

memdb.commit()



try:
	bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
	print('Cannot find CAN board.')
	exit()

print('Ready')

def update_message(value, timestamp, can_id, param_name):
	cursor.execute('''UPDATE messages SET Param_Value=?, timestamp=? WHERE CANid=? and Param_Text=?''', (value, timestamp, can_id, param_name))
			

try:
	while True:
# maybe use
#               for msg in bus:
#                   print(msg.data)
# instead
		message = bus.recv()	# Wait until a message is received.
		s=''
		c = '{0:f} {1:x} {2:x} '.format(message.timestamp, message.arbitration_id, message.dlc)

		CANid = message.arbitration_id
		if CANid == 25:
			timesync = struct.unpack('l', message.data[:4])[0]
			update_message(timesync, message.timestamp, CANid, "TimeSync")
			memdb.commit()
		elif CANid == 40:
			# cansend can0 028#004100F100040000
			Airspeed = struct.unpack('h', message.data[:2])[0]
			update_message(Airspeed, message.timestamp, CANid, 'Airspeed')
			Altitude = struct.unpack('h', message.data[2:4])[0]  # meters
			Altitude *= 3.28084  # feet
			update_message(Altitude, message.timestamp, CANid, 'Altitude')
			VerticalSpeed = struct.unpack('h', message.data[5:7])[0]
			update_message(VerticalSpeed, message.timestamp, CANid, 'VerticalSpeed')
			memdb.commit()
		elif CANid == 41:
			update_message(struct.unpack('h', message.data[:2])[0],  message.timestamp, CANid, "AoA")
			memdb.commit()
		elif CANid == 42:
			OAT = struct.unpack('h', message.data[:2])[0]
			OAT = OAT / 10
			update_message(OAT, message.timestamp, CANid, 'OAT')
			update_message(message.data[2], message.timestamp, CANid, "Humidity")
			memdb.commit()
		elif CANid == 43:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "RawStaticPressure")
			update_message(message.data[2], message.timestamp, CANid, "RawSensorTemperature")
			memdb.commit()
		elif CANid == 46:
			#cansend can0 02E#0004000000000000
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "QNH")
			memdb.commit()
		elif CANid == 50:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "RPM")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "FuelPressure")
			update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "FuelFlow")
			memdb.commit()
		elif CANid == 72:
			update_message(struct.unpack('h', message.data[:2])[0], message.timestamp, CANid, "Heading")
			Roll = struct.unpack('h', message.data[2:4])[0]
			update_message(Roll, message.timestamp, CANid, "Roll")
			Pitch = struct.unpack('h', message.data[4:6])[0]
			update_message(Pitch, message.timestamp, CANid, "Pitch")
			TurnRate = struct.unpack('h', message.data[6:8])[0]
			update_message(TurnRate, message.timestamp, CANid, "TurnRate")
			memdb.commit()
		elif CANid == 73:
			AccX = struct.unpack('h', message.data[:2])[0]
			update_message(AccX, message.timestamp, CANid, "AccX")
			AccY = struct.unpack('h', message.data[2:4])[0]
			update_message(AccY, message.timestamp, CANid, "AccY")
			AccZ = struct.unpack('h', message.data[4:6])[0]
			update_message(AccZ, message.timestamp, CANid, "AccZ")
			memdb.commit()
		elif CANid == 80:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "FuelTank1")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "FuelTank2")
			memdb.commit()
		elif CANid == 81:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "OilPressure")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "OilTemperature")
			memdb.commit()
		elif CANid == 82:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "EGT1")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "EGT2")
			update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "CHT1")
			update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "CHT2")
			memdb.commit()
		elif CANid == 83:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "EGT3")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "EGT4")
			update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "CHT3")
			update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "CHT4")
			memdb.commit()
		elif CANid == 84:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "EGT5")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "EGT6")
			update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "CHT5")
			update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "CHT6")
			memdb.commit()
		elif CANid == 85:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "Volts")
			AmpsAlternator = struct.unpack('h', message.data[2:4])[0]
			update_message(AmpsAlternator, message.timestamp, CANid, "AmpsAlternator")
			AmpsBattery = struct.unpack('h', message.data[4:6])[0]
			update_message(AmpsBattery, message.timestamp, CANid, "AmpsBattery")
			memdb.commit()
		elif CANid == 99:
			Lat = struct.unpack('l', message.data[:4])[0]
			Lon = struct.unpack('l', message.data[4:8])[0]
			Lat = Lat/1000000
			Lon = Lon/1000000
			update_message(Lat, message.timestamp, CANid, 'GPS_Lat')
			update_message(Lon, message.timestamp, CANid, 'GPS_Lon')
			memdb.commit()
		elif CANid == 100:
			update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "GPS_GS")
			update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "GPS_Alt")
			update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "GPS_TRK_T")
			update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "GPS_TRK_M")
			memdb.commit()
		elif CANid == 112:
			update_message(struct.unpack('L', message.data[:4])[0], message.timestamp, CANid, "EngineTimeTacho")
			update_message(struct.unpack('l', message.data[4:8])[0], message.timestamp, CANid, "EngineTimeClock")
			memdb.commit()
		elif CANid == 114:
			update_message(struct.unpack('L', message.data[:4])[0], message.timestamp, CANid, "Airswitch")
			memdb.commit()
		else:
			for i in range(message.dlc ):
				s +=  '{0:x} '.format(message.data[i])
			update_message(s, CANid, message.timestamp, "unknown")
			memdb.commit()


except KeyboardInterrupt:
	print('\n\rKeyboard interrupt')

#!/usr/bin/python3
#

import can
import time
import os
import db
import struct

db.init_db()

try:
	bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except OSError:
	print('Cannot find CAN board.')
	exit()

print('Ready')
			

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
			db.update_message(timesync, message.timestamp, CANid, "TimeSync")
			db.memdb.commit()
		elif CANid == 40:
			# cansend can0 028#004100F100040000
			Airspeed = struct.unpack('h', message.data[:2])[0]
			db.update_message(Airspeed, message.timestamp, CANid, 'Airspeed')
			Altitude = struct.unpack('h', message.data[2:4])[0]  # meters
			Altitude *= 3.28084  # feet
			db.update_message(Altitude, message.timestamp, CANid, 'Altitude')
			VerticalSpeed = struct.unpack('h', message.data[5:7])[0]
			db.update_message(VerticalSpeed, message.timestamp, CANid, 'VerticalSpeed')
			db.memdb.commit()
		elif CANid == 41:
			db.update_message(struct.unpack('h', message.data[:2])[0],  message.timestamp, CANid, "AoA")
			db.memdb.commit()
		elif CANid == 42:
			OAT = struct.unpack('h', message.data[:2])[0]
			OAT = OAT / 10
			db.update_message(OAT, message.timestamp, CANid, 'OAT')
			db.update_message(message.data[2], message.timestamp, CANid, "Humidity")
			db.memdb.commit()
		elif CANid == 43:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "RawStaticPressure")
			db.update_message(message.data[2], message.timestamp, CANid, "RawSensorTemperature")
			db.memdb.commit()
		elif CANid == 46:
			#cansend can0 02E#0004000000000000
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "QNH")
			db.memdb.commit()
		elif CANid == 50:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "RPM")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "FuelPressure")
			db.update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "FuelFlow")
			db.memdb.commit()
		elif CANid == 72:
			db.update_message(struct.unpack('h', message.data[:2])[0], message.timestamp, CANid, "Heading")
			Roll = struct.unpack('h', message.data[2:4])[0]
			db.update_message(Roll, message.timestamp, CANid, "Roll")
			Pitch = struct.unpack('h', message.data[4:6])[0]
			db.update_message(Pitch, message.timestamp, CANid, "Pitch")
			TurnRate = struct.unpack('h', message.data[6:8])[0]
			db.update_message(TurnRate, message.timestamp, CANid, "TurnRate")
			db.memdb.commit()
		elif CANid == 73:
			AccX = struct.unpack('h', message.data[:2])[0]
			db.update_message(AccX, message.timestamp, CANid, "AccX")
			AccY = struct.unpack('h', message.data[2:4])[0]
			db.update_message(AccY, message.timestamp, CANid, "AccY")
			AccZ = struct.unpack('h', message.data[4:6])[0]
			db.update_message(AccZ, message.timestamp, CANid, "AccZ")
			db.memdb.commit()
		elif CANid == 80:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "FuelTank1")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "FuelTank2")
			db.memdb.commit()
		elif CANid == 81:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "OilPressure")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "OilTemperature")
			db.memdb.commit()
		elif CANid == 82:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "EGT1")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "EGT2")
			db.update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "CHT1")
			db.update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "CHT2")
			db.memdb.commit()
		elif CANid == 83:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "EGT3")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "EGT4")
			db.update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "CHT3")
			db.update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "CHT4")
			db.memdb.commit()
		elif CANid == 84:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "EGT5")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "EGT6")
			db.update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "CHT5")
			db.update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "CHT6")
			db.memdb.commit()
		elif CANid == 85:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "Volts")
			AmpsAlternator = struct.unpack('h', message.data[2:4])[0]
			db.update_message(AmpsAlternator, message.timestamp, CANid, "AmpsAlternator")
			AmpsBattery = struct.unpack('h', message.data[4:6])[0]
			db.update_message(AmpsBattery, message.timestamp, CANid, "AmpsBattery")
			db.memdb.commit()
		elif CANid == 99:
			Lat = struct.unpack('l', message.data[:4])[0]
			Lon = struct.unpack('l', message.data[4:8])[0]
			Lat = Lat/1000000
			Lon = Lon/1000000
			db.update_message(Lat, message.timestamp, CANid, 'GPS_Lat')
			db.update_message(Lon, message.timestamp, CANid, 'GPS_Lon')
			db.memdb.commit()
		elif CANid == 100:
			db.update_message(struct.unpack('H', message.data[:2])[0], message.timestamp, CANid, "GPS_GS")
			db.update_message(struct.unpack('H', message.data[2:4])[0], message.timestamp, CANid, "GPS_Alt")
			db.update_message(struct.unpack('H', message.data[4:6])[0], message.timestamp, CANid, "GPS_TRK_T")
			db.update_message(struct.unpack('H', message.data[6:8])[0], message.timestamp, CANid, "GPS_TRK_M")
			db.memdb.commit()
		elif CANid == 112:
			db.update_message(struct.unpack('L', message.data[:4])[0], message.timestamp, CANid, "EngineTimeTacho")
			db.update_message(struct.unpack('l', message.data[4:8])[0], message.timestamp, CANid, "EngineTimeClock")
			db.memdb.commit()
		elif CANid == 114:
			db.update_message(struct.unpack('L', message.data[:4])[0], message.timestamp, CANid, "Airswitch")
			db.memdb.commit()
		else:
			for i in range(message.dlc ):
				s +=  '{0:x} '.format(message.data[i])
			db.update_message(s, CANid, message.timestamp, "unknown")
			db.memdb.commit()


except KeyboardInterrupt:
	print('\n\rKeyboard interrupt')

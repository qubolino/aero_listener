import sqlite3
import time


#get the database ready
memdb = sqlite3.connect('/memdb/memdb.db')
cursor = memdb.cursor()


def create_message(can_id, param_name, default_val=0, default_time=time.time()):
	cursor.execute('''INSERT OR REPLACE  INTO messages(CANid, Param_Text, Param_Value, timestamp) VALUES(?,?,?,?)''', (can_id, param_name, default_val, default_time))
			
            
def update_message(value, timestamp, can_id, param_name):
	cursor.execute('''UPDATE messages SET Param_Value=?, timestamp=? WHERE CANid=? and Param_Text=?''', (value, timestamp, can_id, param_name))
			


def init_db():
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
    create_message(25, "TimeSync", 0, time.time())
    #Msg. 40 from Module A (Air pressure and stuff)
    create_message(40, "Airspeed", 0, time.time())
    create_message(40, "Altitude", 0, time.time())
    create_message(40, "VerticalSpeed", 0, time.time())
    #Msg. 41 from Module A (Angle of Attack)
    create_message(41, "AoA", 0, time.time())
    #Msg. 42 Outside Air Temperature, and Humidity
    create_message(42, "OAT", 0, time.time())
    create_message(42, "Humidity", 0, time.time())
    #Msg. 43 from Module A (Raw Statick pressure and the sensor's temperature)
    create_message(43, "RawStaticPressure", 0, time.time())
    create_message(43, "RawSensorTemperature", 0, time.time())
    #Msg. 46 QNH
    create_message(46, "QNH", 0, time.time())
    #Msg. 50 Engine stuff
    create_message(50, "RPM", 0, time.time())
    create_message(50, "FuelPressure", 0, time.time())
    create_message(50, "FuelFlow", 0, time.time())
    #Msg. 72 Giro data
    create_message(72, "Heading", 0, time.time())
    create_message(72, "Roll", 0, time.time())
    create_message(72, "Pitch", 0, time.time())
    create_message(72, "TurnRate", 0, time.time())
    #Msg. 73 Acceleration
    create_message(73, "AccX", 0, time.time())
    create_message(73, "AccY", 0, time.time())
    create_message(73, "AccZ", 0, time.time())
    #Msg. 80 Fuel Levels
    create_message(80, "FuelTank1", 0, time.time())
    create_message(80, "FuelTank2", 0, time.time())
    #Msg. 81 Oil Temperature and pressure
    create_message(81, "OilPressure", 0, time.time())
    create_message(81, "OilTemperature", 0, time.time())
    #Msg. 82 EGT 1&2 + CHT 1&2
    create_message(82, "EGT1", 0, time.time())
    create_message(82, "EGT2", 0, time.time())
    create_message(82, "CHT1", 0, time.time())
    create_message(82, "CHT2", 0, time.time())
    #Msg. 83 EGT 3&4 + CHT 3&4
    create_message(83, "EGT3", 0, time.time())
    create_message(83, "EGT4", 0, time.time())
    create_message(83, "CHT3", 0, time.time())
    create_message(83, "CHT4", 0, time.time())
    #Msg. 84 EGT 5&6 + CHT 5&6
    create_message(84, "EGT5", 0, time.time())
    create_message(84, "EGT6", 0, time.time())
    create_message(84, "CHT5", 0, time.time())
    create_message(84, "CHT6", 0, time.time())
    #Msg. 85 Electric stuff Voltage and Current
    create_message(85, "Volts", 0, time.time())
    create_message(85, "AmpsAlternator", 0, time.time())
    create_message(85, "AmpsBattery", 0, time.time())
    #Msg. 99 GPS Lat/Lon
    create_message(99, "GPS_Lat", 0, time.time())
    create_message(99, "GPS_Lon", 0, time.time())
    #Msg. 100 GPS GS, ALT, Tracking True and Magnetic
    create_message(100, "GPS_GS", 0, time.time())
    create_message(100, "GPS_Alt", 0, time.time())
    create_message(100, "GPS_TRK_T", 0, time.time())
    create_message(100, "GPS_TRK_M", 0, time.time())
    #Msg. 112 Engine Time and Flight Switch time
    create_message(112, "EngineTimeTacho", 0, time.time())
    create_message(112, "EngineTimeClock", 0, time.time())
    #Msg. 114 Airswitch (Flight time)
    create_message(120, "Airswitch", 0, time.time())

    memdb.commit()


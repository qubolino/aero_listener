
import time
import gdl90
import socket
import struct
import math
import db

if __name__ == "__main__" :

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 4000))

    while True:
        msg, adr = s.recvfrom(8192)
        msg = gdl90.decodeGDL90(msg)

        if len(msg) < 1:
            continue

        if msg[0] == 0x4c:
            roll      = struct.unpack('>h', msg[4:6])[0]/10.0
            pitch     = struct.unpack('>h', msg[6:8])[0]/10.0
            heading   = struct.unpack('>h', msg[8:10])[0]/10.0
            slipskid  = struct.unpack('>h', msg[10:12])[0]/10.0
            yawrate   = struct.unpack('>h', msg[12:14])[0]/10.0
            g         = struct.unpack('>h', msg[14:16])[0]/10.0
            ias       = struct.unpack('>h', msg[16:18])[0]/10.0
            alt       = struct.unpack('>h', msg[18:20])[0] - 5000.5
            vs        = struct.unpack('>h', msg[20:22])[0]

            print(roll, pitch, heading, slipskid, yawrate, g, ias, alt, vs)

            db.update_message(roll, time.time(), 72, "Roll")
            db.update_message(pitch, time.time(), 72, "Pitch")
            db.memdb.commit()

            # self.parent.db_write("PITCH", pitch)
            # self.parent.db_write("ROLL", roll)
            # self.parent.db_write("HEAD", heading)

            # self.parent.db_write("ALAT", -math.sin(slipskid*math.pi/180))
            # self.parent.db_write("ALT", alt)
            # self.parent.db_write("VS", vs)
        elif msg[0] == 0x0a:
            # ownship report
            alt = struct.unpack('>h', msg[11:13])[0]
            tmp = struct.unpack('BB', msg[14:16])
            gnd_speed = (tmp[0] << 4) | (tmp[1] >> 4)
            # self.parent.db_write("IAS", gnd_speed)
            print(alt, gnd_speed)

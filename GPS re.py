import socket
from datetime import datetime
from pynmeagps.nmeareader import NMEAReader


def read(stream: socket.socket):
    """
    Reads and parses NMEA message from socket stream.
    """

    msgcount = 0
    start = datetime.now()

    nmr = NMEAReader(
        stream,
    )
    try:
        for (_, parsed_data) in nmr:
            print(parsed_data.lat, ",",parsed_data.lon )
            msgcount += 1
    except KeyboardInterrupt:
        dur = datetime.now() - start
        secs = dur.seconds + dur.microseconds / 1e6
        print("Session terminated by user")
        print(
            f"{msgcount:,d} messages read in {secs:.2f} seconds:",
            f"{msgcount/secs:.2f} msgs per second",
        )


if __name__ == "__main__":

    SERVER = "YOUR IP"
    PORT = 5050

    print(f"Opening socket {SERVER}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((SERVER, PORT))
        read(sock)

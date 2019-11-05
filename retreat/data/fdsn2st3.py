"""fdsn2st3.py"""
import time
import sys
from obspy.clients.fdsn import Client

def fdsn2st(scnl, myclient, t, length, logfile):
    """
    Fetches a stream object from server using FDSN client

    Args:
        scnl (dict): Dictionary containing desired SCNL values for the stream
        myclient (str): Name of client (default="IRIS"")
        t (UTCDateTime): Desired stream start time
        length (float): Desired length of stream in seconds
        logfile (str): name and path to the logfile

    Returns:
        st (stream): obspy stream object containing retrieved data
    """
    # redirect output to log file:
    sys.stdout = open(logfile, 'a+')
    sys.stderr = sys.stdout

    max_retries = 5
    nsleep = 10 # seconds to wait before retrying

    client = Client(myclient)

    for _ in range(max_retries):

        try:
                # ... do stuff ...
            print("Connecting to server...")
            st = client.get_waveforms(scnl["N"], scnl["S"], scnl["L"], scnl["C"], t, t + length)
        except Exception as e:
            # ... log it, sleep, etc. ...
            print('Connection error: '+ str(e))
            #logging.error('Connection error: '+ str(e))
            print("Will retry in ", str(nsleep), "s")
            #logging.info("Will retry in %ss", nsleep)
            time.sleep(nsleep)
            continue
        else:
            break
    else:
        print("Can't connect to server. Giving up")
        raise SystemExit("Can't connect to server. Giving up")

#	st = client.get_waveforms(scnl["N"], scnl["S"], scnl["L"], scnl["C"], t, t + length)

    return st

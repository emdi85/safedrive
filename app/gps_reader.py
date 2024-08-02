import gps

def get_gps_data():
    session = gps.gps(mode=gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    while True:
        try:
            report = session.next()
            if report['class'] == 'TPV' and hasattr(report, 'lat') and hasattr(report, 'lon'):
                yield report.lat, report.lon
        except KeyError:
            pass
        except KeyboardInterrupt:
            break
        except StopIteration:
            session = None
            print("GPSD has terminated")

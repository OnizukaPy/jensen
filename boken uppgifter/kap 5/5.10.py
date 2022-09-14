import datetime

dt = datetime.datetime.now()
print(dt)
d = str(dt.date())
t = str(dt.time())
print("Dagens datum:\t", d)
print("Klockan är:\t", t[:8])
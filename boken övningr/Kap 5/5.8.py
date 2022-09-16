import datetime as dt

time = str(dt.datetime.now().time())[:5]
timmar = int(time[:2])
minuter = int(time[3:])

total_minuter = timmar*60 + minuter

new_time = input("Skriv en tid som tt:mm: ")

new_timmar = int(new_time[:2])
new_minuter = int(new_time[3:])

total_new_minuter = new_timmar*60 + new_minuter
print(f"\nDet finns {total_new_minuter - total_minuter} minuter mellan de två tidpunkterna\n")

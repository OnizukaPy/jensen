import random

# att skapa en randomisk heltals lista
temperature_list = []
temp_list = []
mät_n = random.randint(1, 30)

for i in range(mät_n):
    t = random.randint(-10, 50)
    temperature_list.append([f"Mätstation n.{i+1}", t])
    temp_list.append(t)

m = sum(temp_list)/len(temp_list)
print(f"\nDen medeltemperaturen är {m:.2f}°C\n")

for i in range(len(temperature_list)):
    if temperature_list[i][1] > m:
        print(f"Temperaturen av {temperature_list[i][1]}°C uppmätts från {temperature_list[i][0]} är högre än medel")

print("\n")
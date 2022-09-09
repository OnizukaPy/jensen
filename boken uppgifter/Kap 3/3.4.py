t = float(input("Temp?: "))
if t < 18:
    print("Sätt på jackan!")
    print("Sätt på värmen ")
    if t < 12 and t > 0:
        print("Det är kallt")
    elif t < 0:
        print("Det är svinkallt")

else:
    print("Det är varmt")
    if t >= 22 and t < 50:
        print("Stäng av värmen")
    elif t>= 50:
        print("Det är ökenhett!")
print(f"Det är {t:.1f} grader")
a = 45
b = 40
c = 35
d = 30
e = 25
max = 50

poäng = int(input("Skriv dina poängar: "))

if poäng <= e:
    betyg = "E"
elif poäng > e and poäng <= d:
    betyg = "D"
elif poäng > d and poäng <= c:
    betyg = "C"
elif poäng > c and poäng <= b:
    betyg = "B"
elif poäng > a and poäng <= max:
    betyg = "A"
else:
    betyg = "N/A"

print(betyg)
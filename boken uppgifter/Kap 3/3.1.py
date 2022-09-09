abbonament = 15             # 15 kr per minut
minuter = int(input("hur måmga minuter använder du varje månad?: "))
rabbat = 0.1
minst = 300

total = minuter * abbonament

if total <= minst:
    total = total * (1- rabbat)
    print(f"Du måste betala {total} kr varje månad. Tyvärr utan rabbat.")
else:
    print(f"Du måste betala {total} kr varje månad. Grattis du har rabbat av {total*rabbat}!.")


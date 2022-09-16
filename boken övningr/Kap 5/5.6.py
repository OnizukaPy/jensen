text1 = input("Skriv en text: ").strip().lower()
text2 = input("Skriv en annan text: ").strip().lower()

if sorted(text1) == sorted(text2):
    print("\nDe är två anagrammar\n")
else:
    print("\nDe är inte två anagrammar\n")

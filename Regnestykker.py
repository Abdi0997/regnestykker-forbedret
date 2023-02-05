import random

def generate_question():
    # Liste over mulige operationer
    operationer = ["+", "-", "*", "/"]
    # vælg en tilfældig operation
    operation = random.choice(operationer)
    # Generer to tilfældige tal mellem 1 og 10
    num1 = random.randint(5, 10)
    num2 = random.randint(1, 4)
    # Opret spørgsmålstrengen
    spørgsmål = f"Hvad er {num1} {operation} {num2}?"
    # Returnér spørgsmålet og svaret (evalueret)
    return spørgsmål, eval(f"{num1} {operation} {num2}")

# Variabel til at tælle antallet af korrekte svar
rigtige_svar = 0
# Spørg 10 gange
for i in range(10):
    # Generer et spørgsmål
    spørgsmål, svar = generate_question()
    print(spørgsmål)
    # Tag svaret fra brugeren
    bruger_svar = input("Dit svar: ")
    # Tjek om svaret er korrekt
    if float(bruger_svar) == svar:
        print("Korrekt!")
        rigtige_svar += 1
    else:
        print("Forkert!")
    print()

# Print det samlede antal rigtige svar
print(f"Du fik {rigtige_svar} ud af 10 rigtige.")

# Tjek antallet af korrekte svar og giv et svar baseret på det
if rigtige_svar >= 8:
   print("Du er god til matematik")
elif rigtige_svar >= 5:
    print("Du er okay til matematik")
else:
    print("Du er dårlig til matematik")
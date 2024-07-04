import random

print("Tossing a coin...")
heads = 0
tails = 0

for i in range(1, 4):
    result = random.choice(["Heads", "Tails"])
    print(f"Round {i}: {result}")
    if result == "Heads":
        heads += 1
    else:
        tails += 1

print(f"Heads: {heads}, Tails: {tails}")

if heads > tails:
    print("You won")
else:
    print("You lost")
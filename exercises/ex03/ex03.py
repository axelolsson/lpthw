# PEMDAS (parenthesis, exponents, multiplication, division, addition, subtraction) PE(M&D)(A&S)
print("I will now count my chickens:")

 # 25 + (30 / 6) => 25 + (5) => 30
print("Hens", 25 + 30 / 6)

 # 100 - ((25 * 3) % 4) => 100 - (75 % 4) => 100 - (3) => 97
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

# (3 + 2 + (1 - 5)) + (((4 % 2) - 1) / 4) + 6 => (3 + 2 + (1 - 5)) + (-0.25 + 6) => (5 + (-4)) + (5.75) => 1 + 5.75 => 6.75
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 -7?")

# False since this evaluates as (5 + 2) < (5 - 7) => 5 < -2
print(3 + 2 < 5 - 7)

print("What is 3 + 2", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

# True
print("Is it greater?", 5 > -2)

# Also True
print("Is it great or equal?", 5 >= -2)

# False
print("Is it less or equal?", 5 <= 2)



name = 'Axel Olsson'
age = 30
height_inches = 76
height_metric = round(height_inches *  2.54)
weight_lbs = 220
weight_kgs = round(weight_lbs * 0.45)
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inces tall.")
print(f"That's {height_metric} cms tall.")
print(f"He's {weight_lbs} pounds heavy.")
print(f"That's {weight_kgs} kgs heavy.")
print("Actually that is pretty heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_inches + weight_lbs

print(f"If I add {age}, {height_inches}, and {weight_lbs} I get {total}.")
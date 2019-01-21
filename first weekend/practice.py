ages = {"Alice":22, "Bob":27}
ages["Charlie"] = 28
print(ages)
del ages["Charlie"]
print(ages)
name = input("Who do you want to look up?")

try: 
	print(f"{name} is {ages[name]} years old")
except KeyError:
	print(f"Sorry, {name} is not in the dictionary.")

# main(): 
# 	print(square)

# def square(x):
# 		return x * x

# print(suare(10))

# How to handle exceptions

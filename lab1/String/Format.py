#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)
#Modifier|changes the value
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Placeholder|do some operations within the brakes
txt = f"The price is {20 * 59} dollars"
print(txt)

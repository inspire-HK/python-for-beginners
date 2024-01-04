# Python String Formatting
# https://www.w3schools.com/python/python_string_formatting.asp

price = 49.00
qty = 6
txt = "The price is {} dollars for {} pcs"
print(txt.format(qty, price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

## f-string
age = 23
name = 'John'
print(f"Hello, My name is {name} and I'm {age} years old.")

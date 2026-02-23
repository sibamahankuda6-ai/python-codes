# name=input("enter your name")
# date= input("enter the date")
# print(f"Dear {name},you are selected! {date}")

letter="""Dear <|name|>,
you are selected!
<|date|>
"""
print(letter.replace("<|name|>","siba").replace("<|date|>","22 october 2004")) #chaining replace function
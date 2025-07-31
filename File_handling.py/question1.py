records = [
    {'name': "rice", 'price': 120, 'category': "grocery"},
    {'name': "sugar", 'price': 220, 'category': "grocery"},
    {'name': "wheat", 'price': 320, 'category': "grocery"},
    {'name': "cereal", 'price': 420, 'category': "grocery"},
]

with open("grocery.txt", "w") as f:
    f.write("ID\tNAME\tPRICE\tCATEGORY\n")
    i = 1
    for item in records:
        line = f"{i}\t{item['name']}\t{item['price']}\t{item['category']}\n"
        f.write(line)
        i += 1
    print("\nGrocery.txt file is created and the data are written inside the grocery.txt file")

print("\nReading data from grocery.txt:\n")
with open("grocery.txt", "r") as f:
    content = f.read()
    print(content)

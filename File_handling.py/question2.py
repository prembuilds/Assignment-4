f = open("demo.txt", "w")
f.write("Hello, this is a demo file.")
f.close()

f = open("demo.txt", "r")
print("File content:", f.read())

f.seek(0)
print("After seek(0):", f.read())

f.seek(7)
print("After seek(7):", f.read())

f.close()

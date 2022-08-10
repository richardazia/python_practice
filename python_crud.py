f = open("tasks.txt", "a")

f.write("\nText added to the file via python")
f.close()

f = open("tasks.txt", "r")
print(f.read())

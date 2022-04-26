from concurrent.futures import process
a=str(input("Enter a Special Char to encode: "))
process = (a.encode().hex().upper())
f1 = "EF%BC%"
print(f1+process)

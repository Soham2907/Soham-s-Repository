print("THIS CALCULATOR ENABLES YOU TO PERFORM SIMPLE ARITHMETIC OPERATIONS")
print(" ")

a = int(input("Enter any number: "))
b = int(input("Enter one more number: "))

print(" ")

print("This is the sum of the 2 numbers: {}".format(a+b))
print("This is the difference of the 2 numbers: {}".format(a-b))
print("This is the product of the 2 numbers: {}".format(a*b))

if b != 0:
  print("This is the quotient {} divided by {}: {}".format(a, b, a+b))

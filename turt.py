# Prompt the user for the coefficients of the two equations
print("Enter the coefficients of the first equation (a1, b1, c1):")
a1, b1, c1 = map(int, input().split())

print("Enter the coefficients of the second equation (a2, b2, c2):")
a2, b2, c2 = map(int, input().split())

# Calculate the determinant of the system
det = a1 * b2 - a2 * b1

# Prompt the user for the operation to perform
print("1. Find the number of solutions")
print("2. Find the point of intersection")
print("3. Quit")

choice = int(input())

if choice == 1:
  # If the determinant is zero, there are infinite solutions
  if det == 0:
    print("The system has infinite solutions")
  else:
    # If the determinant is non-zero, there is exactly one solution
    print("The system has a unique solution")
elif choice == 2:
  # If the determinant is zero, there is no unique solution
  if det == 0:
    print("The system has no unique solution")
  else:
    # If the determinant is non-zero, we can find the unique solution
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    print("The solution is ({}, {})".format(x, y))
else:
  print("Invalid choice")

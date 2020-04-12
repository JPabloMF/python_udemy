# FOR
numbers = [1, 2, 3, 4, 5]
people = ["Nick","Someone","Another person"]

for item in numbers:
  print(item)

for person in people:
  print("This persons name is",person)

run = True
current = 1

# WHILE
while run:
  if current == 100:
    run = False
  else:
    print(current)
    current += 1
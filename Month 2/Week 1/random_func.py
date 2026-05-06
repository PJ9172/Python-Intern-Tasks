import random

# Returns a random number between the given range
print(random.randint(1, 100))
# Alternate randrange()

# Returns a random element from the given sequence
print(random.choice(["Python", "Go", "Java"]))

# Returns a list with a random selection from the given sequence
print(random.choices(["Python", "Go", "Java", "CPP", "C#"]))

# Returns a random float number between 0 and 1
print(random.random())

# Returns a random float number between two given parameters
print(random.uniform(20, 60))

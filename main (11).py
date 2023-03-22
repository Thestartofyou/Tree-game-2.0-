import random

# List of trees, their fun facts, and whether they are edible
trees = [
  ('oak', 'Oaks are the most common type of tree in the world.', False),
  ('maple', 'Maple trees are known for their colorful autumn foliage.', False),
  ('pine', 'Pine trees produce pine cones and have needles instead of leaves.', True),
  ('redwood', 'Redwood trees are the tallest trees in the world.', False)
]

# Welcome message
print("Welcome to the Tree Identification Game!")

# Game loop
while True:
  # Choose a random tree and its fun fact
  tree, fact, edible = random.choice(trees)
  
  # Prompt the user to identify the tree
  guess = input(f"What kind of tree is this: {tree}? ")
  
  # Check if the guess is correct
  if guess.lower() == tree:
    print("Correct!")
  else:
    print("Incorrect. Better luck next time!")
  
  # Print the fun fact
  print(fact)
  
  # Print a message about whether the tree is edible
  if edible:
    print("Did you know that the seeds or nuts from this tree are edible?")
  else:
    print("This tree is not edible.")
    
  # Ask the user if they want to play again
  play_again = input("Would you like to play again (y/n)? ")
  if play_again.lower() != 'y':
    break
    
print("Thanks for playing!")
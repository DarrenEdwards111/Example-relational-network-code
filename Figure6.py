# Define the sets F and W
F = {'snake'}
W = set()

# Define the function T
def T(x):
  if x == 'snake':
    W.add('wood')

# Apply the function T to the set F
for x in F:
  T(x)

# Print the resulting set W
print(W)

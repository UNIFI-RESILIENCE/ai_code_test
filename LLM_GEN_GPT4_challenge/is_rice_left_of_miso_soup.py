# Read the input string representing the arrangement of the plates
S = input()

# Find the index of the rice plate ('R')
rice_index = S.index('R')

# Find the index of the miso soup plate ('M')
miso_index = S.index('M')

# Check if the rice plate is to the left of the miso soup plate
if rice_index < miso_index:
    print("Yes")
else:
    print("No")
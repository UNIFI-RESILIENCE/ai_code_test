# Read the input string S from standard input
S = input().strip()

# Find the indices of rice (R) and miso soup (M) in the string S
index_of_rice = S.find('R')
index_of_miso_soup = S.find('M')

# Check if the plate of rice is to the left of the plate of miso soup
if index_of_rice < index_of_miso_soup:
    # If the condition is true, print "Yes"
    print("Yes")
else:
    # If the condition is false, print "No"
    print("No")
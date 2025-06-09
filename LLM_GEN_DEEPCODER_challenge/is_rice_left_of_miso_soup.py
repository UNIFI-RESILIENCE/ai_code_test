# Read the input string
S = input().strip()

# Find the positions of 'R' (rice) and 'M' (miso soup)
r_pos = S.find('R')
m_pos = S.find('M')

# Check if 'R' is to the left of 'M'
if r_pos < m_pos:
    print("Yes")
else:
    print("No")
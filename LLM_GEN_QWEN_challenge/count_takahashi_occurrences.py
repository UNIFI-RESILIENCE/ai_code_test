def main():
    # Read the number of strings, N, from standard input
    N = int(input().strip())
    
    # Initialize a counter for the occurrences of "Takahashi"
    taka_count = 0
    
    # Loop through each of the N lines to read the strings S_i
    for _ in range(N):
        # Read the current string from standard input
        S_i = input().strip()
        
        # Check if the current string is equal to "Takahashi"
        if S_i == "Takahashi":
            # Increment the counter if the condition is true
            taka_count += 1
    
    # Print the final count of strings that are equal to "Takahashi"
    print(taka_count)

# Ensure that the main function runs when the script is executed
if __name__ == "__main__":
    main()
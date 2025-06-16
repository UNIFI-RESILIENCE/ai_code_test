def count_passengers_over_60(details):
    # Initialize a counter to keep track of passengers over 60 years old
    count = 0
    
    # Iterate through each passenger's details in the list
    for detail in details:
        # Extract the age part of the detail string (characters at index 11 and 12)
        age_str = detail[11:13]
        
        # Convert the extracted age substring to an integer
        age = int(age_str)
        
        # Check if the passenger's age is strictly greater than 60
        if age > 60:
            # Increment the counter if the condition is met
            count += 1
            
    # Return the final count of passengers over 60 years old
    return count

# Example usage:
details_example_1 = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
print(count_passengers_over_60(details_example_1))  # Output: 2

details_example_2 = ["1313579440F2036", "2921522980M5644"]
print(count_passengers_over_60(details_example_2))  # Output: 0
def countSeniors(details):
    # Initialize a counter to keep track of passengers older than 60
    senior_count = 0

    # Loop through each passenger detail string
    for detail in details:
        # Extract the age substring from index 11 to 13
        age_str = detail[11:13]
        
        # Convert age string to integer
        age = int(age_str)

        # Increment the counter if age is strictly greater than 60
        if age > 60:
            senior_count += 1

    # Return the total number of senior passengers
    return senior_count

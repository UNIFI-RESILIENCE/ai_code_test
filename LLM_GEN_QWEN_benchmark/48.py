def is_palindrome(text: str) -> bool:
    # Normalize the text by converting it to lowercase to ensure case insensitivity
    normalized_text = text.lower()
    
    # Compare the normalized text with its reverse to check if it's a palindrome
    return normalized_text == normalized_text[::-1]
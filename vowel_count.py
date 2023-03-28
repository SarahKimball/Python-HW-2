

def vowel_count(phrase):

    # Initialize a dictionary to hold the vowel counts
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convert the phrase to lowercase to make it case-insensitive
    phrase = phrase.lower()
    
    # Loop through each character in the phrase
    for char in phrase:
        # If the character is a vowel, increment its count in the dictionary
        if char in vowel_counts:
            vowel_counts[char] += 1
    
    # Remove any vowels with a count of 0
    return {vowel: count for vowel, count in vowel_counts.items() if count > 0}

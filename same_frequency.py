def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # Convert numbers to strings
    str1 = str(num1)
    str2 = str(num2)
    
    # Count the frequency of each digit in both strings
    freq1 = {}
    freq2 = {}
    
    for digit in str1:
        freq1[digit] = freq1.get(digit, 0) + 1
        
    for digit in str2:
        freq2[digit] = freq2.get(digit, 0) + 1
        
    # Compare the frequency dictionaries
    return freq1 == freq2

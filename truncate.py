

def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    elif len(phrase) <= n:
        return phrase
    else:
        return phrase[:n-3] + '...'

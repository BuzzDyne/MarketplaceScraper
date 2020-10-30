def cleanUrl(url):
    """Cleans the input listing url.
    
    Removes everythin after '?' (inclusive)"""
    sep = '?'
    return url.split(sep,1)[0]
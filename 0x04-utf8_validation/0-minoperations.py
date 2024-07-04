#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
    :param data:
    :return:
    """
    for num in data:
        # Get the 8 least significant bits of the byte
        byte = num & 0xFF
        
        if n_bytes == 0:
            # Count the number of leading 1s
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1
            
            # 1-byte characters
            if n_bytes == 0:
                continue
            
            # If n_bytes is more than 4 or 1, it's not valid
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if the byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        n_bytes -= 1

    # If there are still bytes expected for the current character, return False
    return n_bytes == 0

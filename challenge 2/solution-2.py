def decode_linear_pigpen(encoded_text):
    # Define the formal sorting hierarchy
    sort_order = {'X': 0, 'T': 1, 'R': 2, 'B': 3, 'L': 4, 'D': 5}
    
    # Master Dictionary (Sorted Pigpen Walls -> Alphabet)
    pigpen_map = {
        'RB': 'A',   'RBL': 'B',  'BL': 'C',
        'TRB': 'D',  'TRBL': 'E', 'TBL': 'F',
        'TR': 'G',   'TRL': 'H',  'TL': 'I',
        'RBD': 'J',  'RBLD': 'K', 'BLD': 'L',
        'TRBD': 'M', 'TRBLD': 'N','TBLD': 'O',
        'TRD': 'P',  'TRLD': 'Q', 'TLD': 'R',
        'XT': 'S',   'XL': 'T',   'XR': 'U',   'XB': 'V',
        'XTD': 'W',  'XLD': 'X',  'XRD': 'Y',  'XBD': 'Z'
    }
    
    decoded_message = []
    
    # Format handling: Separate words by '/'
    words = encoded_text.split('/')
    
    for word in words:
        decoded_word = []
        # Separate letters by space
        letters = word.strip().split()
        
        for enc_letter in letters:
            # Handle punctuation
            if enc_letter == ',':
                decoded_word.append(',')
                continue
                
            # Remove visual dots and normalize to uppercase for dictionary lookup
            clean_letter = enc_letter.replace('·', '').upper()
            
            # Normalization for specific manual entry errors
            if clean_letter == 'BLRD':
                clean_letter = 'RBLD'
            elif clean_letter == 'TBRD':
                clean_letter = 'TRBD'
                
            # Apply the required reading order (Sorting the letters)
            sorted_chars = sorted(clean_letter, key=lambda c: sort_order.get(c, 99))
            sorted_letter = ''.join(sorted_chars)
            
            # Translate using the dictionary
            decoded_char = pigpen_map.get(sorted_letter, '?')
            decoded_word.append(decoded_char)
            
        # Join letters into a word
        decoded_message.append(''.join(decoded_word))
        
    # Join words into the final sentence and convert to lowercase
    final_output = ' '.join(decoded_message)
    return final_output.lower()

# Execution with the provided cipher input
cipher_input = (
    "X··L T·B··L·D / T·R··B·D T··L·B·D / "
    "X··T T·R··B·L L·B··D / "
    "X·B··D T·B··L·D B··D·L L··T / "
    "T··L·B B·L··D T·R··B·L T·L··D / "
    "B··T·R B··R T·R··B·L·D / "
    "B·D··R·T T·B··L·D / "
    "D··B·X R·B·· T·L··D T·R·B T··L T·R··B·L·D"
)

result = decode_linear_pigpen(cipher_input)

print("Encrypted Input Processed...")
print(f"Decoded Message: {result}")
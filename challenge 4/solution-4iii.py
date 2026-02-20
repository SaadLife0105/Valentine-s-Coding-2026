import zipfile
import itertools

# The file we want to unlock
zip_filename = "all challenges/Valentine Coding - Challenge 5.zip"

# The digits we know make up the password
digits = "0186"

# Generate all possible 4-digit arrangements (permutations) of these specific numbers.
# Example: 0186, 0168, 0816, 0861, etc.
combinations = itertools.permutations(digits, 4)

print(f"Attempting to unlock '{zip_filename}'...")

try:
    # Open the zip file
    with zipfile.ZipFile(zip_filename) as zf:
        # Loop through every possible combination
        for combo in combinations:
            # Join the tuple of numbers into a single string (e.g., "0186")
            password = "".join(combo)
            
            try:
                # Try to extract the file to the specific folder. 
                # The password needs to be converted to bytes using .encode()
                zf.extractall(path="challenge 4", pwd=password.encode('utf-8'))
                
                # If the line above succeeds without an error, we found the password!
                print(f"\nSUCCESS! The correct password is: {password}")
                print("The contents have been successfully extracted to your 'challenge 4' folder.")
                break  # Stop trying since we found the right one
                
            except (RuntimeError, zipfile.BadZipFile):
                # An error means the password was wrong. We ignore it and try the next one.
                pass

# Exception handling for file not found
except FileNotFoundError:
    print(f"Error: Could not find '{zip_filename}'. Make sure it's in the correct path.")
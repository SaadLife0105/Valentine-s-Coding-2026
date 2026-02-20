from collections import Counter

#data from the challenge
data = """
g p s g p y n P b g i p q n i h P i g k
n c p p g k p P e n i n e P h x p d P P
P w g i m p n e i g p P n e i r p i m n
g i p g P g g P g q i z i P e P e e z P
i i p P P g k P g e g p p x P g i e g i
g h z P n g i p c p n f i e e s p e e P
i P e P P n P i r f u P w e g P p i n x
i i g p g s t i i P i k p i e e m s P o
p u P g P i g P P y x p i a i p p j b t
p e i g u P e g P i n P e n i e b p n g
g n p b e i n e P n i P g e P u g i e p
t b j p p i a i p x y P P g i P g P u p
o P s m e e i p k i P i i t s g p g i i
x n i p P g e w P u f r i P n P P e P i
P e e p s e e i f n p c p i g n P z h g
i g e i g P x p p g e g P k g P P p i i
P z e e P e P i z i q g P g g P g p i g
n m i p r i e n P p g i e n p m i g w P
P P d p x h P e n i n e P p k g p p c n
k g i P h i n q p i g b P n y p g s p g
"""

# Convert the string into a list of characters
letters = data.split()

# Count the frequency of each character
counts = Counter(letters)

# We sort the items by their frequency (the value at index 1)
ascending_list = sorted(counts.items(), key=lambda item: item[1])

print("--- Frequencies (Rare to Common) ---")
for letter, freq in ascending_list:
    print(f"{letter}: {freq}")

# Extract the 6 most common items
top_6_pairs = counts.most_common(6)

# Use a join to concatenate just the letters into a single string
top_6_word = "".join([pair[0] for pair in top_6_pairs])

print("\n" + "-"*30)
print(f"Top 6 'Word': {top_6_word}")
print("-"*30)
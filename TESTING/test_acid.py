#github.com/yinkajets  ##myociormvbahproject-Summer2025

############################
### TESTING/test_acid.py ###
############################

import sys
import os
sys.path.append(os.path.abspath("."))

from acid import VcCom, VcOpen, VcVerify

# Step 1: Define a vector of messages
messages = ["message1", "message2", "message3", "message4"]

# Step 2: Generate a commitment (Merkle root)
commitment = VcCom(messages)
print("Commitment (Merkle root):", commitment)

# Step 3: Open the vector at index j (e.g., j = 2)
j = 2
yj, proof = VcOpen(j, messages)
print(f"\nValue at index {j}:", yj)
print(f"Merkle proof for index {j}:", proof)

# Step 4: Verify the proof
is_valid = VcVerify(j, commitment, yj, proof)
print("\nIs the proof valid?", is_valid)


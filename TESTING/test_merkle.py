#github.com/yinkajets  ##myociormvbahproject-Summer2025

#########################
### Testing Merkle.py ###
#########################

from utils.merkle import MerkleTree

# Example leaves
leaves = ['Alice', 'Bob', 'Charlie', 'David']

# Build the tree
tree = MerkleTree(leaves)

# Print the Merkle root
print("Merkle Root:", tree.get_root())

# Generate a proof for 'Charlie' (index 2)
proof = tree.get_proof(2)

# Verify the proof
is_valid = tree.verify_proof('Charlie', proof, tree.get_root())
print("Is proof valid?", is_valid)


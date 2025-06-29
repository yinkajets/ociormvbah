#github.com/yinkajets  ##myociormvbahproject-Summer2025

#######################################################
### Merkle tree code for implementation used by ACID ##
#######################################################

import hashlib
import math

class MerkleTree:
    def __init__(self, leaves):
        """
        Initialize a Merkle Tree from a list of leaves.
        Each leaf should be a string or byte-like object.
        """
        self.leaves = [self._hash(leaf) for leaf in leaves]
        self.levels = []
        self.build_tree()

    def _hash(self, data):
        """
        Returns a SHA-256 hash of the given data.
        """
        if not isinstance(data, bytes):
            data = str(data).encode('utf-8')
        return hashlib.sha256(data).hexdigest()

    def build_tree(self):
        """
        Constructs the Merkle Tree and stores it level-by-level.
        The bottom level is the hashed leaves.
        """
        current_level = self.leaves
        self.levels.append(current_level)

        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i+1] if i+1 < len(current_level) else left
                combined = self._hash(left + right)
                next_level.append(combined)
            current_level = next_level
            self.levels.append(current_level)

    def get_root(self):
        """
        Returns the Merkle root.
        """
        return self.levels[-1][0] if self.levels else None

    def get_proof(self, index):
        """
        Generates a Merkle proof for the leaf at the given index.
        Returns a list of tuples: (sibling_hash, is_left).
        """
        proof = []
        idx = index
        for level in self.levels[:-1]:
            if idx % 2 == 0:  # left node
                sibling_idx = idx + 1
                is_left = False
            else:  # right node
                sibling_idx = idx - 1
                is_left = True

            if sibling_idx < len(level):
                sibling_hash = level[sibling_idx]
            else:
                sibling_hash = level[idx]  # duplicate own hash if no sibling

            proof.append((sibling_hash, is_left))
            idx = idx // 2
        return proof

    def verify_proof(self, leaf, proof, root):
        """
        Verifies a Merkle proof for a given leaf and root.
        """
        computed_hash = self._hash(leaf)
        for sibling_hash, is_left in proof:
            if is_left:
                computed_hash = self._hash(sibling_hash + computed_hash)
            else:
                computed_hash = self._hash(computed_hash + sibling_hash)
        return computed_hash == root


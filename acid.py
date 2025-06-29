#############################################################
### acid.py : vector commitment using Merkle tree (ACIDh) ###
#############################################################

from utils.merkle import MerkleTree

class VectorCommitment:
    def __init__(self, vector):
        """
        Initialize with a vector of values (y1, y2, ..., yn).
        """
        self.vector = vector
        self.tree = MerkleTree(vector)
        self.commitment = self.tree.get_root()

    def VcCom(self):
        """
        Returns the commitment C (Merkle root) of the vector.
        """
        return self.commitment

    def VcOpen(self, j):
        """
        Returns an opening (proof) for the j-th element in the vector.
        Index j should be 0-based.
        """
        yj = self.vector[j]
        proof = self.tree.get_proof(j)
        return yj, proof

    @staticmethod
    def VcVerify(j, C, yj, proof):
        """
        Verifies that yj is the j-th committed element in a vector
        that corresponds to the Merkle root C.
        """
        temp_tree = MerkleTree([])  # to access hashing only
        return temp_tree.verify_proof(yj, proof, C)

# Optional adapter functions
def VcCom(y):
    return VectorCommitment(y).VcCom()

def VcOpen(j, y):
    return VectorCommitment(y).VcOpen(j)

def VcVerify(j, C, yj, proof):
    return VectorCommitment.VcVerify(j, C, yj, proof)


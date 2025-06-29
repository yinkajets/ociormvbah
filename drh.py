#github.com/yinkajets  ##myociormvbahproject-Summer2025

########################################
### drh.py : data retrieval protocol ###
########################################

from acid import VectorCommitment

class DRh:
    def __init__(self, committed_vector):
        """
        Initialize with the committed vector.
        """
        self.vc = VectorCommitment(committed_vector)

    def retrieve(self, index):
        """
        Retrieve the value yj and proof at index j from the committed vector.
        """
        yj, proof = self.vc.VcOpen(index)
        commitment = self.vc.VcCom()
        return yj, proof, commitment

    @staticmethod
    def verify(index, yj, proof, commitment):
        """
        Verifies that the provided value yj is valid at index j.
        """
        return VectorCommitment.VcVerify(index, commitment, yj, proof)

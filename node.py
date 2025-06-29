#github.com/yinkajets  ##myociormvbahproject-Summer2025

#####################################################################
### node.py : the core class that execute the OciorMVBAh protocol ###
#####################################################################

from acid import VectorCommitment
from drh import DRh
from abbba import ABBBA
from config import t, n

class Node:
    def __init__(self, node_id, input_value, round_number):
        self.node_id = node_id
        self.input_value = input_value
        self.round = round_number
        self.commitment = None
        self.openings = {}
        self.abbba = ABBBA(node_id, round_number)
        self.vector_commitment = None
        self.drh = None

    def vc_commit(self):
        """
        Perform vector commitment over the value.
        In this simple case, we assume the value is a vector of strings.
        """
        self.vector_commitment = VectorCommitment(self.input_value)
        self.commitment = self.vector_commitment.VcCom()
        return self.commitment

    def vc_open(self, index):
        """
        Provide proof for the value at a specific index.
        """
        return self.vector_commitment.VcOpen(index)

    def vc_verify(self, index, value, proof, root):
        """
        Verify a committed value with proof.
        """
        return VectorCommitment.VcVerify(index, root, value, proof)

    def run_abbba(self, peer_inputs):
        """
        Run ABBBA consensus with inputs received from peers.
        """
        for peer_id, val in peer_inputs.items():
            self.abbba.receive_input(peer_id, val)
        decided_value = self.abbba.run()
        return decided_value

    def drh_retrieve(self, index):
        """
        Initialize DRh and retrieve value + proof.
        """
        self.drh = DRh(self.input_value)
        return self.drh.retrieve(index)

    def simulate_protocol(self, peer_inputs):
        """
        Full end-to-end simulation of one OciorMVBAh round at this node.
        """
        print(f"\n--- Node {self.node_id} ---")
        print(f"Step 1: Vector Commitment for {self.input_value}")
        root = self.vc_commit()
        print(f"Commitment (Merkle root): {root}")

        print(f"Step 2: Run ABBBA with peer inputs")
        decision = self.run_abbba(peer_inputs)
        print(f"ABBBA decided on value: {decision}")

        print(f"Step 3: Open DRh at index {decision}")
        value, proof = self.drh_retrieve(decision)
        print(f"Retrieved value: {value}")
        print(f"Proof: {proof}")

        print(f"Step 4: Verify the proof")
        is_valid = self.vc_verify(decision, value, proof, root)
        print(f"Is proof valid? {is_valid}")

        return is_valid, value


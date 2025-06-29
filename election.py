#############################################################################################
### election.py : handles and generates random index for election ###
#############################################################################################

import random
import hashlib
from config import t, n

class Election:
    def __init__(self, ID, r):
        self.ID = ID
        self.r = r
        self.inputs = {}  # node_id -> seed/input
        self.elected = None

    def receive_input(self, node_id, seed):
        """
        Accepts input (e.g., random seed) from a node.
        """
        if node_id not in self.inputs:
            self.inputs[node_id] = seed

    def is_ready(self):
        """
        Checks if enough inputs (t + 1) have been received.
        """
        return len(self.inputs) >= (t + 1)

    def compute_election(self):
        """
        Computes the election result (random l ∈ [1, n]) using the combined hash of inputs.
        """
        if not self.is_ready():
            raise Exception("Not enough inputs to compute election.")

        # Combine and hash all inputs
        combined = ''.join(str(seed) for seed in sorted(self.inputs.values()))
        digest = hashlib.sha256(combined.encode()).hexdigest()

        # Convert hash digest to integer and mod by n to get l ∈ [1, n]
        l = (int(digest, 16) % n) + 1
        self.elected = l
        return l


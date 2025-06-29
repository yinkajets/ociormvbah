#github.com/yinkajets  ##myociormvbahproject-Summer2025

#####################################################################
### node.py : the core class that execute the OciorMVBAh protocol ###
#####################################################################


from acid import VcCom, VcOpen, VcVerify
from drh import DRh
from abba import ABBA
from abbba import ABBBA
from election import Election
from config import n, t

class Node:
    def __init__(self, ID):
        self.ID = ID
        self.input_vector = []
        self.round = 0
        self.commitment = None
        self.other_commitments = {}
        self.received_verified_values = {}
        self.election = None
        self.abba_instances = {}     # round -> ABBA instance
        self.abbba_instances = {}    # round -> ABBBA instance
        self.election_instances = {} # round -> Election instance

    def set_input_vector(self, vector):
        """
        Sets the node's input vector.
        """
        self.input_vector = vector
        self.drh = DRh(vector)

    def commit_vector(self):
        """
        Commits to the vector using vector commitment (Merkle root).
        """
        if not self.input_vector:
            raise ValueError("Input vector is empty or not set.")
        self.commitment = VcCom(self.input_vector)
        return self.commitment

    def receive_commitment(self, from_id, commitment):
        """
        Receive and store commitment from another node.
        """
        self.other_commitments[from_id] = commitment

    def retrieve_value(self, index):
        """
        Retrieve a value and proof at index using DRh.
        """
        drh = DRh(self.input_vector)
        return drh.retrieve(index)

    def verify_value(self, index, value, proof, commitment):
        """
        Verifies retrieved value against commitment.
        """
        return DRh.verify(index, value, proof, commitment)

    def run_abba(self, r, values):
        """
        Run ABBA instance for round r.
        """
        if r not in self.abba_instances:
            self.abba_instances[r] = ABBA(self.ID, r)
        abba = self.abba_instances[r]
        for sender_id in range(len(values)):
            abba.receive_input(sender_id, values[sender_id])
        if abba.is_ready():
            return abba.run()
        return None

    def abba_output(self):
        """
        Return the output of the ABBA protocol if available.
        """
        # We assume only one round is used for now (e.g., round 0)
        if 0 in self.abba_instances:
            return self.abba_instances[0].output
        return None



    def run_abbba(self, r, values):
        """
        Run ABBBA instance for round r.
        """
        if r not in self.abbba_instances:
            self.abbba_instances[r] = ABBBA(self.ID, r)
        abbba = self.abbba_instances[r]
        for sender_id in range(len(values)):
            abbba.receive_input(sender_id, values[sender_id])
        if abbba.is_ready():
            return abbba.run()
        return None

    def abbba_output(self, r=0):
        """
        Get the ABBBA output for round r.
        """
        if r in self.abbba_instances:
            return self.abbba_instances[r].output_value
        return None


    def elect_committee(self, r, seeds):
        """
        Receive seeds and initialize election.
        """
        self.election = Election(self.ID, r)
        for sender_id, seed in seeds.items():
            self.election.receive_input(sender_id, seed)

    def compute_election(self):
        """
        Compute election index.
        """
        if self.election is None:
            raise Exception("Election instance not initialized.")
        return self.election.compute_election()

    def receive_retrieved_value(self, from_id, value, proof, commitment, index):
        """
        Receive and verify retrieved value from another node.
        """
        valid = self.drh.verify(index, value, proof, commitment)
        if valid:
           self.received_verified_values[from_id] = value


#github.com/yinkajets  ##myociormvbahproject-Summer2025

########################################
### abba.py : asynchronous binary BA ###
########################################

import random
from config import t, n

class ABBA:
    def __init__(self, ID, r):
        self.ID = ID
        self.r = r
        self.received_inputs = {}  # node_id -> 0 or 1
        self.common_coin = None
        self.output = None

    def receive_input(self, node_id, value):
        """
        Collect input from other nodes.
        """
        if node_id not in self.received_inputs:
            self.received_inputs[node_id] = value

    def is_ready(self):
        """
        Check if ABBA is ready to run: needs t+1 inputs.
        """
        return len(self.received_inputs) >= (t + 1)

    def get_majority(self):
        """
        Determine the majority input among received.
        """
        values = list(self.received_inputs.values())
        return 1 if values.count(1) >= values.count(0) else 0

    def generate_common_coin(self):
        """
        Simulate shared randomness via a common coin.
        """
        self.common_coin = random.randint(0, 1)
        return self.common_coin

    def run(self):
        """
        Execute the ABBA decision logic.
        """
        if not self.is_ready():
            raise Exception("Insufficient inputs to run ABBA")

        majority = self.get_majority()
        support = list(self.received_inputs.values()).count(majority)
        coin = self.generate_common_coin()

        if support >= (n - t):
            self.output = majority
        else:
            self.output = coin

        return self.output


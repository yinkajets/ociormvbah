#github.com/yinkajets  ##myociormvbahproject-Summer2025

################################################
### abbba.py : asynchronous biased binary BA ###
################################################

import random
from config import t, n

class ABBBA:
    def __init__(self, ID, r):
        self.ID = ID
        self.r = r
        self.input_value = None
        self.output_value = None
        self.received_values = {}  # node_id -> value
        self.common_coin_value = None

    def receive_input(self, node_id, value):
        """
        Receive input from node. Values are 0 or 1.
        """
        if node_id not in self.received_values:
            self.received_values[node_id] = value

    def is_ready(self):
        """
        Check if at least t+1 values received.
        """
        return len(self.received_values) >= (t + 1)

    def get_majority_value(self):
        """
        Return majority value from received inputs.
        """
        count_0 = list(self.received_values.values()).count(0)
        count_1 = list(self.received_values.values()).count(1)
        return 0 if count_0 > count_1 else 1

    def generate_common_coin(self):
        """
        Simulates the common coin generation (shared randomness).
        """
        self.common_coin_value = random.randint(0, 1)
        return self.common_coin_value

    def run(self):
        """
        Runs ABBBA consensus process and returns decided value.
        """
        if not self.is_ready():
            raise Exception("Not enough inputs to run ABBBA")

        maj = self.get_majority_value()
        coin = self.generate_common_coin()

        # Decision rule: output majority if there is strong support, else coin
        support = list(self.received_values.values()).count(maj)
        if support >= (n - t):
            self.output_value = maj
        else:
            self.output_value = coin

        return self.output_value


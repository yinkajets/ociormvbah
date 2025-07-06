#github.com/yinkajets  ##myociormvbahproject-Summer2025

####################
### test abba.py ###
####################

import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from abba import ABBA
from config import n, t

def test_abba_protocol():
    print("=== Testing ABBA Protocol ===")

    # Create ABBA instances for each node
    abba_instances = [ABBA(ID=i, r=0) for i in range(n)]

    # Simulate each node receiving inputs from others (e.g., broadcast)
    inputs = [random.randint(0, 1) for _ in range(n)]

    for i, instance in enumerate(abba_instances):
        for j in range(n):
            instance.receive_input(j, inputs[j])

    # Run ABBA protocol for each node
    for i, instance in enumerate(abba_instances):
        try:
            decision = instance.run()
            print(f"Node {i} decided on value: {decision}")
        except Exception as e:
            print(f"Node {i} failed: {str(e)}")

if __name__ == "__main__":
    test_abba_protocol()


#github.com/yinkajets  ##myociormvbahproject-Summer2025

########################
### testing abbba.py ###
########################

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from abbba import ABBBA
from config import n, t

def test_abbba_protocol():
    print("=== Testing ABBBA Protocol ===")

    round_number = 1
    nodes = []

    # Create ABBBA instances for each node
    for i in range(n):
        node = ABBBA(ID=i, r=round_number)
        nodes.append(node)

    # Simulate each node broadcasting its input
    inputs = [0, 1, 0, 0]  # Example inputs (n=4)

    for i, node in enumerate(nodes):
        for j in range(n):
            node.receive_input(j, inputs[j])

    # Run ABBBA on each node and print output
    for i, node in enumerate(nodes):
        if node.is_ready():
            decision = node.run()
            print(f"Node {i} decided on value: {decision}")
        else:
            print(f"Node {i} not ready")

if __name__ == "__main__":
    test_abbba_protocol()



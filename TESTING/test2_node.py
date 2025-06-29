#github.com/yinkajets  ##myociormvbahproject-Summer2025

###################################################################################
### test node2.py : For improvement on test_node.py by allowing multiple rounds ###
###################################################################################

from config import n
from node import Node
import random

def simulate_ocior_mvbah_multi_rounds(rounds=3):
    print("=== Simulating OciorMVBAh Protocol Over Multiple Rounds ===")

    for r in range(rounds):
        print(f"\n--- Round {r} ---")

        # Initialize nodes
        nodes = [Node(ID=i) for i in range(n)]

        # Set input vector for each node
        for node in nodes:
            input_vector = [f"msg{i}_round{r}_node{node.ID}" for i in range(n)]
            node.set_input_vector(input_vector)

        # Commitment phase
        commitments = [node.commit_vector() for node in nodes]
        for node in nodes:
            for i, C in enumerate(commitments):
                node.receive_commitment(i, C)

        # Data retrieval phase
        index = r % n  # cycle index for variety
        retrieved_data = [node.retrieve_value(index) for node in nodes]
        for node in nodes:
            for i, (val, proof, C) in enumerate(retrieved_data):
                node.receive_retrieved_value(i, val, proof, C, index)

        # Election phase
        seeds = {node.ID: f"seed{node.ID}_r{r}" for node in nodes}
        for node in nodes:
            node.elect_committee(r=r, seeds=seeds)

        election_results = [node.compute_election() for node in nodes]
        print("Election Results:", election_results)

        # ABBBA phase
        shared_values = [random.randint(0, 1) for _ in range(n)]
        for node in nodes:
            input_val = shared_values[node.ID]
            node.run_abbba(r, shared_values)
        abbba_outputs = [node.abbba_output(r) for node in nodes]
        print("ABBBA Outputs:", abbba_outputs)

        # ABBA phase
        for node in nodes:
            input_val = shared_values[node.ID]
            node.run_abba(r, shared_values)
        abba_outputs = [node.abba_output(r) for node in nodes]
        print("ABBA Outputs:", abba_outputs)

if __name__ == "__main__":
    simulate_ocior_mvbah_multi_rounds()


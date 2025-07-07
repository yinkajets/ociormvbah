import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from node import Node
from config import n

def resolve_ocior_mvbah_interactively():
    print("=== Interactive OciorMVBAh Protocol Simulation ===")

    # Create node instances
    nodes = [Node(ID=i) for i in range(n)]

    # Prompt user to enter input vector for each node
    for node in nodes:
        print(f"\nEnter input vector for Node {node.ID} (comma-separated values):")
        raw_input = input(">>> ")
        input_vector = [val.strip() for val in raw_input.split(",")]
        node.set_input_vector(input_vector)

    # Each node commits and shares its commitment
    commitments = [node.commit_vector() for node in nodes]
    for node in nodes:
        for i, C in enumerate(commitments):
            node.receive_commitment(i, C)

    # Retrieve and share values
    index = 0  # or choose another strategy for index
    retrieved_data = [node.retrieve_value(index) for node in nodes]
    for node in nodes:
        for i, (val, proof, C) in enumerate(retrieved_data):
            node.receive_retrieved_value(i, val, proof, C, index)

    # Election phase
    seeds = {node.ID: f"seed{node.ID}" for node in nodes}
    for node in nodes:
        node.elect_committee(r=0, seeds=seeds)

    election_results = [node.compute_election() for node in nodes]
    print("\nElection Results:", election_results)

    # Run ABBBA
    shared_values = [node.ID % 2 for node in nodes]
    for node in nodes:
        input_val = node.ID % 2
        node.run_abbba(r=0, values=shared_values)

    abbba_outputs = [node.abbba_output(0) for node in nodes]
    print("ABBBA Outputs:", abbba_outputs)

    # Run ABBA
    for node in nodes:
        input_val = node.ID % 2
        node.run_abba(r=0, values=shared_values)

    abba_outputs = [node.abba_output(0) for node in nodes]
    print("ABBA Outputs:", abba_outputs)

    # Final agreement resolution
    final_output = max(set(abba_outputs), key=abba_outputs.count)
    print(f"\n✅ Final Agreed Output of OciorMVBAh: {final_output}")

if __name__ == "__main__":
    resolve_ocior_mvbah_interactively()


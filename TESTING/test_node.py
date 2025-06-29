#github.com/yinkajets  ##myociormvbahproject-Summer2025

####################
### test node.py ###
####################

from node import Node
from config import n

def simulate_ocior_mvbah():
    print("=== Testing OciorMVBAh Protocol Simulation ===")

    # Create node instances
    nodes = [Node(ID=i) for i in range(n)]

    # Set input vector for each node
    for node in nodes:
        input_vector = [f"message{i}_{node.ID}" for i in range(n)]
        node.set_input_vector(input_vector)

    # Each node commits and shares its commitment
    commitments = [node.commit_vector() for node in nodes]

    # All nodes receive the commitments
    for node in nodes:
        for i, C in enumerate(commitments):
            node.receive_commitment(i, C)

    # Simulate data retrieval (e.g., index 2)
    index = 2
    retrieved_data = [node.retrieve_value(index) for node in nodes]

    # Share retrieved values
    for node in nodes:
        for i, (val, proof, C) in enumerate(retrieved_data):
            node.receive_retrieved_value(i, val, proof, C, index)

    # Election phase: all nodes provide their seed to each other
    seeds = {node.ID: f"seed{node.ID}" for node in nodes}
    for node in nodes:
        node.elect_committee(r=0, seeds=seeds)


    election_results = [node.compute_election() for node in nodes]
    print("Election Results (l values):", election_results)

    # Run ABBBA
    shared_values = [node.ID % 2 for node in nodes]  # Sample shared values for ABBBA
    for node in nodes:
        input_val = node.ID % 2
        node.run_abbba(input_val, shared_values)

    abbba_outputs = [node.abbba_output() for node in nodes]
    print("ABBBA Outputs:", abbba_outputs)

    # Run ABBA
    for node in nodes:
        input_val = node.ID % 2
        node.run_abba(input_val, shared_values)

    abba_outputs = [node.abba_output() for node in nodes]
    print("ABBA Outputs:", abba_outputs)

if __name__ == "__main__":
    simulate_ocior_mvbah()

#github.com/yinkajets  ##myociormvbahproject-Summer2025

####################
### test node.py ###
####################

from node import Node
from config import n

def simulate_mvbah_protocol():
    print("=== Testing OciorMVBAh Protocol Simulation ===\n")

    input_values = [f"message{i}" for i in range(n)]
    results = []

    for i in range(n):
        node = Node(node_id=i, input_value=input_values[i])
        result = node.run_protocol(input_values)
        results.append(result)

    for res in results:
        print(f"Node {res['node']}:")
        print(f"  Commitment: {res['commitment']}")
        print(f"  Committee: {res['committee']}")
        print(f"  Value Retrieved: {res['value']}")
        print(f"  Merkle Proof: {res['proof']}")
        print(f"  Validation (ABBBA): {res['validated']}")
        print(f"  Decision Output (ABBA): {res['output']}\n")

if __name__ == "__main__":
    simulate_mvbah_protocol()


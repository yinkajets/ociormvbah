#github.com/yinkajets  ##myociormvbahproject-Summer2025

###########################
### TESTING election.py ###
###########################

from election import Election
from config import t, n

# Create an election instance
election = Election(ID="test", r=1)

# Simulate node inputs
for node_id in range(t + 1):
    election.receive_input(node_id, f"seed_from_node_{node_id}")

# Trigger election
if election.is_ready():
    l = election.compute_election()
    print(f"Elected l value: {l}")
else:
    print("Not enough inputs to elect.")


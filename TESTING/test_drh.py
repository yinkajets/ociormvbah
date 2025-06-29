#github.com/yinkajets  ##myociormvbahproject-Summer2025

###################
### test drh.py ###
###################

from drh import DRh

def test_drh():
    print("=== Testing DRh Data Retrieval ===")
    data_vector = ['a', 'b', 'c', 'd']
    drh = DRh(data_vector)

    index = 2
    yj, proof, commitment = drh.retrieve(index)
    print(f"Retrieved value: {yj}")
    print(f"Proof: {proof}")
    print(f"Commitment: {commitment}")
    
    is_valid = DRh.verify(index, yj, proof, commitment)
    print("Is proof valid?", is_valid)

if __name__ == "__main__":
    test_drh()


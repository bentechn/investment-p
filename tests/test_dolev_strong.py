# tests/test_dolev_strong.py

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from market_sim.consensus.dolev_strong import run_dolev_strong_protocol

def print_result(title, result):
    print(f"\n=== {title} ===")
    for node_id in sorted(result):
        print(f"Node {node_id}: {result[node_id]}")

def test_all_honest():
    result = run_dolev_strong_protocol(
        num_nodes=5,
        max_faults=1,
        sender_bit=1,
        corrupt_ids=[]
    )
    print_result("All Honest Nodes (Consensus Expected)", result)

def test_one_corrupt():
    result = run_dolev_strong_protocol(
        num_nodes=5,
        max_faults=1,
        sender_bit=1,
        corrupt_ids=[3]
    )
    print_result("One Corrupt Node (Consensus Still Expected)", result)

def test_corrupt_sender():
    result = run_dolev_strong_protocol(
        num_nodes=5,
        max_faults=1,
        sender_bit=1,
        corrupt_ids=[1]  # sender is corrupt
    )
    print_result("Corrupt Sender (May Fail Validity)", result)

def test_inconsistent_corruption():
    result = run_dolev_strong_protocol(
        num_nodes=7,
        max_faults=2,
        sender_bit=0,
        corrupt_ids=[2, 5]
    )
    print_result("Two Corrupt Nodes (f = 2, Should Still Work)", result)

if __name__ == "__main__":
    test_all_honest()
    test_one_corrupt()
    test_corrupt_sender()
    test_inconsistent_corruption()

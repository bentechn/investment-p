# market_sim/consensus/dolev_strong.py

from market_sim.agents.node import Node

def run_dolev_strong_protocol(num_nodes, max_faults, sender_bit, corrupt_ids=[]):
    """
    Run the Dolev-Strong Protocol.
    - num_nodes: total number of nodes
    - max_faults: max number of faulty nodes (f)
    - sender_bit: the bit proposed by the sender (node 1)
    - corrupt_ids: list of node IDs that are corrupt
    """

    # Initialize nodes
    nodes = {}
    for i in range(1, num_nodes + 1):
        nodes[i] = Node(i, is_honest=(i not in corrupt_ids))

    # Round 0: Sender (node 1) sends signed message to all
    round_messages = []
    initial_msg = nodes[1].create_signed_message(sender_bit, [1])
    for i in range(2, num_nodes + 1):
        round_messages.append((i, initial_msg))  # (recipient_id, message)

    # Rounds 1 to f + 1
    for r in range(1, max_faults + 2):
        next_round_messages = []

        # Group messages for each node
        inbox = {i: [] for i in nodes}
        for recipient_id, message in round_messages:
            inbox[recipient_id].append(message)

        # Let each node process its messages
        for i in range(1, num_nodes + 1):
            new_msgs = nodes[i].receive_messages(inbox[i], r, max_faults)
            for msg in new_msgs:
                for j in range(1, num_nodes + 1):
                    if j != i:
                        next_round_messages.append((j, msg))

        round_messages = next_round_messages

    # Final output
    results = {}
    for i in range(1, num_nodes + 1):
        extracted = nodes[i].extracted_set
        if len(extracted) == 1:
            results[i] = list(extracted)[0]
        else:
            results[i] = 0
    return results

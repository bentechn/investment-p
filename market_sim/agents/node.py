# market_sim/agents/node.py

import hashlib
import random

class Node:
    def __init__(self, node_id, is_honest=True):
        self.node_id = node_id
        self.is_honest = is_honest
        self.extracted_set = set()
        self.private_key = f"secret_{node_id}"  # Simplified "key"
        self.public_key = f"node_{node_id}"

    def sign(self, message):
        # Simplified signature: hash(message + secret)
        return hashlib.sha256((message + self.private_key).encode()).hexdigest()

    def verify(self, message, signature, signer_id):
        expected = hashlib.sha256((message + f"secret_{signer_id}").encode()).hexdigest()
        return signature == expected

    def create_signed_message(self, bit, signers):
        """
        Creates a message like: ("0", [("sig1", id1), ("sig2", id2), ...])
        """
        message = str(bit)
        sigs = []
        for node_id in signers:
            sig = hashlib.sha256((message + f"secret_{node_id}").encode()).hexdigest()
            sigs.append((sig, node_id))
        return (bit, sigs)

    def receive_messages(self, messages, current_round, max_faults):
        """
        Process incoming messages and return new ones to forward.
        """
        new_messages = []
        for bit, sigs in messages:
            if bit not in self.extracted_set and len(sigs) == current_round:
                valid = True
                signer_ids = set()
                for sig, signer_id in sigs:
                    if not self.verify(str(bit), sig, signer_id):
                        valid = False
                    signer_ids.add(signer_id)
                if valid and 1 in signer_ids:  # Must include sender
                    self.extracted_set.add(bit)
                    # Forward message with new signature if still in protocol rounds
                    if current_round < max_faults + 1:
                        new_sigs = sigs + [(self.sign(str(bit)), self.node_id)]
                        new_messages.append((bit, new_sigs))
        return new_messages

# Dolev-Strong Protocol – Investment-P Simulation Extension

This project is a technical submission for Torbellino Tech's introductory test. It extends the `investment-p` repository with a simulation of the **Dolev-Strong Byzantine consensus protocol** implemented in Python.

## 📘 Summary

The Dolev-Strong protocol is a deterministic, round-based Byzantine broadcast protocol designed for synchronous networks. It tolerates up to `f` corrupt nodes and guarantees consensus among honest participants using digital signatures.

This implementation integrates with the `market_sim` framework and simulates the behavior of honest and corrupt nodes over multiple rounds of signed message propagation.

## 📁 Project Structure

investment-p/
├── market_sim/
│ ├── agents/
│ │ └── node.py # Defines honest and corrupt node behavior
│ ├── consensus/
│ │ └── dolev_strong.py # Protocol logic with message rounds
│ └── network_sim.py # (Placeholder for future integration)
├── tests/
│ └── test_dolev_strong.py # Runs protocol in various scenarios


## 🚀 How It Works

- Node 1 (sender) sends a signed bit to all others
- In each of `f + 1` rounds, nodes forward signed messages with exactly `r` signatures
- Nodes accept a value into their `extracted_set` only if the message is valid and timely
- At the end, each node outputs:
  - The bit if it has exactly one value in its set
  - `0` if the set is empty or has multiple values

## 🧪 Testing

Run all test scenarios:

```bash
python tests/test_dolev_strong.py


=== All Honest Nodes (Consensus Expected) ===
Node 1: 1
Node 2: 1
Node 3: 1
...

=== One Corrupt Node (Consensus Still Expected) ===
Node 4: 1
...

=== Corrupt Sender (May Fail Validity) ===
Node 1: 1
Node 2: 0
...

## Features
Message signing and signature verification (simplified)

Honest and corrupt node behavior

Configurable number of nodes and max faults

Round-by-round simulation

Clear output of consensus results per scenario

##  Requirements
Python 3.8+

No external libraries required (only built-in hashlib and random)
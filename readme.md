# Batfish

- Open Source MultiVendor Analysis Tool
- Helps to detect errors, validate changes before implementation
- Offline tool
- Containerized
- Learns via snapshots
- Constructs vendor agnostic models
- Queried via questions(pybatfish, Ansible role)

### What can Batfish do?

- Network Modelling
- Control Plane Simulation
- Validate configuration
- Query control plane state
- Verify ACL behavior
- Analyze routing/flow paths
- Simulate network failure(Impact Analysis)

### Batfish Installation

```BASH
sudo apt install python3-dev python3-venv
sudo apt-get install --reinstall build-essential
docker pull batfish/allinone
docker run --name batfish -d -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
python3 -m venv venv-batfish
pip install pybatfish
```
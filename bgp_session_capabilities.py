from pybatfish.client.commands import bf_session, bf_set_network
from pybatfish.question import bfq
from pybatfish.question.question import load_questions
from rich import print

BF_SERVICE_IP = "192.168.0.161"
BF_SNAPSHOT_PATH = "batfish/snapshots/automation-pod01"
BF_SNAPSHOT_NAME = "automation-pod01"
BF_NETWORK_NAME = "automation-pod01-network"

bf_session_host = BF_SERVICE_IP

load_questions()

bf_set_network(BF_NETWORK_NAME)

bf_session.init_snapshot(BF_SNAPSHOT_PATH, name=BF_NETWORK_NAME, overwrite=True)
df_bgp_compat = bfq.bgpSessionCompatibility().answer().frame()
print(df_bgp_compat)
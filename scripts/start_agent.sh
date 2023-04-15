set -e 

# fetch the agent from the local package registry
aea fetch eightballer/liquidation_station --local

# go to the new agent
cd liquidation_station/

# create and add a new ethereum key
aea generate-key ethereum && aea add-key ethereum

# issue certificates for agent 2 agent communications
aea issue-certificates

# finally, run the agent
aea run

set -e 

# fetch the agent from the local package registry
#aea fetch eightballer/liquidation_station --local
aea fetch $1 --local --alias agent

# go to the new agent
#cd liquidation_station/
cd agent

# install the agent
aea install

# create and add a new ethereum key
aea generate-key ethereum && aea add-key ethereum

# install any agent deps
aea install



# issue certificates for agent 2 agent communications
aea issue-certificates

# finally, run the agent
aea run

# Liquidation Station

The application is build on top of the open-autonomy framework.

This allows us to define a multi-agent system secured on chain, using the autonolas stack.



## Running a single agent locally

### Dependencies
- Tendermint

```bash
wget https://github.com/tendermint/tendermint/releases/download/v0.34.11/tendermint_0.34.11_linux_amd64.tar.gz

tar -xf tendermint.tar.gz
sudo mv tendermint /usr/local/bin/tendermint
```


First you must create a local tendermint node to run the agent. If you have old data stored, remove that first.
```bash
sudo rm -r ~/.tendermint/data/ &&
```

Then start a local Tendermint node for the agent to connect to 
```bash
sudo tendermint init validator && sudo cp -r /root/.tendermint ~/
```

Finally, the agent can be fetched and ran using the script provided

```bash
bash scripts/start_agent.sh
```

In case you already have an existing folder from a previous deployment you have simply remove it.



# Liquidation Station

The application is build on top of the open-autonomy framework.

This allows us to define a multi-agent system secured on chain, using the autonolas stack.


## Live Deployments

The application is currently deployed on Digital Ocean pending deployment to;

app.propel.valory.xyz

Live endpoints are available for the frontend;

(frontend)[165.22.80.193:3000]

And for the 4 agents;

```bash
curl @165.22.80.193:8000
{"state": {"name": "liquidation_station", "address": "0x6Af19cF073B399740Bc664bb7E908099f222E306", "round": "prepare_liquidation_transactions_behaviour"}}
```


## Running a single agent locally


### Dependencies
- Tendermint
```bash
wget https://github.com/tendermint/tendermint/releases/download/v0.34.11/tendermint_0.34.11_linux_amd64.tar.gz
```



First you must create a local tendermint node to run the agent, (Do this in a seperate tab)
```bash
sudo rm -r ~/.tendermint/data/ && sudo tendermint init validator && sudo cp -r /root/.tendermint ~/  && sudo chown -R (whoami):(whoami) ~/.tendermint
```
Then, you can fetch the agent;

```bash
poetry install && poetry shell
autonomy packages sync
```

```bash
make run-single-agent
```




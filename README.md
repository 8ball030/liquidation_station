# Liquidation Station

Much of the contemporary defi protocols depend on bot operators to perform
various tasks in order to ensure that actions get taken when required.
The operators are incentivized by the reward they receive, however, the
environment is extremely competitive which inevitably leads to scenarios where
only those most skilled and well equiped can participate. Not only does this
lead to centralization which diminishes fault tolerance, the software that these
operators run is often a black box to those whose protocols rely on it.

We take the opposite approach in our multi-agent application, where we incentivize
collaboration by securing off chain computation using Tendermint. Doing so all
state transitions during off chain computation require consensus. After a
complete iteration the final transactions to liquidate are submitted on-chain
(polygon mainnet). The agents share a multisig wallet and the rewards are
distributed evenly, where operators that perform better get rewarded more, and
those that do not contribute can be removed from the set of active participants
if so decided by majority consensus, in order to allow the system to be purged
from parasites that will inevitably arise.

These liquidation fees and subsequently used in the Rysk Roller skill, which the
agents use the trade using the Wheel Options Strategy. By utilizing the Wheel
Strategy, Rysk Roller aims to capitalize on market opportunities while
maintaining a balanced and fully collateralized position. We developed a [smart
contract](https://github.com/N0xMare/rysk-hmm) that provides access to the necessary methods on various smart contracts
of [Rysk](https://www.rysk.finance/), [Opyn](https://www.opyn.co/?ct=NL) and [Gamma Protocol](https://www.gamma.xyz/)
This allows for additional income generation through options premiums.

The application is build on top of the open-autonomy framework.
This allows us to define a multi-agent system secured on chain, using the Autonolas stack.

## Live Deployments

The application is currently deployed on Digital Ocean pending deployment to;

app.propel.valory.xyz

Live endpoints are available for the frontend;

[frontend](http://165.22.80.193:3000)

And for the 4 agents;

```bash
curl @165.22.80.193:8000
{"state": {"name": "liquidation_station", "address": "0x6Af19cF073B399740Bc664bb7E908099f222E306", "round": "prepare_liquidation_transactions_behaviour"}}
```


## Running as a multi agent service

First setup the env;

```
export INFURA_API_KEY=secret
export POLYGONSCAN_API_KEY=secrets
# make some keys
autonomy generate-key ethereum -n 4
# set your author
aea init --remote --reset --author eightballer --ipfs
autonomy packages sync
```
bash scripts/start_multi_agent.sh

```



## Running a single agent locally


### Dependencies
- Tendermint

```bash
wget https://github.com/tendermint/tendermint/releases/download/v0.34.11/tendermint_0.34.11_linux_amd64.tar.gz

tar -xf tendermint.tar.gz
sudo mv tendermint /usr/local/bin/tendermint
```

First you must create a local tendermint node to run the agent, (Do this in a seperate tab). If you have old data stored, remove that first.

```bash
sudo rm -r ~/.tendermint/data/ &&
```

Then start a local Tendermint node for the agent to connect to 
```bash
sudo tendermint init validator && sudo cp -r /root/.tendermint ~/  && sudo chown -R (whoami):(whoami) ~/.tendermint
tendermint start
```

Finally, the agent can be fetched and ran using the script provided

```bash
poetry install && poetry shell
autonomy packages sync
```

```bash
make run-single-agent
```

In case you already have an existing folder from a previous deployment you may have to remove it first.



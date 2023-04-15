# Liquidation Station

The application is build on top of the open-autonomy framework.

This allows us to define a multi-agent system secured on chain, using the autonolas stack.



## Running a single agent locally

### Dependencies
- Tendermint
```bash
wget https://github.com/tendermint/tendermint/releases/download/v0.34.11/tendermint_0.34.11_linux_amd64.tar.gz
```



First you must create a local tendermint node to run the agent
```bash
sudo rm -r ~/.tendermint/data/ && sudo tendermint init validator && sudo cp -r /root/.tendermint ~/  && sudo chown -R (whoami):(whoami) ~/.tendermint
```
Then, you can fetch the agent;

```bash
Todo
```

And finally, you can run it;



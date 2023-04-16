#! /bin/bash
set -e
autonomy fetch eightballer/liquidation_station --local --service

cd liquidation_station

# build the images
autonomy build-image
# build the deployment
autonomy deploy build ../keys.json
# run the deployment
cd abci_build
docker-compose up


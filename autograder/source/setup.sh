#!/bin/bash
apt-get update && apt-get install -y openjdk-17-jre unzip python3 python3-pip
pip3 install amulet-core
echo "Setup complete!"

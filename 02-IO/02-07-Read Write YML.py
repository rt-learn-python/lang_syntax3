#!/usr/bin/env python3

import yaml

with open('~/tickets.yml') as file:
    tickets = yaml.load(file)

print(tickets)

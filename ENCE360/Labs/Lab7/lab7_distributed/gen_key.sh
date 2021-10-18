#!/bin/bash

cp ~/.ssh ~/.ssh.bak -r
rm -r ~/.ssh


ssh-keygen -f ~/.ssh/id_rsa -t rsa -N '' -C ''

printf "Host cs*\n\tStrictHostKeyChecking=no" >> ~/.ssh/config
ssh-copy-id localhost 

ssh-add

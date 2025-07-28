#!/bin/bash
#
# Adds ssh deploy key to agent and scans gitlab server pubkey
#

set -e

eval $(ssh-agent -s)
echo "$MASTER_DEPLOY_KEY" > /tmp/ssh_deploy.key
chmod 600 /tmp/ssh_deploy.key
ssh-add /tmp/ssh_deploy.key
mkdir -p -m 0600 /root/.ssh
ssh-keyscan github.com >> /root/.ssh/known_hosts
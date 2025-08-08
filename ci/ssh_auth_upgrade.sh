#!/bin/sh
#
# Adds ssh deploy key to agent and scans github server pubkey
#

set -e

eval $(ssh-agent -s)
echo "$MASTER_DEPLOY_KEY" > /tmp/ssh_deploy.key
chmod 600 /tmp/ssh_deploy.key
ssh-add /tmp/ssh_deploy.key
ssh-keyscan github.com >> /tmp/known_hosts
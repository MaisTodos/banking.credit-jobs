#!/bin/bash

set -e

aws secretsmanager get-secret-value --secret-id ${AWS_SECRET_ID} --query SecretString --output text | jq 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' > /tmp/secrets.env
eval $(cat /tmp/secrets.env | sed 's/^/export /')
rm -f /tmp/secrets.env

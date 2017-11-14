#!/bin/bash
set -ev

## Decrypt the SSH deploy key and push the site live, if this is the live
## environment (on Travis) and not a PR

# 1. Check this isn't a Travis PR
if [ "$TRAVIS_PULL_REQUEST" != "false" ]
then
  echo "This is not a Travis build, or is a Travis PR - skipping deploy."
  exit 0
fi

# 2. Check for decryption key in environment
if [ -z "$encrypted_713170cfc4d9_key" -o -z "$encrypted_713170cfc4d9_iv" ]
then
  echo "Travis encryption key and/or IV not present - skipping deploy."
  exit 0
fi

# Should now be safe to deploy

# Decrypt the deploy key and add it as a git remote
openssl aes-256-cbc -K $encrypted_713170cfc4d9_key -iv $encrypted_713170cfc4d9_iv
  -in deploy_key.enc -out deploy_key -d
chmod 600 deploy_key
mv deploy_key ~/.ssh/id_rsa
git remote add deploy ssh://git@github.com/${TRAVIS_REPO_SLUG}.git

# Publish the site live
make publish github

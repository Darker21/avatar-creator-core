#!/usr/bin/env bash

PACKAGE_NAME="avatar-creator-core"
NEXT_BETA=$(curl -s https://pypi.org/pypi/$PACKAGE_NAME/json | python3 -c "
import sys, json, re
json_data = json.load(sys.stdin)
releases = json_data['releases']
info = json_data['info']

latest_version = info.get('version')
if not latest_version:
    latest_version = '1.0.0'
major, minor, patch = latest_version.split('.')
patch = int(patch) + 1
next_version = f'{major}.{minor}.{patch}'

beta_versions = [v for v in releases.keys() if 'beta' in v]
if beta_versions:
    nums = [int(re.search(r'beta-?(\d+)', v).group(1)) for v in beta_versions if re.search(r'beta-?(\d+)', v)]
    latest_beta = max(nums)
    print(f'{next_version}-beta.{latest_beta + 1}')
else:
    print(f'{next_version}-beta.1')
")

VERSION=$NEXT_BETA

echo "Package version: $VERSION"
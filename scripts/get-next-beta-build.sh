#!/usr/bin/env bash

PACKAGE_NAME="avatar-creator-core"
LATEST_BETA=$(curl -s https://pypi.org/pypi/$PACKAGE_NAME/json | python3 -c "
import sys, json, re
releases = json.load(sys.stdin)['releases']
beta_versions = [v for v in releases.keys() if 'beta' in v]
if beta_versions:
    nums = [int(re.search(r'beta-?(\d+)', v).group(1)) for v in beta_versions if re.search(r'beta-?(\d+)', v)]
    print(f'{max(nums)}')
else:
    print('0')
")

if [ -z "$LATEST_BETA" ] || [[ "$LATEST_BETA" == *"ModuleNotFoundError"* ]]; then
    VERSION="1.0.0-beta.1"
else
    VERSION="1.0.0-beta.$((LATEST_BETA + 1))"
fi

echo "Package version: $VERSION"
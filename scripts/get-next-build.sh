#!/usr/bin/env bash

PACKAGE_NAME="avatar-creator-core"

LATEST_VERSION=$(curl -s https://pypi.org/pypi/$PACKAGE_NAME/json | python3 -c "import sys, json; print(json.load(sys.stdin)['info'].get('version', ''))" || true)
if [ -z "$LATEST_VERSION" ] || [[ "$LATEST_VERSION" == *"ModuleNotFoundError"* ]]; then
    VERSION="1.0.0"
else
    VERSION=$LATEST_VERSION
fi

IFS='.' read -r MAJOR MINOR PATCH <<< "$VERSION"
PATCH=$((PATCH + 1))
VERSION="${MAJOR}.${MINOR}.${PATCH}"
echo "Package version: $VERSION"

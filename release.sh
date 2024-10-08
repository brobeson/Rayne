#!/usr/bin/bash

# cspell:ignore testpypi

# Must enter the new version on the command line.
if [[ $# -ne 2 ]]; then
  echo "error: must enter the version and PyPI token file"
  exit 1
fi

set -e
git switch main

# Update version values in files.
sed --in-place "s/^version = \".*\"$/version = \"${1}\"/" pyproject.toml docs/conf.py
sed --in-place "s/^release = \".*\"$/release = \"${1}\"/" docs/conf.py

# Commit, tag, and push.
git add .
git commit -m "Release v${1}"
git push
git tag "v${1}"
git push --tags

# Clean rebuild and publish.
rm -r dist/
python3 -m build
TWINE_PASSWORD=$(<"$2") twine upload dist/*

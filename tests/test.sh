#!/bin/bash
set -uo pipefail

# pytest is baked into the environment image (environment/Dockerfile).
mkdir -p /logs/verifier
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
test_status=$?

if [ "$test_status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

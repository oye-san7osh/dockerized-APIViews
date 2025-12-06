#!/bin/bash

set -e

echo "Starting Django Application......"

# apply database migration
python manage.py migrate

exec "$@"
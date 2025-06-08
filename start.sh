#!/bin/bash
echo "Starting Gunicorn on port $PORT..."
exec gunicorn server:app --bind 0.0.0.0:$PORT --workers 3 --timeout 120

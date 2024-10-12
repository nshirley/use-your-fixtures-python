#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Start the Flask API server in the background
echo "Starting API server..."
FLASK_APP=api/app.py flask run &

# Get the process ID of the Flask server so we can stop it later
FLASK_PID=$!

# Wait for the server to start up
until curl -s http://127.0.0.1:5000/health; do
  echo "Waiting for API to be ready..."
  sleep 1
done

# Run the tests
echo "Running tests..."
pytest

# Kill the Flask server after tests are done
kill $FLASK_PID

echo "Server stopped and tests completed."
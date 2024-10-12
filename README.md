# Example API and Tests with pytest

This repository contains a simple mock API and pytest tests that demonstrate how to use fixtures to cache authentication tokens and make API requests. This pairs with the blog post over at [testinglimits](testinglimits.blog)

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```


## Running the API

To start the API locally:

```bash
source .venv/bin/activate
python api/app.py
```

Alternatively, you can use the vscode debug profile after configuring the python env.

## Running tests

You can use the shell script `run_tests_local.sh`, this will start the API then run tests (which point to local) and then shuts down the server when done. 
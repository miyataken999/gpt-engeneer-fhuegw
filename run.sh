#!/bin/bash

# Install dependencies
python -m pip install --user -r requirements.txt

# Run tests in parallel
pytest tests/test_script_executor.py tests/test_script_parser.py tests/test_test_executor.py

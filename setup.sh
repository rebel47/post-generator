#!/bin/bash

echo "========================================"
echo "  LinkedIn Post Generator - Setup"
echo "========================================"
echo ""

echo "Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7+ from python.org"
    exit 1
fi
echo ""

echo "Installing dependencies..."
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
echo ""

echo "Testing installation..."
python3 test_installation.py
echo ""

echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "  1. Run demo: python3 demo.py"
echo "  2. Try CLI: python3 cli.py --help"
echo "  3. Check examples: ls examples/"
echo "  4. Read documentation: README.md"
echo ""

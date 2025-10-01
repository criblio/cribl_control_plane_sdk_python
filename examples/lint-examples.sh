#!/bin/bash
set -e

echo "🔍 Linting examples directory..."

# Change to project root from examples directory
cd "$(dirname "$0")/.."

# Install examples dependencies if not already installed
if [ ! -d "examples/examples-env" ]; then
    echo "📦 Installing examples dependencies..."
    pip install -r examples/requirements.txt
fi

echo "🔍 Running pylint on examples..."
poetry run pylint examples/*.py --fail-under=9.0

echo "🔍 Running mypy type checking on examples..."
poetry run mypy examples/ --config-file examples/mypy.ini

echo "🔍 Running pyright type checking for strict type validation..."
if command -v pyright &> /dev/null; then
    cd examples/
    # Run pyright with poetry's python environment
    POETRY_PYTHON_PATH=$(cd .. && poetry run which python)
    export PYRIGHT_PYTHON_PATH="$POETRY_PYTHON_PATH"
    
    # Run pyright - only errors should fail the build
    pyright . --pythonpath ../src
    PYRIGHT_EXIT_CODE=$?
    
    if [ $PYRIGHT_EXIT_CODE -ne 0 ]; then
        echo "⚠️ Pyright found issues, but continuing (non-critical for examples)"
    fi
    
    cd ..
    echo "✅ Pyright type checking completed!"
else
    echo "⚠️ Pyright not available, skipping strict type checking"
    echo "   To install: npm install -g pyright"
fi

echo "🔍 Running custom ProductsCore validation..."
# Custom check for ProductsCore usage
PRODUCT_ERRORS=$(grep -n 'product="stream"\|product="edge"' examples/*.py || true)
if [ ! -z "$PRODUCT_ERRORS" ]; then
    echo "❌ Found ProductsCore type errors:"
    echo "$PRODUCT_ERRORS"
    echo ""
    echo "💡 Fix: Use ProductsCore.STREAM or ProductsCore.EDGE instead of string literals"
    exit 1
else
    echo "✅ No ProductsCore type errors found!"
fi

echo "✅ Examples linting completed successfully!"

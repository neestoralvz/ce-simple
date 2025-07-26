#!/bin/bash

# Setup Git Hooks for VDD Coherence Validation

echo "Setting up VDD Git hooks..."

# Configure Git to use our hooks directory
git config core.hooksPath .githooks

echo "✅ Git hooks configured"
echo "Pre-commit hook will now validate coherence before each commit"
echo
echo "To test the hook manually:"
echo "  .githooks/pre-commit"
echo
echo "To bypass hook temporarily (not recommended):"
echo "  git commit --no-verify"
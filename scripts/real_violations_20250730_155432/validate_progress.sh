#!/bin/bash
# Quick validation of extraction progress

CONTEXT_DIR="/Users/nalve/ce-simple/context"
echo "🔍 Current violation status (excluding backups):"
find "$CONTEXT_DIR" -name "*.md" \
    -not -path "*/archive/*" \
    -not -path "*backup*" \
    -not -path "*BACKUP*" \
    -not -name "*backup*" \
    -not -name "*BACKUP*" \
    -exec wc -l {} + | \
    awk '$1 > 80 && $2 !~ /backup|BACKUP/ {print $1, $2}' | \
    sort -nr | wc -l | tr -d ' '
echo "violations remaining"

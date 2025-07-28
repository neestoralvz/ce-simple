#!/bin/bash

# Database Maintenance Script for Health Monitoring
# Optimizes health.db by removing old records and compacting

DB_PATH="/Users/nalve/ce-simple/data/monitoring/health.db"
BACKUP_DIR="/Users/nalve/ce-simple/data/monitoring/backups"
RETENTION_HOURS=1

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Create timestamped backup
BACKUP_FILE="$BACKUP_DIR/health.db.backup.$(date +%Y%m%d_%H%M%S)"
cp "$DB_PATH" "$BACKUP_FILE"

echo "Backup created: $BACKUP_FILE"

# Get initial size
INITIAL_SIZE=$(stat -f%z "$DB_PATH")
echo "Initial database size: $INITIAL_SIZE bytes"

# Clean old records (keep only last hour)
sqlite3 "$DB_PATH" "DELETE FROM health_metrics WHERE timestamp < datetime('now', '-${RETENTION_HOURS} hours');"

# Remove old behavioral data (keep only last 24 hours)
sqlite3 "$DB_PATH" "DELETE FROM behavioral_compliance WHERE timestamp < datetime('now', '-24 hours');"
sqlite3 "$DB_PATH" "DELETE FROM behavioral_violations WHERE timestamp < datetime('now', '-24 hours');"
sqlite3 "$DB_PATH" "DELETE FROM behavioral_health_metrics WHERE timestamp < datetime('now', '-24 hours');"

# Compact database
sqlite3 "$DB_PATH" "VACUUM;"

# Get final size
FINAL_SIZE=$(stat -f%z "$DB_PATH")
SAVED_BYTES=$((INITIAL_SIZE - FINAL_SIZE))
SAVED_PERCENT=$((SAVED_BYTES * 100 / INITIAL_SIZE))

echo "Final database size: $FINAL_SIZE bytes"
echo "Space saved: $SAVED_BYTES bytes ($SAVED_PERCENT%)"

# Keep only last 7 backup files
find "$BACKUP_DIR" -name "health.db.backup.*" -type f | sort -r | tail -n +8 | xargs rm -f

echo "Database maintenance completed successfully"
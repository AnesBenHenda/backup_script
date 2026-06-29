#!/bin/bash
SOURCE_DIR="${1:-$HOME/test}"
BACKUP_DIR="${2:-$HOME/test_backup}"

LOG_DIR="${BACKUP_DIR}/logs"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

ARCHIVE_NAME="backup_$(basename "$SOURCE_DIR")_${TIMESTAMP}.tar.gz"

ARCHIVE_PATH="${BACKUP_DIR}/${ARCHIVE_NAME}"

LOG_FILE="${LOG_DIR}/backup_${TIMESTAMP}.log"

log()  { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INFO]  $*" | tee -a "$LOG_FILE"; }
warn() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [WARN]  $*" | tee -a "$LOG_FILE"; }
err()  { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [ERROR] $*" | tee -a "$LOG_FILE" >&2; }

ok()   { echo "[$(date '+%Y-%m-%d %H:%M:%S')] [OK]    $*" | tee -a "$LOG_FILE"; }


mkdir -p "$BACKUP_DIR" "$LOG_DIR"

: > "$LOG_FILE"

log "============================================"
log "  Backup script started"
log "  Source      : $SOURCE_DIR"
log "  Destination : $BACKUP_DIR"
log "  Log file    : $LOG_FILE"
log "============================================"


log " start compression........"
log " source: $SOURCE_DIR"
log " archive: $ARCHIVE_PATH "

tar -czf "$ARCHIVE_PATH" \
     -C "$(dirname $SOURCE_DIR)" \
     "$(basename "$SOURCE_DIR")" \
     2>>"$LOG_FILE"


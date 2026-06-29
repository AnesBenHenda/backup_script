#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from datetime import datetime
import logging
import subprocess


source_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "test"
backup_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.home() / "test_backup"

log_dir=backup_dir/"logs"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


archive_name=f"backup_{Path (source_dir).name}_{timestamp}.tar.gz"

log_file=f"{log_dir}/backup_{timestamp}.log"

archive_path = backup_dir / archive_name

result = subprocess.run(
    ["mkdir", "-p", backup_dir, log_dir],
    capture_output=True,
    text=True,
    check=True,
)

result = subprocess.run(
    ["touch",log_file],
    capture_output=True,
    text=True,
    check=True,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

log = logging.getLogger(__name__)
try:
	log.info("Starting backup")
	log.warning("Disk almost full")
except Exception as e:
	log.error("Failed: %s", str(e))


log.info("============================================")
log.info("  Backup script started")
log.info("  Source      : %s", source_dir)
log.info("  Destination : %s", backup_dir)
log.info("  Log file    : %s", log_file)

log.info("============================================")
log.info("  Starting compression...")
log.info("  Source  : %s", source_dir)
log.info("  Archive : %s", archive_path)

try:
	result = subprocess.run(
	["tar", "-czf", str(archive_path), "-C", str(source_dir.parent), source_dir.name],
    	capture_output=True,
    	text=True,
    	check=True,
	)
	log.info("Backup completed sucssefully")
except Exception as e:
    log.error("Failed: %s", e)

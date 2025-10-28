import logging
import sys

# 1. Define a custom Handler class
class CustomLevelFilter(logging.Filter):
    def filter(self, record):
        # Only allow records with level WARNING or higher
        return record.levelno >= logging.WARNING

# 2. Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 3. Create a StreamHandler for console output
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG) # Handle all levels initially

# 4. Attach the custom filter to the handler
handler.addFilter(CustomLevelFilter())

# 5. Attach the handler to the logger
logger.addHandler(handler)

print("--- Logging Demonstration (Only WARNING and above appear) ---")
logger.debug("This message won't show in the console.")
logger.info("This info message won't show either.")
logger.warning("Warning: Disk space is getting low.")
logger.error("Error: Could not connect to the database.")

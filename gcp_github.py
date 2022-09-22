from google.cloud import storage, bigquery, logging


logger = logging_client.logger("ms-log")
logger.log_text("finished successfully!")

from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.logging import logger

if __name__ == "__main__":
    try:
        logger.info("Stage 01: Data Ingestion started")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info("Stage 01: Data Ingestion completed")
    except Exception as e:
        logger.exception(e)
        raise e
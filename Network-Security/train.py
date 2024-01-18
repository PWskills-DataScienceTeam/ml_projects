import sys

from network.exception import NetworkException
from network.pipeline.training_pipeline import TrainPipeline
from network.utils.main_utils import sync_artifacts


def start_training():
    """
    It runs a training pipeline, and if it fails, it raises an exception and syncs the app artifacts
    """
    try:
        tp = TrainPipeline()

        tp.run_pipeline()

    except Exception as e:
        raise NetworkException(e, sys)

    finally:
        sync_artifacts()


if __name__ == "__main__":
    start_training()

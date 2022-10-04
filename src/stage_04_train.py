from src.utils.all_utils import read_yaml,create_directory
import argparse
import os
import logging

# logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(messages)s]"
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'runnig_logs.log'), level=logging.INFO, filemode='a')

def train_model(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]

    


if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args = args.parse_args()
    try:
        logging.info(">>>>> Stage four started")
        train_model(config_path = parsed_args.config, params_path = parsed_args.params)
        logging.info("stage four completd! Training completed and model saved >>>>>\n")
    except Exception as e:
        logging.exception(e)
        raise e

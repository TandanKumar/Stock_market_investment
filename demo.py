from stock_market.pipeline.pipeline import Pipeline
from stock_market.exception import stockmarketException
from stock_market.logger import logging
from stock_market.config.configuration import Configuartion

def main():
    try:
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        data_validation_config = Configuartion.get_data_validation_config()
        print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()

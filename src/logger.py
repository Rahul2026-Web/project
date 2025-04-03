import logging
import os
from datetime import datetime

LOG_FTILE=f"{datetime.now().strftime('%m_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FTILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FTILE_PATH=os.path.join(logs_path,LOG_FTILE)

logging.basicConfig(
    filename=LOG_FTILE_PATH,
    format="[ %(asctime)s]%(lineno)d %(name)s -%(levelnames)s -%(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("Logging has started")
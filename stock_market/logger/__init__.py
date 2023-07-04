import logging
from datetime import datetime
import os


Log_DIR = "Stock_logs"
Current_Time_Stamp  = f"{datetime.now().strftime('%y-%m-%d_%H-%M-%S')}"
Log_File_name = f"log_{Current_Time_Stamp}.log"

os.makedirs(Log_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(Log_DIR,Log_File_name)

logging.basicConfig(filename = LOG_FILE_PATH,filemode ='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',level = logging.INFO)

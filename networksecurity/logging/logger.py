import logging
import os
from datetime import datetime

LOG_FILES = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILES)

os.makedirs(logs_path,exist_ok=True)
LOG_FILES_PATH = os.path.join(logs_path,LOG_FILES)

logging.basicConfig(
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
    
    
)

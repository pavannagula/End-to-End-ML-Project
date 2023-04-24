# Logger is used to log all execution and error messages to a file which helps for further analysis
import logging
import os
from datetime import datetime

Log_File = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", Log_File) # It will create Log folder and stores all log files in the source file

os.makedirs(logs_path, exist_ok=True) # Even though there is files or folders keeps on appending
Log_File_Path = os.path.join(logs_path, Log_File)

logging.basicConfig(
    filename= Log_File_Path,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO,
    )


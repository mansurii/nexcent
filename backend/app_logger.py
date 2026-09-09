import logging

class AppLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='backend/logs/app_log.log', encoding='utf-8', level=logging.DEBUG)
        self.console = logging.StreamHandler()
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.console.setFormatter(self.formatter)
        self.logger.addHandler(self.console)

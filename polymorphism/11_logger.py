class Logger:
    def log(self, message, level='info'):
        if level == 'error':
            print(f"ERROR: {message}")
        elif level == 'warning':
            print(f"WARNING: {message}")
        else:
            print(f"INFO: {message}")

logger = Logger()
message = input("Enter message: ")
level = input("Enter level (error, warning, info): ")
logger.log(message, level)

from datetime import datetime

LOG_FILE = "audit.log"

def log_action(username, action):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {username} | {action}\n")
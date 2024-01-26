from datetime import datetime


def save_log(entry):
    with open(f"log_saves/{datetime.utcnow().strftime('%Y_%m_%d')}", "a") as file:
        file.write(f'{datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC:")} {entry} \n')
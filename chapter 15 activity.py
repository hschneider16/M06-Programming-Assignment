import multiprocessing
import random
import time
from datetime import datetime

def process_func():
    wait_time = random.random()
    time.sleep(wait_time)
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"Process ID: {multiprocessing.current_process().pid}, Current Time: {current_time}")

if __name__ == '__main__':
    processes = []
    
    for _ in range(3):
        process = multiprocessing.Process(target=process_func)
        process.start()
        processes.append(process)
    
    for process in processes:
        process.join()
import time

from multiprocessing import Process

def worker():
    for i in range(100):
        print(f">>> Woreker : {i}")
        time.sleep(0.5)
    
if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    
    cnt = 0
    while p.is_alive():
        print(f">>> Main : {cnt} MainMainMainMainMainMainMainMainMainMainMain")
        print("포멧터를 테스트 해봅니다. 포멧터를 테스트 해봅니다. 포멧터를 테스트 해봅니다. 포멧터를 테스트 해봅니다.")
        time.sleep(5)
    p.join()
# asyncio.run(coro)
# if __name__ == "__main__":
    
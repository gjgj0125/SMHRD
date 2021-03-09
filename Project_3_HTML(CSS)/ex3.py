from multiprocessing import Process
import time

start_time = time.time();
def guguVertical():
    for n in range(1, 10):  # 단 수가 밖에 존재.
        for m in range(2, 10):
            print(f'{n} x {m} = {n * m}') 

if __name__ == "__main__":
    p = Process(target=guguVertical)
    p.start()
    p.join()



print("--- %s seconds ---" % (time.time() - start_time))

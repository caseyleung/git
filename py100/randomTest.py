from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # å¯å¨8ä¸ªè¿ç¨å°æ°æ®åçåè¿è¡è¿ç®
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # å¼å§è®°å½ææè¿ç¨æ§è¡å®æè±è´¹çæ¶é´
    start = time()
    for p in processes:
        p.join()
    # åå¹¶æ§è¡ç»æ
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == '__main__':
    main()
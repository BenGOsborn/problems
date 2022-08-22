import threading
from time import sleep

data_lock = threading.Lock()

data = []


def produce(amount, id):
    for i in range(amount):
        data_lock.acquire()

        data.append(f"TP{id}:{i}")

        data_lock.release()


def consume(id):
    retries = 3
    remainder = retries

    while remainder > 0:
        data_lock.acquire()

        if len(data) == 0:
            remainder -= 1
        else:
            print(f"TC{id}:{data.pop(0)}")

            remainder = retries

        data_lock.release()

        sleep(1)


def main():
    PRODUCERS = 10
    PRODUCE_AMOUNT = 10
    CONSUMERS = 100

    producers = []
    consumers = []

    for i in range(PRODUCERS):
        thread = threading.Thread(target=produce, args=(PRODUCE_AMOUNT, i))
        thread.start()
        producers.append(thread)

    for i in range(CONSUMERS):
        thread = threading.Thread(target=consume, args=(i,))
        thread.start()
        consumers.append(thread)

    for thread in producers + consumers:
        thread.join()


if __name__ == "__main__":
    main()

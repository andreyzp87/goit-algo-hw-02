import random
from queue import Queue
from time import sleep

from faker import Faker

queue = Queue()
fake = Faker()


def generate_request():
    task = {
        'id': fake.random_number(),
        'name': fake.name(),
    }

    queue.put(task)
    print(f"Заявка створена: {task}")


def process_request():
    if not queue.empty():
        task = queue.get()
        print(f"Заявка оброблена: {task}")
    else:
        print("Черга пуста")


if __name__ == '__main__':
    while True:
        if random.randint(0, 1) < 0.5:
            generate_request()

        process_request()
        sleep(1)

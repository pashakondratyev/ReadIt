import time


def poll():
    return 0


def long_poll():
    while True:
        poll()
        time.sleep(.5)  # Sleeps .5 seconds between polls


if __name__ == '__main__':
    long_poll()
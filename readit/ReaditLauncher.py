import calendar
import time


def report(event):
    print(event)


def process(reddit_result, time_after):
    # TODO: Put code for parsing JSON here
    # TODO: For each event check if time < created_utc
    for event in reddit_result:
        if time_after < event.created_utc:
            report(event)
    return 0


def poll():
    return []


def long_poll():
    time_after = calendar.timegm(time.gmtime())
    while True:
        result = poll()
        process(result, time_after)
        time_after = calendar.timegm(time.gmtime())
        time.sleep(.5)  # Sleeps .5 seconds between polls


if __name__ == '__main__':
    long_poll()
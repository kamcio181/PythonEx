TIMEOUT = 5000  # example timeout


def process(retries):
    attempts = 0
    while attempts < retries:
        connection = connect()
        if connection is None:
            attempts += 1
            continue

        while True:
            try:
                record = get_next_record(connection, TIMEOUT)
                if record is None:
                    return  # all records processed, use 'continue' in order to check if new record showed up
                do_work(record)
            except ConnectionException:
                attempts = 0
                break
            except ProcessingException as pe:
                print(pe)
    raise ConnectionRefusedError


class ConnectionException(Exception):
    def __str__(self):
        return 'ConnectionException'


class ProcessingException(Exception):
    def __str__(self):
        return 'ProcessingException'


#  function mock


def get_next_record(connection, timeout):
    return 0


def connect():
    return 0


def do_work(record):
    pass


process(5)

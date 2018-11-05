TIMEOUT = 5000


def get_next_record(connection, timeout):
    return 0


def connect():
    return 0


def do_work(record):
    pass


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
                    return              #TODO None przerywa czy probuje pobrac kolejny?
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


process(5)

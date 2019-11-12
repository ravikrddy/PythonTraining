"""class members"""


# from datetime import datetime
# print(datetime.now())
class MaxConnectionError(Exception):
    """custom exception"""


class Connections:
    connection_counter = 0
    max_connections = 5  # class variable

    def __init__(self, connection_id):
        self.connection_id = connection_id
        Connections.connection_counter += 1
        Connections.check_4_limit()

    @classmethod
    def check_4_limit(cls):
        if cls.connection_counter > cls.max_connections:
            raise MaxConnectionError('reached the maximum allowed connections')


def main():
    try:
        list_of_connections = []
        for item in range(1, 11):
            list_of_connections.append(Connections(item))
    except MaxConnectionError as err:
        print(err)
    for conn in list_of_connections:
        print(conn)


if __name__ == '__main__':
    main()

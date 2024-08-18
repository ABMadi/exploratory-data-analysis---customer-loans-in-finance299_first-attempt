class RDSDatabaseConnector:
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        """
        Initialize the RDSDatabaseConnector with the required database connection parameters.
        
        :param host: The hostname of the RDS database.
        :param user: The username for the database.
        :param password: The password for the database.
        :param database: The name of the database to connect to.
        :param port: The port number for the database connection (default is 3306).
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

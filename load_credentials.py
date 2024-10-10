import yaml

def load_credentials(filepath: str) -> dict:
    """
    Load credentials from a YAML file and return as a dictionary.

    :param filepath: Path to the credentials YAML file.
    :return: Dictionary containing the credentials.
    """
    with open(filepath, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials

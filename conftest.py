import yaml
from pytest import fixture

from qa_challenge.model.credentials import Credentials


@fixture
def credentials():
    with open("credentials.yaml") as yaml_file:
        credentials_yaml = yaml.load(yaml_file)
        return Credentials(credentials_yaml.get("email"), credentials_yaml.get("password"))

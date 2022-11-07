import yaml


def read_props():
    with open("properties.yml", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

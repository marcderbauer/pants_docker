import yaml
from typing import Any


class Component():

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config

    @classmethod
    def create_component(cls, yaml_path: str):
        with open(yaml_path, "r") as f:
            config = yaml.safe_load(f)
        return cls(config)
    
    def pong(self):
        return "comPONGnent"
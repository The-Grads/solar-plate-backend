from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    @abstractmethod
    def build(self, json_data: dict):
        raise NotImplementedError()

    @abstractmethod
    def build_from_model(self, model):
        raise NotImplementedError()

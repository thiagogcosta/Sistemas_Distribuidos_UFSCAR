from abc import ABC, abstractmethod


class Classifier(ABC):
    _instance_image_classifier = None

    @classmethod
    def instance(cls):
        if cls._instance_image_classifier is None:
            cls._instance_image_classifier = cls()
        return cls._instance_image_classifier

    @abstractmethod
    def captar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def preprocessar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def configurar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def treinar(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def testar(self) -> None:
        raise NotImplementedError

    def executar(self) -> None:
        self.captar()
        self.preprocessar()
        self.treinar()
        self.testar()

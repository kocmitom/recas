from abc import ABC, abstractmethod


class Recipe(ABC):

    @property
    @abstractmethod
    def license(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def authors(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def url(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def paper(self):
        raise NotImplementedError

    def getInfo(self):
        return {"license": self.license(),
                "authors": self.authors(),
                "url": self.url(),
                "paper": self.paper()
                }

    @abstractmethod
    def prepare(self):
        pass

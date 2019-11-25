from dataclasses import dataclass

__author__ = 'karims'


@dataclass
class BaseComponentData(object):

    def as_dict(self):
        return self.__dict__

    def collect(self, data: 'BaseComponentData'):
        self.__setattr__(str(data.__class__), data)

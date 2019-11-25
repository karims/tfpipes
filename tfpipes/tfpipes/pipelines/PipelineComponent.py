from typing import List

import abc

from tfpipes.tfpipes.pipelines.ComponentData import BaseComponentData

__author__ = 'karims'


class PipelineComponent(abc.ABC):

    def __init__(self,
                 expects: type(BaseComponentData),
                 filters: List['PipelineComponent'] = None) -> None:
        self.filters = filters
        self.expects = expects

    @abc.abstractmethod
    def execute(self, data: BaseComponentData) -> BaseComponentData:
        pass

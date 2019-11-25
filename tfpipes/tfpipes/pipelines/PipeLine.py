from typing import List

from tfpipes.tfpipes.pipelines.ComponentData import BaseComponentData
from tfpipes.tfpipes.pipelines.PipelineComponent import PipelineComponent

__author__ = 'karims'


class PipeLine:
    """
    Pipeline construction class
    """
    def __init__(self, name, init_data: BaseComponentData, output_class: str):
        self.name = name
        self.components: List['PipelineComponent'] = []
        self.init_data = init_data
        self.output_class = output_class

    def run(self) -> BaseComponentData:
        """ Runs the pipeline """
        res = BaseComponentData()
        res.collect(self.init_data)
        for c in self.components:
            ex = c.expects
            if not hasattr(res, str(ex)):
                raise Exception('Type does not match')
            else:
                stage_output = c.execute(res.__getattribute__(str(ex)))
                res.collect(stage_output)
        if self.output_class:
            return res.__getattribute__(self.output_class)
        else:
            return res

    def add(self, component: PipelineComponent):
        """
        Adds a component to the pipeline
        :param component: Component class as defined by PipelineComponent
        :return:
        """
        if not isinstance(component, PipelineComponent):
            raise Exception('Given component is not a subclass of PipelineComponent')
        if component:
            self.components.append(component)
        else:
            raise Exception('Pipeline component is None or Empty')


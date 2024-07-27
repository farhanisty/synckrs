from .RenderEngine import RenderEngine
from src.Matkul import Matkul


class RenderInvoker:
    def __init__(self, renderEngine: RenderEngine):
        self.renderEngine = renderEngine

    def changeRenderEngine(self, renderEngine: RenderEngine):
        self.__init__(renderEngine)

    def render(self, matkuls: list[Matkul]):
        self.renderEngine.render(matkuls)

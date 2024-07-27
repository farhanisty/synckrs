from .RenderEngine import RenderEngine
from src.Matkul import Matkul
from src.sorter.MatkulSorter import MatkulSorter


class RenderInvoker:
    def __init__(self, renderEngine: RenderEngine):
        self.sorter = None
        self.sortMode = "ASC"
        self.changeRenderEngine(renderEngine)

    def sort(self, matkulSorter: MatkulSorter):
        self.sorter = matkulSorter
        return self

    def changeMode(self, mode: str):
        if mode.upper() in ["ASC", "DESC"]:
            self.sortMode = mode

        return self

    def changeRenderEngine(self, renderEngine: RenderEngine):
        self.renderEngine = renderEngine
        return self

    def render(self, matkuls: list[Matkul]):
        if self.sorter is not None:
            self.sorter.execute(matkuls, self.sortMode)
        self.renderEngine.render(matkuls)

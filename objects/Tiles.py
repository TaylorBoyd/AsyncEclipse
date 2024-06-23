class Tile:

    def __init__(self, id, name, moneyPop, sciencePop, materialPop, neutralPop, wormholes, vp):
        self.id = id
        self.name = name

        self.moneyPop = moneyPop[0]
        self.moneyPopAdvanced = moneyPop[1]

        self.sciencePop = sciencePop[0]
        self.sciencePopAdvanced = sciencePop[1]

        self.materialPop = materialPop[0]
        self.materialPopAdvanced = materialPop[1]

        self.neutralPop = neutralPop[0]
        self.neutralPopAdvnaced = neutralPop[1]

        self.wormholes = wormholes

        self.vp = vp



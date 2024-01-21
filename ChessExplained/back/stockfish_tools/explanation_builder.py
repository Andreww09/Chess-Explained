class ExplanationBuilder:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.build_explanation()

    def build_explanation(self):
        explanation = ""
        explanation += self.castling_explanation(self.dictionary['castling'])
        explanation += self.pawn_promotion_explanation(self.dictionary['pawn_promotion'])
        explanation += self.sacrifice_explanation(self.dictionary['sacrifice'])
        return explanation

    @staticmethod
    def castling_explanation(info):
        if info['enable'] is False:
            return ""

        if info['side'] == "KingSide":
            return "It moves your king to safety."

        return "It moves your king to safety while putting the rook on a more active square."

    @staticmethod
    def pawn_promotion_explanation(info):
        if info['enable'] is False:
            return ""

        return f"It promotes the pawn to a {info['piece']}"

    @staticmethod
    def sacrifice_explanation(info):
        if info['enable'] is False:
            return ""

        if info['capture'] is False:
            return f"It sacrifices the {info['sacrificed']} to gain an advantage"

        return f"It sacrifices the {info['sacrificed']} for a {info['captured']} to gain an advantage"

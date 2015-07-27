
class Scorer:
    def __init__(self, scoresheet):
        self.scoresheet = scoresheet

    def calculate_score(self, data):
        gold, silver = data.get('gold', 0), data.get('silver', 0)
        moved = data.get('moved', False)
        token_score = 2*(gold + silver) // (2 if gold and silver else 1)
        return token_score + int(moved)

    def calculate_scores(self):
        return {tla: self.calculate_score(data)
                for tla, data in self.scoresheet.items()}

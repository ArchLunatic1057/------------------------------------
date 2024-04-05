class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def execute_strategy(self):
        if self.strategy == "1" or str(self.strategy) == "1":    strategy = strategyOne()
        elif self.strategy == "2" or str(self.strategy) == "2":  strategy = strategyTwo()
        else: raise ValueError("Invalid strategy")
        strategy.execute()

class strategyOne:
    def execute(self): print("Executing Strategy One")
class strategyTwo:
    def execute(self): print("Executing Strategy Two")

context = Context(input("Choose Strategy: 1 or 2 >> ")).execute_strategy()
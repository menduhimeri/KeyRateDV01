class Scenario:
    """
    Represents a yield curve shock scenario.
    Shock values in basis points.
    """

    def __init__(self, name: str, shocks: dict[str, float]):
        self.name = name
        self.shocks = shocks

    def get_shock(self, column: str) -> float:
        return self.shocks.get(column, 0.0)

    def __repr__(self):
        return f"Scenario({self.name})"

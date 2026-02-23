class DashboardKPIs:
    def __init__(
        self,
        total_ca: float,
        total_carburant: float,
        benefice_total: float,
        dernier_plein: float,
        total_distance: int
    ):
        self.total_ca = total_ca
        self.total_carburant = total_carburant
        self.benefice_total = benefice_total
        self.dernier_plein = dernier_plein
        self.total_distance = total_distance

    def to_dict(self):
        return self.__dict__


class DashboardKPIs:
    def __init__(
        self,
        total_ca: float,
        total_carburant: float,
        benefice_total: float,
        dernier_plein: float,
        total_distance: int,
        benefice_net: float,
        ca_du_jour: float = 0.0,
        distance_du_jour: int = 0.0,
        benefice_net_du_jour: float = 0.0
    ):
        self.total_ca = total_ca
        self.total_carburant = total_carburant
        self.benefice_total = benefice_total
        self.dernier_plein = dernier_plein
        self.total_distance = total_distance
        self.benefice_net = benefice_net
        self.ca_du_jour = ca_du_jour
        self.distance_du_jour = distance_du_jour
        self.benefice_net_du_jour = benefice_net_du_jour

    def to_dict(self):
        return self.__dict__


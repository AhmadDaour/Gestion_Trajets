class ServicesKPIs:
    def __init__(
        self,
        ca_du_jour: float
    ):
        self.ca_du_jour = ca_du_jour

    def to_dict(self):
        return self.__dict__


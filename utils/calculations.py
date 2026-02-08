
class Calculations: 

    @staticmethod
    def total_CA(trips: list[dict]) -> float:
        return sum(trip["prix"] for trip in trips)
    
    @staticmethod
    def total_fuels(fuels: list[dict]) -> float:
        return sum(fuel["prix_total"] for fuel in fuels)
    
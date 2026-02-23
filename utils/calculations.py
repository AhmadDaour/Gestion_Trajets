
class Calculations: 

    @staticmethod
    def total_CA(trips: list[dict]) -> float:
        return sum(trip["prix"] for trip in trips)
    
    @staticmethod
    def benefice_net(trips: list[dict]) -> float:
        return sum(trip["benefice"] for trip in trips)
    
    @staticmethod
    def total_distance(trips: list[dict]) -> int:
        return sum(trip["distance"] for trip in trips)
    
    @staticmethod
    def total_fuels(fuels: list[dict]) -> float:
        return sum(fuel["prix_total"] for fuel in fuels)

    
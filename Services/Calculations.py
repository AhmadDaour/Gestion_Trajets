from Services.utils import supabase

class Calculations:
    """
    Performing the calculations related to trips.
    """

    @staticmethod
    def Coast_Per_Kilometer():
        """
        Calculates the cost per kilometer using the formula:
        average_consumption_per_km * price_per_liter from the 'carburants' table in Supabase.
        
        :return: Cost per kilometer (float).
        :raises Exception: In case of query error or missing data.
        """
        try:
            # Retrieve the latest entry from the 'carburants' table (sorted by date descending)
            response = supabase.table("carburants").select("consommation_moyenne_par_km, prix_litre").order("date", desc=True).limit(1).execute()
            if not response.data:
                raise ValueError("No data found in the 'carburants' table.")
            
            data = response.data[0]
            consommation = data["consommation_moyenne_par_km"]
            prix_litre = data["prix_litre"]
            
            if consommation <= 0 or prix_litre <= 0:
                raise ValueError("Consumption or price values must be positive.")
            
            cout_par_km = consommation * prix_litre
            return cout_par_km
        except Exception as e:
            print(f"Error calculating cost per km: {str(e)}")
            raise

    @staticmethod
    def Profit_Calculation(distance, price):
        """
        Calculates the profit for a trip using the formulas:
        total_cost = cost_per_km * distance
        profit = price - total_cost
        
        Where distance and price are received as parameters, and cost_per_km is from the latest record in the 'carburants' table.
        
        :param distance: Distance of the trip (float).
        :param price: Price of the trip (float).
        :return: Profit (float).
        :raises Exception: In case of query error or missing data.
        """
        try:
            # Fetch cost_per_km from the latest 'carburants' record
            cost_per_km = Calculations.Coast_Per_Kilometer()
            
            # Calculate total cost and profit
            total_cost = cost_per_km * distance
            profit = price - total_cost
            
            return profit
        except Exception as e:
            print(f"Error calculating profit: {str(e)}")
            raise




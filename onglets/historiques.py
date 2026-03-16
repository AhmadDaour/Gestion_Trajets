import streamlit as st
import pandas as pd
from services.historiques_service import HistoriquesService
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

@st.cache_data
def load_trips():
    service = HistoriquesService()
    return service.get_trips()


def render_historiques():

    trips = load_trips()

    if not trips:
        st.info("Aucun trajet trouvé.")
        return
    df = pd.DataFrame(trips)

    # Configuration avancée du tableau
    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_default_column(
        sortable=True,
        filter=True,
        resizable=True
    )

    gb.configure_pagination(
        paginationAutoPageSize=False,
        paginationPageSize=10
    )

    grid_options = gb.build()

    AgGrid(
        df,
        gridOptions=grid_options,
        update_mode=GridUpdateMode.NO_UPDATE,
        fit_columns_on_grid_load=True,
        theme="streamlit",
    )
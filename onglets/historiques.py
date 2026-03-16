import streamlit as st
import pandas as pd
from services.historiques_service import HistoriquesService
from st_aggrid import AgGrid, GridOptionsBuilder
from ui.config.aggrid_local_FR  import AGGRID_LOCALE_FR

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
    # Export CSV
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Exporter CSV",
        csv,
        "trajets.csv",
        "text/csv"
    )

     # Recherche globale
    search = st.text_input("🔎 Rechercher un trajet")

    if search:
        df = df[df.astype(str).apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )]
        

    gb = GridOptionsBuilder.from_dataframe(df)

    gb.configure_default_column(
        sortable=True,
        filter=True,
        resizable=True
    )

    page_size = st.selectbox(
    "Nombre de lignes",
    [10, 20, 50, 100],
    index=0
)

    grid_options = gb.build()
    grid_options["localeText"] = AGGRID_LOCALE_FR
    grid_options["paginationPageSizeSelector"] = False

    grid = AgGrid(
        df,
        gridOptions=grid_options,
        theme="streamlit",
        use_container_width=True
    )


    gb.configure_pagination(
        paginationAutoPageSize=False,
        paginationPageSize=page_size
    )

    gb.configure_selection("single")

    selected = grid["selected_rows"]

    if selected:
        st.write("Trajet sélectionné :", selected[0])
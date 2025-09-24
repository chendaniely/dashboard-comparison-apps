import streamlit as st
from palmerpenguins import load_penguins
from plotnine import aes, geom_histogram, ggplot, theme_minimal

dat = load_penguins().dropna()
species = dat["species"].unique().tolist()

selected_species = st.radio("Species", species, horizontal=True)

sel = dat[dat["species"] == selected_species]

plot = (
    ggplot(aes(x="bill_length_mm"))
    + geom_histogram(dat, fill="#C2C2C4", binwidth=1)
    + geom_histogram(sel, fill="#447099", binwidth=1)
    + theme_minimal()
)

st.pyplot(ggplot.draw(plot))

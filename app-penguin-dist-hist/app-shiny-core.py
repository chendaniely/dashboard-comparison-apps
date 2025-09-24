from palmerpenguins import load_penguins
from plotnine import aes, geom_histogram, ggplot, theme_minimal
from shiny import App, render, ui

dat = load_penguins().dropna()
species = dat["species"].unique().tolist()

app_ui = ui.page_fluid(
    ui.input_radio_buttons("species", "Species", species, inline=True),
    ui.output_plot("plot"),
)


def server(input, output, session):
    @render.plot
    def plot():
        sel = dat[dat["species"] == input.species()]
        return (
            ggplot(aes(x="bill_length_mm"))
            + geom_histogram(dat, fill="#C2C2C4", binwidth=1)
            + geom_histogram(sel, fill="#447099", binwidth=1)
            + theme_minimal()
        )


app = App(app_ui, server)

library(ggplot2)
library(palmerpenguins)
library(shiny)
library(tidyverse)
library(shiny)
library(bslib)

dat <- penguins |>
  tidyr::drop_na()

species <- dat |>
  dplyr::distinct(species) |>
  dplyr::pull()

ui <- page_fluid(
  shiny::radioButtons(
    inputId = "species",
    label = "Species",
    choices = species,
    inline = TRUE
  ),
  shiny::plotOutput(outputId = "plot")
)

server <- function(input, output, session) {
  output$plot <- renderPlot({
    sel <- dat |>
      dplyr::filter(species == input$species)

    ggplot(dat, aes(x=bill_length_mm)) +
      geom_histogram()

  })
}

shiny::shinyApp(ui = ui, server = server)

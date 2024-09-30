# Cargar las librerías necesarias
library(shiny)
library(ggplot2)
library(dplyr)
library(caret)
library(gridExtra)

# Definir la UI
ui <- fluidPage(
  
  # Título de la aplicación
  titlePanel("Análisis de Regresión Múltiple - Boston Housing"),
  
  # Layout con barra lateral
  sidebarLayout(
    
    # Panel lateral para seleccionar las variables independientes
    sidebarPanel(
      checkboxGroupInput("variables", "Selecciona las variables independientes:",
                         choices = names(select(read.csv("Boston.csv"), -medv)), # Cargar las variables excluyendo "medv"
                         selected = c("age", "rm")),
      actionButton("run", "Ejecutar Modelo")
    ),
    
    # Panel principal para mostrar los gráficos y resultados
    mainPanel(
      h3(textOutput("model_title")),
      plotOutput("plot"),
      verbatimTextOutput("summary_output"),
      plotOutput("diagnostics_plots")
    )
  )
)

# Definir el server
server <- function(input, output) {
  
  # Cargar los datos al iniciar la aplicación
  datos1 <- read.csv("Boston.csv", head = TRUE, sep = ",")
  datos <- select(datos1, -medv)
  y <- datos1$medv  # Variable dependiente (medv)
  
  # Acción a ejecutar cuando se presione el botón "Ejecutar"
  observeEvent(input$run, {
    
    # Definir el tipo de modelo seleccionado por el usuario
    output$model_title <- renderText({
      paste("Modelo de Regresión Múltiple con Variables:", paste(input$variables, collapse = ", "))
    })
    
    # Crear el conjunto de datos con las variables seleccionadas
    datos_seleccionados <- select(datos1, one_of(input$variables))
    
    # Ajustar el modelo de regresión múltiple
    modelo_multiple <- lm(y ~ ., data = datos_seleccionados)
    
    # Mostrar el resumen del modelo
    output$summary_output <- renderPrint({
      summary(modelo_multiple)
    })
    
    # Crear gráficos de regresión múltiple
    output$plot <- renderPlot({
      # Graficar cada predictor vs. la variable dependiente
      plots <- lapply(names(datos_seleccionados), function(var) {
        ggplot(datos1, aes_string(x = var, y = "medv")) +
          geom_point(color = "blue") +
          geom_smooth(method = "lm", se = FALSE, color = "red") +
          labs(title = paste("Regresión: medv vs", var), x = var, y = "medv") +
          theme_bw()
      })
      
      # Combinar los gráficos en una sola salida
      do.call(grid.arrange, c(plots, ncol = 2))
    })
    
    # Crear gráficos de diagnóstico (residuos, etc.)
    output$diagnostics_plots <- renderPlot({
      par(mfrow = c(2, 2))
      plot(modelo_multiple)
    })
    
  })
}

# Ejecutar la aplicación Shiny
shinyApp(ui = ui, server = server)

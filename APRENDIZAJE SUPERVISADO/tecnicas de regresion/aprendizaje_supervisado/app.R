# Cargar las librerías necesarias
library(shiny)
library(ggplot2)
library(dplyr)
library(rpart)
library(rpart.plot)
library(boot)

# Definir la UI
ui <- fluidPage(
  
  # Título de la aplicación
  titlePanel("Análisis de Regresión Lineal y Modelos Complementarios - Boston Housing"),
  
  # Layout con barra lateral
  sidebarLayout(
    
    # Panel lateral para seleccionar el tipo de análisis
    sidebarPanel(
      selectInput("model_type", "Selecciona el Modelo:",
                  choices = c("Regresión Lineal", "Regresión Polinomial", "Árbol de Decisión", "Bootstrapping")),
      actionButton("run", "Ejecutar")
    ),
    
    # Panel principal para mostrar los resultados
    mainPanel(
      h3(textOutput("model_title")),
      plotOutput("plot"),
      verbatimTextOutput("summary_output")
    )
  )
)

# Definir el server
server <- function(input, output) {
  
  # Cargar los datos al iniciar la aplicación
  datos1 <- read.csv("Boston.csv", head = TRUE, sep = ",")
  datos <- select(datos1, age, medv)
  datos <- rename(Y = medv , X = age, .data = datos)
  
  # Acción a ejecutar cuando se presione el botón "Ejecutar"
  observeEvent(input$run, {
    
    # Definir el tipo de modelo seleccionado por el usuario
    output$model_title <- renderText({
      paste("Resultados del modelo:", input$model_type)
    })
    
    # Calcular el modelo y generar los gráficos según la selección del usuario
    if (input$model_type == "Regresión Lineal") {
      # Modelo de regresión lineal simple
      modelo_lineal <- lm(Y ~ X, data = datos)
      
      output$summary_output <- renderPrint({
        summary(modelo_lineal)
      })
      
      output$plot <- renderPlot({
        ggplot(data = datos, mapping = aes(x = X, y = Y)) + 
          geom_point(size = 3, color = "firebrick") + 
          geom_smooth(method = "lm", se = FALSE, color = "blue") +
          labs(title = "Regresión Lineal Simple", x = "Edad", y = "Valor Medio de Vivienda") +
          theme_bw()
      })
      
    } else if (input$model_type == "Regresión Polinomial") {
      # Modelo de regresión polinomial de segundo grado
      modelo_polinomial <- lm(Y ~ poly(X, 2), data = datos)
      
      output$summary_output <- renderPrint({
        summary(modelo_polinomial)
      })
      
      output$plot <- renderPlot({
        ggplot(data = datos, mapping = aes(x = X, y = Y)) + 
          geom_point(size = 3, color = "firebrick") + 
          geom_smooth(method = "lm", formula = y ~ poly(x, 2), se = FALSE, color = "green") +
          labs(title = "Regresión Polinomial", x = "Edad", y = "Valor Medio de Vivienda") +
          theme_bw()
      })
      
    } else if (input$model_type == "Árbol de Decisión") {
      # Modelo de árbol de decisión
      set.seed(1234)
      regresor_decisiontree <- rpart(Y ~ X, data = datos, control = rpart.control(minsplit = 2))
      
      output$summary_output <- renderPrint({
        summary(regresor_decisiontree)
      })
      
      output$plot <- renderPlot({
        rpart.plot(regresor_decisiontree, main = "Árbol de Decisión")
      })
      
    } else if (input$model_type == "Bootstrapping") {
      # Bootstrapping
      fun_coeficientes <- function(data, index) {
        return(coef(lm(Y ~ X, data = data, subset = index)))
      }
      
      set.seed(123)
      resultados_boot <- boot(data = datos, statistic = fun_coeficientes, R = 1000)
      
      output$summary_output <- renderPrint({
        print(resultados_boot)
      })
      
      output$plot <- renderPlot({
        plot(resultados_boot)
      })
    }
    
  })
}

# Ejecutar la aplicación Shiny
shinyApp(ui = ui, server = server)

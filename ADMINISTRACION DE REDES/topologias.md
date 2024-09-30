# Topologías de Redes

## Conexión

La conexión en una red puede ser establecida mediante diferentes medios, cada uno con sus propias características y aplicaciones.

### 1. Cableado

#### Par Trenzado
El par trenzado es uno de los medios de transmisión más comunes en redes locales. Consiste en pares de cables de cobre trenzados para reducir la interferencia electromagnética.

- **UTP (Unshielded Twisted Pair):** No tiene blindaje adicional, es más económico y ampliamente utilizado en redes Ethernet.
- **FTP (Foiled Twisted Pair):** Tiene un blindaje de aluminio que protege contra interferencias externas.
- **STP (Shielded Twisted Pair):** Incluye un apantallamiento adicional alrededor de cada par de cables para mayor protección contra interferencias.

**Limitación:** El par trenzado puede alcanzar una distancia máxima de hasta 90 metros sin necesidad de repetidores.

#### Coaxial
El cable coaxial está compuesto por un conductor central rodeado por un aislante, una malla metálica y una cubierta exterior. Es conocido por su robustez y capacidad para transmitir señales a largas distancias.

- **Topología Bus:** Utiliza un único cable coaxial que actúa como un bus compartido donde todos los dispositivos están conectados.

**Alcance:** El cable coaxial puede transmitir señales hasta 10,000 metros.

#### Fibra Óptica
La fibra óptica utiliza hilos de vidrio o plástico para transmitir datos como pulsos de luz, ofreciendo altas velocidades y grandes distancias.

- **Monomodo:** Utiliza una única longitud de onda de luz, ideal para largas distancias y altas velocidades.
- **Multimodo:** Utiliza múltiples longitudes de onda de luz, adecuado para distancias más cortas debido a la dispersión modal.

### 2. Inalámbrico

Las conexiones inalámbricas permiten la transmisión de datos sin cables físicos, utilizando diferentes tecnologías y medios.

- **WiFi (1-6):** Estándares de redes inalámbricas que varían en velocidad y alcance, desde 802.11a/b/g hasta 802.11ax.
- **Bluetooth:** Tecnología para la comunicación a corta distancia entre dispositivos electrónicos.
- **Infrarrojo:** Utiliza luz infrarroja para transmitir datos, generalmente en dispositivos de corto alcance.
- **Radiofrecuencia (RF):** Emplea ondas de radio para la transmisión de datos a diversas distancias.
- **Satelital:** Utiliza satélites para la comunicación, ideal para áreas remotas donde no hay infraestructura terrestre.
- **LiFi:** Tecnología de comunicación que utiliza luz visible para transmitir datos, ofreciendo alta velocidad y seguridad.

## Flujo de Datos

El flujo de datos en una red se gestiona a través de dispositivos que dirigen el tráfico de información entre los diferentes nodos.

### 1. Concentrador

El concentrador es un dispositivo de red que conecta múltiples dispositivos en una red, permitiendo que compartan datos y recursos.

- **HUB:** Dispositivo simple que transmite los datos recibidos a todos los puertos, sin gestionar el tráfico de manera inteligente.
- **Switch:** Dispositivo más avanzado que dirige los datos específicamente al dispositivo de destino, mejorando la eficiencia y reduciendo colisiones.

## Conceptos Importantes

> [!IMPORTANT]
> **¿Qué es el acuse de recibo (ACK)?**
> 
> El acuse de recibo (ACK) es una señal enviada por el receptor para confirmar que ha recibido correctamente un paquete de datos. Es fundamental en protocolos de comunicación para asegurar la entrega exitosa de la información.
>
> **¿Qué es el CoS (Clase de Servicio)?**
> 
> El CoS (Class of Service) es una técnica utilizada en redes para priorizar el tráfico de datos. Permite asignar diferentes niveles de prioridad a diferentes tipos de tráfico, garantizando que los datos críticos reciban un tratamiento preferencial.

## Temas para Estudiar

> [!Estudiar]
> **Métodos de Envío**
>
> - **Unicast:** Comunicación uno a uno entre un emisor y un receptor.
> - **Broadcast:** Comunicación uno a todos los dispositivos de la red.
> - **Multicast:** Comunicación uno a múltiples receptores seleccionados.
> - **Anycast:** Comunicación uno a cualquier receptor más cercano en un grupo de posibles receptores.

## Topologías de Red Comunes

- **Estrella:** Todos los dispositivos están conectados a un punto central, como un switch o un hub. Facilita la gestión y aislamiento de fallos.
- **Anillo:** Cada dispositivo está conectado al siguiente formando un circuito cerrado. La señal circula en una dirección, lo que puede simplificar la detección de fallos.
- **Bus:** Todos los dispositivos comparten un único medio de transmisión. Es fácil de implementar pero puede sufrir colisiones y limitaciones de rendimiento.
- **Malla:** Cada dispositivo está conectado a varios otros dispositivos, proporcionando múltiples rutas para la transmisión de datos. Ofrece alta redundancia y fiabilidad.
- **Árbol:** Estructura jerárquica que combina características de las topologías estrella y bus. Es escalable y fácil de gestionar.

## Consideraciones al Elegir una Topología

- **Escalabilidad:** Capacidad de la red para crecer sin pérdida significativa de rendimiento.
- **Costo:** Inversión necesaria para implementar y mantener la infraestructura de red.
- **Fiabilidad:** Resistencia de la red ante fallos de componentes o enlaces.
- **Facilidad de Administración:** Simplicidad para gestionar y solucionar problemas en la red.
- **Rendimiento:** Capacidad de la red para manejar el tráfico de datos requerido.


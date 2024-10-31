# Currency API

Esta es una API sencilla desarrollada con FastAPI para consultar el valor de venta de monedas extranjeras (USD y EUR) usando valores de una fuente de datos externa. Los valores se actualizan automáticamente cada 10 minutos para mantener la información actualizada.

## Requisitos

- Python 3.7 o superior
- FastAPI
- `aux` (Módulo externo para la obtención de valores de moneda)

## Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/JotaVeBass/apibna.git
   cd apibna
   
Instala las dependencias: Utiliza pip para instalar las librerías necesarias.
pip install fastapi uvicorn
Asegúrate de que también tengas instalado el módulo aux, que contiene la función get_currency_bna_value para obtener valores de cambio.

Configuración y uso
Estructura del proyecto:

Asegúrate de que la estructura del proyecto sea la siguiente:

bash
Copiar código
├── main.py             # Archivo principal de la API
└── aux.py              # Módulo auxiliar para obtener valores de moneda
Ejecuta la API: Inicia el servidor de desarrollo con uvicorn.

uvicorn main:app --reload
Uso de la API: La API tiene dos funcionalidades principales:

Actualizar valores automáticamente: Al iniciar, la API actualiza cada 10 minutos los valores de las monedas (dólar y euro) usando el módulo aux.

Consultar valor de venta de una moneda: Puedes consultar el valor actual de una moneda haciendo una solicitud GET a la ruta /currency/sale/{currency}, donde {currency} puede ser dolar o euro.

Ejemplo de uso:

ruby
GET http://127.0.0.1:8000/currency/sale/dolar
Respuesta:

json

{
   "currency": "dolar",
   "value": 100.50,
   "timestamp": "2024-10-31T12:00:00.000000"
}

Archivos y Estructura del Código

main.py: Archivo principal que contiene la configuración de la API y el ciclo de actualización de valores de moneda.
aux.py: Módulo auxiliar con la función get_currency_bna_value(currency: str) -> float, que debe devolver el valor de la moneda solicitada.

Logs
Se incluye configuración de logs para realizar un seguimiento de eventos importantes. Al actualizarse el valor de una moneda, los valores actuales se almacenan en la variable resultado_actual, con información sobre el tiempo de la última actualización (timestamp).

Contribución
Si quieres contribuir a este proyecto, haz un fork y crea un pull request con tus mejoras.

Licencia
Este proyecto está bajo la licencia MIT.





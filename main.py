from fastapi import FastAPI, HTTPException
import aux
import asyncio
import datetime
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


app = FastAPI(title="API CURRENCIES")

logger = logging.getLogger(__name__)

resultado_actual = {"valores": None, "timestamp": None}


async def consultar_periodicamente():
    global resultado_actual
    while True:
        nuevo_valor = {
            "dolar": aux.get_currency_bna_value("dolar"),
            "euro": aux.get_currency_bna_value("euro"),
        }

        resultado_actual = {
            "valores": nuevo_valor,
            "timestamp": datetime.datetime.now().isoformat(),
        }
        # logger.INFO("Valores Actualizados")
        await asyncio.sleep(600)


@app.on_event("startup")
async def iniciar_tarea_consulta():
    asyncio.create_task(consultar_periodicamente())


@app.get("/currency/sale/{currency}")
async def get_currency_sale(currency: str):
    global resultado_actual
    try:
        value = resultado_actual["valores"][currency.lower()]
        timestamp = resultado_actual["timestamp"]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Moneda {currency} no encontrada")
    return {"currency": currency, "value": value, "timestamp": timestamp}

import requests
from bs4 import BeautifulSoup

def get_currency_bna_value(currency_name):
    """Extracts the dollar or Euro value from the BNA website.

    Args:
        currency_name: 'Dólar' for the dollar value, 'Euro' for the Euro value. 

    Returns:
        float: The extracted value.

    Raises:
        ValueError: If there's a problem parsing the BNA website or if the currency is not found.
    """

    base_url = "https://www.bna.com.ar/Personas"
    
    page = requests.get(base_url)

    # Handle redirection, using the redirected URL for subsequent requests
    if page.url != base_url:
        base_url = page.url
    page = requests.get(base_url) 

    soup = BeautifulSoup(page.content, "html.parser")
    divisas_table = soup.find(id="divisas")
    billetes_table = soup.find(id="billetes")
    if not divisas_table or billetes_table:
        raise ValueError("No se puede encontrar la tabla de cotizaciones")

    all_tds_divisas = divisas_table.find_all("td", class_=False)
    all_tds_billetes = billetes_table.find_all("td", class_=False)

    # Dictionary to map currency name to index within tds
    currency_index = {'dolar': 1, 'euro': 3}

    try:
        index = currency_index[currency_name]
    except KeyError:
        raise ValueError(f"Moneda no soportada: {currency_name}")

    value_str_divisas = all_tds_divisas[index].text.strip().replace(',', '.')
    value_str_billetes = all_tds_billetes[index].text.strip().replace(',', '.')
    return float({
        "divisas": value_str_divisas,
        "billetes": value_str_billetes
        })

if __name__ == "__main__":
    dolar_bna = get_currency_bna_value('dolar')
    euro_bna = get_currency_bna_value('euro')

    print(f"Valor del dólar BNA: {dolar_bna}")
    print(f"Valor del Euro BNA: {euro_bna}")

from src.utils.inventory_api_client import InventoryAPIClient
from dotenv import load_dotenv
import os
load_dotenv()
from typing import List, Dict, Optional, Union
from datetime import datetime
import json  

def crear_venta(customer_name:str,items:List[Dict]):
    """  
        Crea una nueva venta.  
        
        Args:  
            customer_name: Nombre del cliente  
            items: Lista de items [{"product_id": int, "quantity": int}]  
            
        Returns:  
            Dict: Confirmación de la venta  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])

    print("###### DATOS DE LA VENTA A CREAR ###########")
    print(customer_name)
    print(items)
    print("###### DATOS DE LA VENTA A CREAR ###########")
    sale = client.create_sale(
        customer_name=customer_name,
        items=items
    )
    return sale

def consultar_venta(sale_id:int):
    """  
    Obtiene los detalles de una venta.  
    
    Args:  
        sale_id: ID de la venta  
        
    Returns:  
        Dict: Datos de la venta  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    sale = client.get_sale(sale_id)
    return sale

def obtener_reporte_ventas(start_date:str,end_date:str):
    """  
    Obtiene el reporte de ventas.  
    
    Args:  
        start_date: Fecha inicial (opcional)  
        end_date: Fecha final (opcional)  
        
    Returns:  
        List[Dict]: Lista de ventas  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    report = client.get_sales_report(
        start_date=start_date,
        end_date=end_date
    )
    return report
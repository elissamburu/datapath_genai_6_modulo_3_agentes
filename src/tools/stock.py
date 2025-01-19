from src.utils.inventory_api_client import InventoryAPIClient
from dotenv import load_dotenv
import os
load_dotenv()
from typing import List, Dict, Optional, Union
from datetime import datetime
import json  

def obtener_stock_alerts():
    """
        Obtiene las alertas de stock.  
    """
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    alerts = client.get_stock_alerts()
    return alerts

def obtener_producto_stock(product_id:int):
    """  
    Obtiene el stock actual de un producto.  
    
    Args:  
        product_id: ID del producto  
        
    Returns:  
        List[Dict]: Lista de registros de stock  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    stock = client.get_product_stock(product_id)
    return stock

def registrar_movimiento(product_id:int,movement_type:str,quantity:int,reference_type:str, reference_id: Optional[int] = None, notes: Optional[str] = None):
    """  
    Registra un movimiento de stock.  
    
    Args:  
        product_id: ID del producto  
        movement_type: Tipo de movimiento ('IN' o 'OUT')  
        quantity: Cantidad  
        reference_type: Tipo de referencia ('PURCHASE', 'SALE', 'ADJUSTMENT')  
        reference_id: ID de referencia opcional  
        notes: Notas opcionales  
        
    Returns:  
        Dict: Confirmación del movimiento  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    client.create_stock_movement(
        product_id=product_id,
        movement_type=movement_type,
        quantity=quantity,
        reference_type=reference_type
    )

def obtener_movimientos_stock(product_id: Optional[int] = None,  
                    start_date: Optional[str] = None,  
                    end_date: Optional[str] = None) -> List[Dict]:  
    """  
    Obtiene el historial de movimientos de stock.  
    
    Args:  
        product_id: ID del producto (opcional)  
        start_date: Fecha inicial (opcional)  
        end_date: Fecha final (opcional)  
        
    Returns:  
        List[Dict]: Lista de movimientos  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    movements = client.get_stock_movements(product_id=product_id)
    return movements

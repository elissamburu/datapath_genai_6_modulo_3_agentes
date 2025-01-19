from src.utils.inventory_api_client import InventoryAPIClient
from dotenv import load_dotenv
import os
load_dotenv()
from typing import List, Dict, Optional, Union
from datetime import datetime
import json  

def crear_produto(name:str,unit_price:float,min_stock:int,max_stock:int,description:str):
    """  
    Crea un nuevo producto.  
    
    Args:  
        name: Nombre del producto  
        unit_price: Precio unitario  
        min_stock: Stock mínimo  
        max_stock: Stock máximo  
        description: Descripción opcional  
        
    Returns:  
        Dict: Datos del producto creado  
    """  
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    product = client.create_product(
        name=name,
        description=description,
        unit_price=unit_price,
        min_stock=min_stock,
        max_stock=max_stock
    )
    return product

def actualizar_producto(product_id:int,**kwargs):
    """  
    Actualiza un producto existente.  
    
    Args:  
        product_id: ID del producto  
        **kwargs: Campos a actualizar (name, description, unit_price, min_stock, max_stock)  
        
    Returns:  
        Dict: Mensaje de confirmación  
    """
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    product = client.update_product(product_id, **kwargs)
    return product

def eliminar_producto(product_id:int):
    """  
    Elimina un producto existente.  
    
    Args:  
        product_id: ID del producto  
        
    Returns:  
        Dict: Mensaje de confirmación  
    """
    client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    product = client.delete_product(product_id)
    return product

def consultar_productos():
    """  
    Obtiene la lista de todos los productos.  
    
    Returns:  
        Lista de productos 
    """
    #client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
    #products = client.get_all_products()
    #json_data = json.dumps(products, indent=2)  
    #print(json_data)
    import requests
    url = "http://localhost:8001/products/"  
    try:  
        response = requests.get(url)  
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP  
        return response.json()  
    except requests.exceptions.RequestException as e:  
        print(f"Error al obtener productos: {e}")  
        return None  

def obtener_producto(product_id:int):
        """  
        Obtiene los detalles de un producto.  
        
        Args:  
            product_id: ID del producto  
            
        Returns:  
            Dict: Datos del producto  
        """  
        client = InventoryAPIClient(os.environ["INVENTORY_API_PATH"])
        product = client.get_product(product_id)
        return product

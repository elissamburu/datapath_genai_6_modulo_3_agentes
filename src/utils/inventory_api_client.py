import requests
from typing import List, Dict, Optional, Union

class InventoryAPIClient:
    def __init__(self, base_url: str = "http://localhost:8001"):  
        """  
        Inicializa el cliente de la API.  

        Args:  
            base_url (str): URL base de la API  
        """  
        self.base_url = base_url.rstrip('/')  
        self.session = requests.Session()  
        self.session.headers.update({  
            'Content-Type': 'application/json',  
            'Accept': 'application/json'  
        })  
        """
        Inicializa el cliente de la API.

        Args:  
            base_url (str): URL base de la API  
        """  
        # Inicialización explícita de todos los atributos  
        self.base_url = base_url.rstrip('/')  
        # Crear una nueva sesión de requests  
        self.session = requests.Session()  
        # Configurar headers por defecto  
        self.session.headers.update({  
            'Content-Type': 'application/json',  
            'Accept': 'application/json'  
        })  

    def _handle_response(self, response: requests.Response) -> Union[Dict, List]:  
        """  
        Maneja la respuesta de la API y procesa posibles errores.  
        """  
        try:  
            response.raise_for_status()  
            return response.json()  
        except requests.exceptions.HTTPError as e:  
            error_msg = f"Error HTTP: {e}"  
            try:  
                error_detail = response.json()  
                error_msg += f"\nDetalle: {error_detail}"  
            except:  
                pass  
            raise Exception(error_msg)  
        except Exception as e:  
            raise Exception(f"Error inesperado: {str(e)}")  
    
    # ============ Métodos para Productos ============  
    def create_product(self, name: str, unit_price: float, min_stock: int,   
                    max_stock: int, description: Optional[str] = None) -> Dict:  
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
        data = {  
            "name": name,  
            "unit_price": unit_price,  
            "min_stock": min_stock,  
            "max_stock": max_stock,  
            "description": description  
        }  
        response = self.session.post(f"{self.base_url}/products/", json=data)  
        return self._handle_response(response)  

    def get_product(self, product_id: int) -> Dict:  
        """  
        Obtiene los detalles de un producto.  
        
        Args:  
            product_id: ID del producto  
            
        Returns:  
            Dict: Datos del producto  
        """  
        response = self.session.get(f"{self.base_url}/products/{product_id}")  
        return self._handle_response(response)  

    def search_products(self, product_name: str) -> Dict:  
        """  
        Realiza una búsqueda de los productos por la descripción que envíes 
        
        Args:  
            product_name: Nombre o parte del nombre del producto.
            
        Returns:  
            list[Dict]: Datos de los producto  
        """  
        response = self.session.get(f"{self.base_url}/products/search/{product_name}")  
        return self._handle_response(response)  


    def get_all_products(self) -> List[Dict]:  
        """  
        Obtiene la lista de todos los productos.  
        
        Returns:  
            List[Dict]: Lista de productos  
        """  
        print(f"{self.base_url}/products/")
        response = self.session.get(f"{self.base_url}/products/")  
        return self._handle_response(response)  

    

    def update_product(self, product_id: int, **kwargs) -> Dict:  
        """  
        Actualiza un producto existente.  
        
        Args:  
            product_id: ID del producto  
            **kwargs: Campos a actualizar (name, description, unit_price, min_stock, max_stock)  
            
        Returns:  
            Dict: Mensaje de confirmación  
        """  
        response = self.session.put(f"{self.base_url}/products/{product_id}", json=kwargs)  
        return self._handle_response(response)  

    def delete_product(self, product_id: int) -> Dict:  
        """  
        Elimina un producto.  
        
        Args:  
            product_id: ID del producto  
            
        Returns:  
            Dict: Mensaje de confirmación  
        """  
        response = self.session.delete(f"{self.base_url}/products/{product_id}")  
        return self._handle_response(response)  

    # ============ Métodos para Stock ============  
    def get_product_stock(self, product_id: int) -> List[Dict]:  
        """  
        Obtiene el stock actual de un producto.  
        
        Args:  
            product_id: ID del producto  
            
        Returns:  
            List[Dict]: Lista de registros de stock  
        """  
        response = self.session.get(f"{self.base_url}/stock/{product_id}")  
        return self._handle_response(response)  

    def create_stock_movement(self, product_id: int, movement_type: str,   
                            quantity: int, reference_type: str,  
                            reference_id: Optional[int] = None,  
                            notes: Optional[str] = None) -> Dict:  
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
        data = {  
            "product_id": product_id,  
            "movement_type": movement_type,  
            "quantity": quantity,  
            "reference_type": reference_type,  
            "reference_id": reference_id,  
            "notes": notes  
        }  
        response = self.session.post(f"{self.base_url}/stock/movements/", json=data)  
        return self._handle_response(response)  

    def get_stock_movements(self, product_id: Optional[int] = None,  
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
        params = {  
            "product_id": product_id,  
            "start_date": start_date,  
            "end_date": end_date  
        }  
        params = {k: v for k, v in params.items() if v is not None}  
        response = self.session.get(f"{self.base_url}/stock/movements/", params=params)  
        return self._handle_response(response)  

    def get_stock_alerts(self) -> List[Dict]:  
        """  
        Obtiene las alertas de stock bajo.  
        
        Returns:  
            List[Dict]: Lista de alertas  
        """  
        response = self.session.get(f"{self.base_url}/stock/alerts/")  
        return self._handle_response(response)  

    # ============ Métodos para Ventas ============  
    def create_sale(self, customer_name: str, items: List[Dict]) -> Dict:  
        """  
        Crea una nueva venta.  
        
        Args:  
            customer_name: Nombre del cliente  
            items: Lista de items [{"product_id": int, "quantity": int}]  
            
        Returns:  
            Dict: Confirmación de la venta  
        """  
        data = {  
            "customer_name": customer_name,  
            "items": items  
        }  
        response = self.session.post(f"{self.base_url}/sales/", json=data)  
        return self._handle_response(response)  

    def get_sale(self, sale_id: int) -> Dict:  
        """  
        Obtiene los detalles de una venta.  
        
        Args:  
            sale_id: ID de la venta  
            
        Returns:  
            Dict: Datos de la venta  
        """  
        response = self.session.get(f"{self.base_url}/sales/{sale_id}")  
        return self._handle_response(response)  

    def get_sales_report(self, start_date: Optional[str] = None,  
                        end_date: Optional[str] = None) -> List[Dict]:  
        """  
        Obtiene el reporte de ventas.  
        
        Args:  
            start_date: Fecha inicial (opcional)  
            end_date: Fecha final (opcional)  
            
        Returns:  
            List[Dict]: Lista de ventas  
        """  
        params = {  
            "start_date": start_date,  
            "end_date": end_date  
        }  
        params = {k: v for k, v in params.items() if v is not None}  
        response = self.session.get(f"{self.base_url}/sales/", params=params)  
        return self._handle_response(response)  

"""
Skyscanner API Integration Service

This module provides integration with the Skyscanner Flight Search API.
It handles authentication, API calls, and response parsing.

Documentation: https://developers.skyscanner.net/
API Status: https://partners.api.skyscanner.net/apiservices/

IMPORTANT: This service requires a valid Skyscanner API key.
To obtain an API key, visit: https://developers.skyscanner.net/
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime
from ..models.flight import Flight


class SkyscannerAPIError(Exception):
    """Custom exception for Skyscanner API errors"""
    pass


class SkyscannerService:
    """
    Service for interacting with the Skyscanner Flight Search API.
    
    This service provides methods to search for flights using the Skyscanner API.
    It requires a valid API key to function.
    
    Configuration:
        Set the SKYSCANNER_API_KEY environment variable with your API key.
        Example: export SKYSCANNER_API_KEY="your_api_key_here"
    """
    
    # Skyscanner API endpoints
    BASE_URL = "https://partners.api.skyscanner.net/apiservices"
    BROWSE_ROUTES_ENDPOINT = "/browseroutes/v1.0"
    BROWSE_QUOTES_ENDPOINT = "/browsequotes/v1.0"
    
    # Default parameters
    DEFAULT_MARKET = "ES"  # Spain
    DEFAULT_CURRENCY = "EUR"
    DEFAULT_LOCALE = "es-ES"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Skyscanner service.
        
        Args:
            api_key: Skyscanner API key. If not provided, will attempt to read 
                     from SKYSCANNER_API_KEY environment variable.
        
        Raises:
            SkyscannerAPIError: If no API key is provided and none is found in environment.
        """
        self.api_key = api_key or os.getenv("SKYSCANNER_API_KEY")
        
        if not self.api_key:
            # API key is not available yet - this is expected during initial development
            self.api_key = None
            self._is_configured = False
        else:
            self._is_configured = True
    
    def is_configured(self) -> bool:
        """
        Check if the service is properly configured with an API key.
        
        Returns:
            bool: True if API key is configured, False otherwise.
        """
        return self._is_configured
    
    def search_flights(
        self,
        origin: str,
        destination: str,
        departure_date: str,
        return_date: Optional[str] = None,
        adults: int = 1,
        max_price: Optional[float] = None
    ) -> List[Flight]:
        """
        Search for flights using the Skyscanner API.
        
        This method uses the Browse Quotes API endpoint to find available flights.
        
        Args:
            origin: Origin airport code (IATA, e.g., "MAD")
            destination: Destination airport code (IATA, e.g., "BCN")
            departure_date: Departure date in YYYY-MM-DD format
            return_date: Optional return date in YYYY-MM-DD format
            adults: Number of adult passengers (default: 1)
            max_price: Optional maximum price filter
        
        Returns:
            List of Flight objects matching the search criteria.
        
        Raises:
            SkyscannerAPIError: If API key is not configured or API call fails.
        """
        if not self.is_configured():
            raise SkyscannerAPIError(
                "Skyscanner API key is not configured. "
                "Please set the SKYSCANNER_API_KEY environment variable."
            )
        
        # Construct the API URL
        outbound_date = departure_date
        inbound_date = return_date if return_date else ""
        
        url = (
            f"{self.BASE_URL}{self.BROWSE_QUOTES_ENDPOINT}/"
            f"{self.DEFAULT_MARKET}/{self.DEFAULT_CURRENCY}/{self.DEFAULT_LOCALE}/"
            f"{origin}/{destination}/{outbound_date}"
        )
        
        if inbound_date:
            url += f"/{inbound_date}"
        
        # Add API key to headers
        headers = {
            "Accept": "application/json",
            "x-api-key": self.api_key
        }
        
        # Make the API request
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Parse the response and convert to Flight objects
            flights = self._parse_skyscanner_response(data, origin, destination)
            
            # Filter by max price if specified
            if max_price:
                flights = [f for f in flights if f.price <= max_price]
            
            # Sort by price
            flights.sort(key=lambda x: x.price)
            
            return flights
            
        except requests.exceptions.RequestException as e:
            raise SkyscannerAPIError(f"Failed to fetch flights from Skyscanner: {str(e)}")
    
    def _parse_skyscanner_response(
        self, 
        data: Dict, 
        origin: str, 
        destination: str
    ) -> List[Flight]:
        """
        Parse Skyscanner API response and convert to Flight objects.
        
        Args:
            data: JSON response from Skyscanner API
            origin: Origin airport code
            destination: Destination airport code
        
        Returns:
            List of Flight objects
        """
        flights = []
        
        # Parse quotes from the response
        quotes = data.get("Quotes", [])
        carriers = {c["CarrierId"]: c["Name"] for c in data.get("Carriers", [])}
        
        for quote in quotes:
            # Extract flight information
            price = quote.get("MinPrice", 0)
            direct = quote.get("Direct", False)
            
            # Get outbound leg information
            outbound_leg = quote.get("OutboundLeg", {})
            departure_date = outbound_leg.get("DepartureDate", "")
            carrier_ids = outbound_leg.get("CarrierIds", [])
            
            # Get airline name
            airline = carriers.get(carrier_ids[0], "Unknown") if carrier_ids else "Unknown"
            
            # Parse dates
            try:
                dep_datetime = datetime.fromisoformat(departure_date.replace("Z", "+00:00"))
            except (ValueError, AttributeError):
                continue
            
            # Create Flight object
            # Note: Skyscanner quotes don't include exact arrival times or durations
            # For full details, would need to use the full search API
            flight = Flight(
                id=f"SKY{quote.get('QuoteId', 0)}",
                origin=origin,
                destination=destination,
                departure_date=dep_datetime,
                arrival_date=dep_datetime,  # Would need full API for accurate arrival
                price=price,
                airline=airline,
                duration_minutes=0,  # Would need full API for duration
                available_seats=None
            )
            
            flights.append(flight)
        
        return flights
    
    def get_route_info(
        self,
        origin: str,
        destination: str,
        departure_date: str
    ) -> Dict:
        """
        Get route information using the Browse Routes API.
        
        This endpoint provides aggregated pricing and route information.
        
        Args:
            origin: Origin airport code (IATA)
            destination: Destination airport code (IATA)
            departure_date: Departure date in YYYY-MM-DD format
        
        Returns:
            Dictionary with route information and pricing
        
        Raises:
            SkyscannerAPIError: If API key is not configured or API call fails.
        """
        if not self.is_configured():
            raise SkyscannerAPIError(
                "Skyscanner API key is not configured. "
                "Please set the SKYSCANNER_API_KEY environment variable."
            )
        
        url = (
            f"{self.BASE_URL}{self.BROWSE_ROUTES_ENDPOINT}/"
            f"{self.DEFAULT_MARKET}/{self.DEFAULT_CURRENCY}/{self.DEFAULT_LOCALE}/"
            f"{origin}/{destination}/{departure_date}"
        )
        
        headers = {
            "Accept": "application/json",
            "x-api-key": self.api_key
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise SkyscannerAPIError(f"Failed to fetch route info from Skyscanner: {str(e)}")


# Factory function to create a SkyscannerService instance
def get_skyscanner_service() -> SkyscannerService:
    """
    Factory function to create and return a SkyscannerService instance.
    
    Returns:
        Configured SkyscannerService instance
    """
    return SkyscannerService()

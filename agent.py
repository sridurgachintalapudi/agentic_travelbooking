import requests
from bs4 import BeautifulSoup

def search_flights(destination):
    url = f"https://www.example.com/flights-to-{destination}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    flights = []
    for flight in soup.find_all('div', class_='flight-info'):
        flight_details = {
            'airline': flight.find('span', class_='airline-name').text,
            'price': flight.find('span', class_='price').text,
            'departure': flight.find('span', class_='departure-time').text,
            'arrival': flight.find('span', class_='arrival-time').text
        }
        flights.append(flight_details)
    
    return flights

def plan_travel(destination):
    flights = search_flights(destination)
    print(f"Found {len(flights)} flights to {destination}:")
    for flight in flights:
        print(f"Airline: {flight['airline']}, Price: {flight['price']}, Departure: {flight['departure']}, Arrival: {flight['arrival']}")

if __name__ == "__main__":
    destination = input("Enter your travel destination: ")
    plan_travel(destination)
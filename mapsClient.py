import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyD7SYo_K1nRimkiAbYFCpjFp5-npqINDVw')
now = datetime.now()
origen = 'Avenida Coyoacan 739 Casa 1, Benito Juarez, Del Valle, 03100 Ciudad de México'
destino = 'Bosque de Chapultepec I Secc, 11100 Ciudad de México, CDMX'
direccion = gmaps.directions(origen,destino,mode = 'driving', departure_time=now)

print(direccion)

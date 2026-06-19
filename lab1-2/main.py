import requests

def get_weather():
    # Coordonatele sunt pentru București
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.4323&longitude=26.1063&current_weather=true"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Verifică dacă cererea a avut succes
        
        data = response.json()
        temp = data['current_weather']['temperature']
        
        print(f"Temperatura curentă este: {temp}°C")
        
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea datelor: {e}")

if __name__ == "__main__":
    get_weather()
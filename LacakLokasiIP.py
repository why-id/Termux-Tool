import requests
from opencage.geocoder import OpenCageGeocode

def get_location_from_ip(ip):
    # Menggunakan layanan ipinfo.io untuk mendapatkan lokasi dari IP publik
    response = requests.get(f'https://ipinfo.io/{ip}/json')
    if response.status_code == 200:
        data = response.json()
        location = data.get('loc')
        if location:
            lat, lng = map(float, location.split(','))
            return lat, lng
    return None, None

def get_location_details_from_opencage(lat, lng, api_key):
    geocoder = OpenCageGeocode(api_key)
    result = geocoder.reverse_geocode(lat, lng)
    if result and len(result):
        return result[0]['formatted'], lat, lng
    return None, None, None

def main():
    opencage_key = "your_opencage_key"  # Ganti dengan API Key OpenCage Anda

    # Mendapatkan input alamat IP dari pengguna
    ip = input("Masukkan alamat IP: ")
    
    # Mendapatkan lokasi berdasarkan IP publik
    lat, lng = get_location_from_ip(ip)
    if lat and lng:
        print(f"Lokasi dari IP: Latitude={lat}, Longitude={lng}")

        # Mendapatkan detail lokasi dari OpenCage
        lokasi, lat, lng = get_location_details_from_opencage(lat, lng, opencage_key)
        if lokasi:
            print(f"Detail Lokasi: {lokasi}")
            google_maps_url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
            print("URL Google Maps:", google_maps_url)
        else:
            print("Gagal mendapatkan detail lokasi dari OpenCage.")
    else:
        print("Gagal mendapatkan lokasi dari IP.")

if __name__ == "__main__":
    main()

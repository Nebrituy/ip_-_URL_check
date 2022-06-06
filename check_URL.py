import requests
import folium
import socket


def get_info_by_ip(ip='46.182.80.11'):
  try:
    response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
    # print(response)
        
    data = {
      '[IP]': response.get('query'),
      '[Провайдер]': response.get('isp'),
      '[Организация]': response.get('org'),
      '[Страна]': response.get('country'),
      '[Регион]': response.get('regionName'),
      '[Город]': response.get('city'),
      '[ZIP]': response.get('zip'),
      '[Lat]': response.get('lat'),
      '[Lon]': response.get('lon'),
    }
        
    for k, v in data.items():
      print(f'{k} : {v}')
      
    latitude = response.get('lat')
    longitude = response.get('lon')
    print(f'https://maps.google.com/maps?q={latitude},{longitude}')
    
    print_map = 'n'
    # print_map = input('Создать HTML-файл с картой? (Yes/No)')
    if print_map.lower() == 'yes' or print_map.lower() == 'y':
      area = folium.Map(location=[response.get('lat'), response.get('lon')])
    else:
      return

    
    
    # print(f'https://maps.google.com?saddr=Current+Location&daddr={latitude},{longitude}')
    # print(f'https://maps.google.com?daddr={latitude},{longitude}')
    
    area.save(f'{response.get("query")}_{response.get("city")}.html')
        
  except requests.exceptions.ConnectionError:
    print('[!] Please check your connection!')

def get_ip_by_hostname():
  hostname = input('Введите URL сайта: ').strip("http://").strip("https://").strip("www.")
  if hostname.find('/') != -1:
    hostname = hostname[:hostname.find('/')]


  try:
    get_info_by_ip(socket.gethostbyname(hostname))
    # return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
  except socket.gaierror as error:
    return f'Invalid Hostname - {error}'



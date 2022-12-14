import requests
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }
        for b, v in data.items():
            print(f'{b} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f"{response.get('query')}_{response.get('city')}.html")
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    ip = input('Please enter a target IP:')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()

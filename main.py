# coding=utf-8
import csv
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()



def get_html():
    headers = {
        'authority': 'www.instagram.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'x-ig-www-claim':
            'hmac.AR2wqeeSx8xfBahf0bdSSKN65F7lAOxNmtMLRXgwQZoKpi7F',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',
        'x-csrftoken': 'gkvamdzzSnA6rffgXwFwUfnzfQLBhvmT',
        'x-ig-app-id': '936619743392459',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/alexed34/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'ig_did=A0599024-31F0-4D29-9A96-253A017E071C; '
                  'mid=XrObdQALAAEFrmHRXvdpfyO5H1v3; '
                  'fbm_124024574287414=base_domain=.instagram.com; '
                  'datr=HJiBX9mjqrRm9LGkt9WMj-y4; ig_nrcb=1; shbid=12457; '
                  'shbts=1609592151.3214407; rur=VLL; '
                  'csrftoken=gkvamdzzSnA6rffgXwFwUfnzfQLBhvmT; '
                  'ds_user_id=2728140171; '
                  'sessionid=2728140171%3A5Q2MXWUXfVbxwp%3A10; '
                  'fbsr_124024574287414=8REyYVEIL09cBWDHbLpJXeAaIx1d_zPjH2KCXZA_HmY.eyJ1c2VyX2lkIjoiMTAwMDA2NTYzNDE4MzgwIiwiY29kZSI6IkFRRDFUYVVvTmcwVVVNSjRRazItWVdOd0xHV0k2S2piOTZKbW45bGFtNC1JVDN4TmpONFk1TTZuVTVMZ1Qxb2hQNmluQlg4ZkNkZkk5bm13dTF2V252N3EwWEpQaUJOWTAxOW1OYXlaTGxYbTZHVU9qWWNGVzRnZHNaTzRFTTBSZ0lBOXFYbVpmUVd3VDhnY0ppeGpSeEY1MnU4eXVZaGdTWTFFNTctc2VSX2pPWTRzemFmTFJlTFV0UE51SGFUZy03ajBmVUM2dlpDakdiSmNxVUo3NnFZcUx5T0dEX3N1OXlZYWc2MkxDNTdMc3Bjc050bkNEaEpNU0JhUGI4RjF3QXZQUFQzX252RHdZbEtqaF8tZE55TlVXOTVrSXZONXY5NEZnc28zR3JhcjR4bnFQRllzZ1FRY1J2UDFhc2pzTkJmaGdkSGg5ektmWUlLZk5OT25pWjZLIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdGRlhIV3MyYlpDSGhaQmh0cGxzVG9sYlZieFl1M3h4MDRqbUhJUHVTQjdvM2JjeFhZOEd0WkFaQWZ3V2MxRUFPUDM0cjUxbzdZMjd4VXU1dXhQNW1LU1pDbXB6NGd2TU84Z09mU1JudXZaQ0pSaHhGTHFTcGxWY0VaQk1aQVhrTjlKc1pDSnhmalQ0QjlzdzlIVTRwTWNCa2MxUG1mTHRXWHhxdThidmhVQUUiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYwOTYxNzA5N30; urlgen="{\\"93.81.213.43\\": 3216}:1kvmw6:Re7ZbvcHbO5Jvy9OklEWqaiz1_c"',
    }

    params = (
        ('query_hash', '003056d32c2554def87228bc3fd9668a'),
        ('variables',
         '{"id":"2728140171","first":12,'
         '"after":"QVFCb2tuOW44cW92Q0VOanVsRjRWYWMzcmZKOFFRRWJESVBZazNycE4zdGVLckczOWlXR3FsNTl1TUE2QnVmR29pU29HdlFiTzV4cGhTUmVPVUd4T0hraw=="}'),
    )

    response = requests.get('https://www.instagram.com/millstream_wines/',
                            headers=headers, params=params).text
    result = response.split('window._sharedData =')
    result = result[1].split(';</script>')[0]
    result = json.loads(result)
    json_data = result['entry_data']['ProfilePage'][0]['graphql']['user'][
        'edge_owner_to_timeline_media']['edges']
    return json_data


def get_post(url):
    headers = {
        'authority': 'www.instagram.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'x-ig-www-claim':
            'hmac.AR2wqeeSx8xfBahf0bdSSKN65F7lAOxNmtMLRXgwQZoKprs4',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.141 Safari/537.36',
        'x-csrftoken': 'gkvamdzzSnA6rffgXwFwUfnzfQLBhvmT',
        'x-ig-app-id': '936619743392459',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': url,
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'ig_did=A0599024-31F0-4D29-9A96-253A017E071C; '
                  'mid=XrObdQALAAEFrmHRXvdpfyO5H1v3; '
                  'fbm_124024574287414=base_domain=.instagram.com; '
                  'datr=HJiBX9mjqrRm9LGkt9WMj-y4; ig_nrcb=1; shbid=12457; '
                  'csrftoken=gkvamdzzSnA6rffgXwFwUfnzfQLBhvmT; '
                  'ds_user_id=2728140171; '
                  'sessionid=2728140171%3A5Q2MXWUXfVbxwp%3A10; '
                  'shbts=1610122993.329948; rur=VLL; '
                  'fbsr_124024574287414=VX9Vay0RLsl3QRhmz6pf_dfsJ62PHoYB5bgQiqiLmas.eyJ1c2VyX2lkIjoiMTAwMDA2NTYzNDE4MzgwIiwiY29kZSI6IkFRQUkyWWJpM19vUndDQm04YjFaUUJ5RXM1N3RvZmQ2bXBkZWxlQ2Fhbll6bGZPak1FMXU4Ul9xeDZXbDZOQTNxRnVPRHJMTC1PSDZJazlPb2xqelpOWF81VE9tY0EzVGRTWHJvOFRLXzM3NkxlLTBGYlZ4eHZvdFJPVjNSVkZEQng4SDdLV1dMalNHandZUDRSME5oUHpVUjBQam14QktqZ1NQNVo5cFVpN25wRTQyeVJYOWpJUk92Rk44OFhJV01PdmFERnFtSzlHb1lpQkpZdmg2c0hlQ3hVbldQc0w1VUZNY0UxeHRaX0xlazZKMnBxU0FoOW1qV0pXX3EyOVpaNTd6cnJLcTNSOTh2b1dETGNzX0NOM0tHd2JvUlQwQTk5UnFBeWIxWko4V2hlNTFLSXZkX1h1VjdwSlpEMURRQVoyNnZTX0d6OEN2aG80Ui0tRHJIOS10Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU03RmxEZVNmUUJwZ2NOZHBvSEJDeEpWdllOcHZFT09aQ1NjN00wYm9qM2dRQVRTcGdEeTEyVEZRM05xSXNQc29TdEJmN0xOY0syUERETGU4clRxc1pBQjJ6Um1YaU1RZGtoMXhRQ2FnaHlJaXJVU1hxWkFUQjNaQjYxbVlyc2VscmZNbEJLYUlyVm16Rm5jbU5mZ0VIcWd6VldRSDA1QmRYSDZaQW5kciIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjEwMTIzMDEzfQ; urlgen="{\\"93.81.213.43\\": 3216}:1kxua7:g0Ggzv3RD6hJZQLPXP_81qSCVm8"',
    }

    params = (
        ('query_hash', '003056d32c2554def87228bc3fd9668a'),
        ('variables', '{"id":"6037799274","first":12}'),
    )

    response = requests.get('https://www.instagram.com/graphql/query/',
                            headers=headers, params=params)
    response.encoding = 'utf8'
    return response.json()


def write_csv(text, filename):
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([text])


def write_img(url, filename):
    filename = f'photo/{filename}.jpg'
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)


def get_shortcodes_site(text):
    shortcodes = []
    for i in text:
        shortcode = i['node']['shortcode']
        shortcodes.append(shortcode)
    return shortcodes


def open_links():
    data = []
    with open('link.csv', 'r') as file:
        reader = file.readlines()
        for i in reader:
            if i:
                data.append(i.strip())
    return data


def get_texts_and_imgs(text):
    json_posts = text['data']['user']['edge_owner_to_timeline_media']['edges']
    links = open_links()
    for i in json_posts:
        shortcode = i['node']['shortcode']
        if shortcode not in links:
            write_csv(shortcode, 'link.csv')
            image_url = i['node']['display_url']

            write_img(image_url, shortcode)
            text = i['node']['edge_media_to_caption']['edges'][0]['node'][
                'text']
            text = text.replace('??', '')
            text = text.replace('?', '')
            text = text.replace('\n\n', '\n')
            filename = f'texts/{shortcode}'
            write_csv(text, filename)
            # print('image_url', image_url)
            # print('text', text)
            print(shortcode)


def send_photo_server(photo, ACCESS_TOKEN):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {'group_id': 201491375, 'access_token': ACCESS_TOKEN,
              'v': '5.126'}

    response = requests.get(url, params=params).json()
    link = response['response']['upload_url']

    with open(photo, 'rb') as file:
        files = {'photo': file}

        response = requests.post(link, files=files)
        response.raise_for_status()
    return response.json()


def save_wall_photo(response_json, ACCESS_TOKEN):
    server = response_json['server']
    hash = response_json['hash']
    photo = response_json['photo']
    access_token = ACCESS_TOKEN
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {'group_id': 201491375, 'server': server, 'hash': hash,
              'photo': photo, 'access_token': access_token, 'v': '5.126'}
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()


def publish_post(shortcode, response_wall_photo, ACCESS_TOKEN):
    access_token = ACCESS_TOKEN
    owner_id = response_wall_photo['response'][0]['owner_id']
    media_id = response_wall_photo['response'][0]['id']
    attachments = f'photo{owner_id}_{media_id}'
    with open(f'texts/{shortcode}', 'r', encoding='utf-8') as file:
        reader = file.read()
        url = 'https://api.vk.com/method/wall.post'
        params = {'owner_id': -201491375, 'from_group': 1,
                  'attachments': attachments,
                  'message': reader,
                  'access_token': access_token, 'v': '5.126'}
    response = requests.post(url, params=params)
    response.raise_for_status()


def delete_file(shortcode):
    os.remove(f'texts/{shortcode}')
    os.remove(f'photo/{shortcode}.jpg')


def main():
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    shortcodes_site = get_shortcodes_site(get_html())
    url_last_post = f'https://www.instagram.com/p/{shortcodes_site[0]}/'
    last_post = get_post(url_last_post)
    get_texts_and_imgs(last_post)
    shortcodes = os.listdir('texts')
    for shortcode in shortcodes[:3]:
        try:
            photo = f'photo/{shortcode}.jpg'
            response_wall_photo = save_wall_photo(
                send_photo_server(photo, ACCESS_TOKEN), ACCESS_TOKEN)
            publish_post(shortcode, response_wall_photo, ACCESS_TOKEN)
        except requests.exceptions.HTTPError as err:

            print('error')
            print(shortcode)
        finally:
            delete_file(shortcode)
            print('finish')


if __name__ == '__main__':
    main()

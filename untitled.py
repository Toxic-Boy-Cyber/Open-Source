import requests

cookies = {
    'datr': 'FAjFY7f5D8XKH6qfzLSMExgS',
    'sb': 'FAjFY0TuEsFlt8DLr920m9_F',
    'locale': 'en_GB',
    'vpd': 'v1%3B704x360x2',
    'wd': '980x1829',
    'dpr': '2',
    'fr': '0mdvmQpwWVUFshZry..BjxQgU.GY.AAA.0.0.Bjy2QF.AWV64LnnB28',
}

          header_freefb = {'authority': 'www.facebook.com',
           'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'GET',
            'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
    'referer': 'https://mbasic.facebook.com/',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="110", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5378.192 Safari/537.36 Edg/106.0.1395.44',
    'viewport-width': '980',
}

params = {
    'login_attempt': '1',
}

data = {
    'email': '',
    'cuid': '',
    'guid': 'f7d9eba51efec8',
    'lgnjs': '1674273564',
    'lgnrnd': '195909_PtQN',
    'locale': 'en_GB',
    'login_source': 'comet_login_header',
    'next': 'https://www.facebook.com/Web.com/',
    'skstamp': '',
    'timezone': '-360',
    'lsd': 'AVq9-FNO2Ws',
    'jazoest': '2845',
    'lgndim': 'eyJ3IjozNjAsImgiOjgwMCwiYXciOjM2MCwiYWgiOjgwMCwiYyI6MjR9',
    'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'prefill_contact_point': '',
    'prefill_source': '',
    'encpass': '#PWD_BROWSER:5:1674273576:AedQAGZm7asYXtGh+UL6gHHD1PS1vygFSiYqQnnlGBokP5MndGCv5IULj3+DQj+XX4HxKsVYmZ7bVwLh9UkAd9O3TpbOYjMpB6dy0nF1nsUedcxL7RAhQZ7lVD4MXxJBfGGJzw==',
}

response = requests.post(
    'https://www.facebook.com/login/device-based/regular/login/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)



#mx_________



header_freefb = {
		    'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,}
            
            
            
            
          #  tox________
          
          header_freefb = {'authority': 'mbasic.facebook.com',
			'upgrade-insecure-requests': '1',
			'viewport-width': '980',
			'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'manifest',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.81 Mobile SFB/15.0.0034.21 Safari/537.36'
			    
			}
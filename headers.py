import requests

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'dnt': '1',
    'origin': 'https://weverse.io',
    'priority': 'u=1, i',
    'referer': 'https://weverse.io/',
    'sec-ch-ua': '"Whale";v="3", "Not-A.Brand";v="8", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Whale/3.26.244.21 Safari/537.36',
}

response = requests.get(
    'https://aegis-naver.pstatic.net/weverse/read/v2/VOD_DRM/weverse_2024_05_28_0/cenc/b6717346-1cc8-11ef-ad27-a0369fffb848/stream.mpd',
    headers=headers,
)

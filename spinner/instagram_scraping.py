import requests
import random



def post_info(code):
    url = 'https://www.instagram.com/p/%s/?__a=1' % code
    req_session = requests.Session()
    request_respond = req_session.get(url).json()['graphql']['shortcode_media']
    return {
        'text': request_respond['edge_media_to_caption']['edges'][0]['node']['text'],
        'id': request_respond['owner']['id'],
        'username': request_respond['owner']['username'],
        'screen_name': request_respond['owner']['full_name'],
        'profile_pic_url': request_respond['owner']['profile_pic_url'],
    }


def comments_fetching(code):
    data = []
    query_hash = 'f0986789a5c5d17c2400faebf16efd0d'
    shortcode = code
    first = 20
    after = None
    has_next_page = True

    while has_next_page:
        var = (
            query_hash,
            shortcode,
            first,
            ', "after":"%s"' % after if after else ''
        )
        url = 'https://www.instagram.com/graphql/query/?query_hash=%s&variables={"shortcode":"%s","first":%d%s}' % var
        req_session = requests.Session()
        request_respond = req_session.get(url).json()['data']['shortcode_media']['edge_media_to_comment']
        page_info = request_respond['page_info']
        data.extend(request_respond['edges'])
        after = page_info['end_cursor']
        has_next_page = page_info['has_next_page']
    return data

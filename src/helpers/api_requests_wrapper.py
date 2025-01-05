import json
import requests

def get_request(url,auth,in_json):
    get_response = requests.get(url = url, auth = auth)
    if in_json:                      #same as if in_json == True:
        return get_response.json()
    return get_response

def post_request(url,auth,headers,payload,in_json):
    post_response = requests.post(url=url,auth=auth,headers=headers, data =json.dumps(payload))
    if in_json:
        return post_response.json()
    return post_response

def patch_request(url,auth,headers,payload,in_json):
    patch_response = requests.patch(url=url,auth=auth,headers=headers, data =json.dumps(payload))
    if in_json:
        return patch_response.json()
    return patch_response

def put_request(url,auth,headers,payload,in_json):
    put_response = requests.put(url=url,auth=auth,headers=headers, data =json.dumps(payload))
    if in_json:
        return put_response.json()
    return put_response

def del_request(url,auth,headers,in_json):
    del_response = requests.delete(url=url,auth=auth,headers=headers)
    if in_json:
        return del_response.json()
    return del_response
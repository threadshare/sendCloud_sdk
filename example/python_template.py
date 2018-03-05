#coding:utf-8                                                                   

import requests, json                                                                

url = "http://sendcloud.sohu.com/webapi/mail.send_template.json"                         

API_USER = 'zhichaozhang_tesxxx'
API_KEY = 'LJB2mqIGvht2FzHo'

sub_vars = {
    'to': ['to1@domain.com', 'to2@domain.com'],
    'sub': {
        '%name%': ['user1', 'user2'],
        '%money%': ['1000', '2000'],
    }
}

params = {
    "api_user": API_USER,
    "api_key" : API_KEY,                                             
    "template_invoke_name" : "test_template",
    "substitution_vars" : json.dumps(sub_vars),
    "from" : "sendcloud@sendcloud.org",
    "fromname" : "SendCloud",
    "subject" : "SendCloud python template",
    "resp_email_id": "true",
}

filename = "..."
display_filename = "..."

files = { "file1" : (display_filename, open(filename,"rb"))}

r = requests.post(url, files=files, data=params)

print(r.text)


from requests_html import HTMLSession,HTML
from flask import Flask,request,jsonify
from flask_cors import *
app = Flask(__name__)
import json
CORS(app,supports_credentials=True)

@app.route('/')
def hello():
    print(request.args.get('category'))
    return 'welcome to my watchlist'

@app.route('/info')
def category_info():
    param_info = request.args.get('category')
    session = HTMLSession()
    try:
        res = session.get('https://avmoo.casa/cn/search/' + param_info)
        title = res.html.find('.photo-frame> img', first=True).attrs['title']
        detail_info = res.html.find('.photo-frame> img', first=True).attrs
        return jsonify({
            'status': 200,
            'message': 'success',
            'data': {
                'detail_info':detail_info
            }
        })
    except:
        return jsonify({
            'status': 500,
            'message': 'error'

        })

    return title


@app.route('/magnet/info')
def download_info():
    category = request.args.get('category')
    session = HTMLSession()
    response = session.get('https://sukebei.nyaa.si/?f=0&c=0_0&q=apns-079')
    element_list_tr = response.html.find('.default')
    print(element_list_tr)






#
# session = HTMLSession()
# res = session.get('https://avmoo.casa/cn/search/apns-053')
# print(res.html.find('.photo-frame> img',first=True).attrs)
# title = res.html.find('.photo-frame> img',first=True).attrs['title']
# print(title)


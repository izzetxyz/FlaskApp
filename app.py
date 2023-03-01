from flask import Flask, jsonify, request
from demo_selenium import bytedance,write_Verification,checkMail_Confirmations,getcookies,send_SMS,post_SMS
from concurrent.futures import ThreadPoolExecutor
import json
app = Flask(__name__)

executor = ThreadPoolExecutor(max_workers=10)

def bytedance_async(id, password, token,cflb,cfruid,cfbm):
    # bytedance fonksiyonunu asenkron olarak çağırmak için bir yardımcı fonksiyon.
    # bu fonksiyon, bytedance fonksiyonunu ThreadPoolExecutor havuzunda çalıştırır.
    result = bytedance(id, password, token,cflb,cfruid,cfbm)
    return result

@app.route('/api/checkUsernamePassword' , methods=['POST'])
def get_balance():
    data = request.json
    id = request.args.get('id')
    password = request.args.get('password')
    future = executor.submit(bytedance_async, id, password , data.get('token'), data.get('__cflb'), data.get('__cfruid'), data.get('__cf_bm'))
    cookies  = future.result()
    return jsonify(cookies)
@app.route('/api/getCookies', methods=['GET'])
def get_cookies():
    future = executor.submit(getcookies)
    cookies  = future.result()
    return jsonify(cookies)
@app.route('/api/sendSMS', methods=['POST'])
def get_sms():
    data = request.json
    future = executor.submit(send_SMS, data.get('__cflb'), data.get('__cfruid'),data.get('__cf_bm'),data.get('accesstoken'))
    result = future.result()
    return jsonify(result)
@app.route('/api/postsendSMS', methods=['POST'])
def get_smsPost():
    data = request.json
    future = executor.submit(post_SMS, data.get('__cflb'), data.get('__cfruid'),data.get('__cf_bm'),data.get('accesstoken'),data.get('code'))
    result = future.result()
    return jsonify(result)
@app.route('/api/getCode', methods=['POST'])
def get_code():
    data = request.json
    future = executor.submit(write_Verification, data.get('__cflb'), data.get('__cfruid'),data.get('__cf_bm'),data.get('accesstoken'),data.get('code'))
    result = future.result()
    return jsonify(result)
@app.route('/api/checkMailConfirmation', methods=['POST'])
def mail_confirmation():
    data = request.json
    future = executor.submit(checkMail_Confirmations, data.get('__cflb'), data.get('__cfruid'),data.get('__cf_bm'),data.get('accesstoken'))
    result = future.result()
    return jsonify(result)
if __name__ == '__main__':
    app.run(port=8000)
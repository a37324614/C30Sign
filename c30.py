import requests
import datetime

url_token = 'http://studentservice.iclass30.com/base/baselogin/login'
requests.packages.urllib3.disable_warnings()

params0 = {
    'account': '',  # 账号
    'logintype': '21',
    'passWord': '',  # 密码
    'userType': '2',
    'isCheckProduct': '0',
    'noticeDeviceId': '',  # 设备id
    'terminalType': 'app_student',
    'serviceVersion': '11.0',
    'schoolId': ''
}



def get_token():
    r = requests.get(url=url_token, params=params0, timeout=500, verify=False)
    token = r.json()['data']['token']
    return token


url_reg = 'https://px.iclass30.com/gatewayApi/subject/internshipStu/saveTodaySign'


def is_mora():
    now = datetime.datetime.now()
    if now.hour >= 12:
        return 1
    else:
        return 0


headers1 = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Mobile/15E148',
    'Authorization': 'null',
    'Accept': 'application/json,text/plain,*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-encoding': 'gzip,deflate,br',
    'X-Requested-Width': 'XMLHttpRequest',
    'Sec-Fetch-Mode': 'cors',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'token': get_token()
}


def get_register():
    qd = {
        'signData': 'point:[**,**]',#经纬度,
        'signType': is_mora(),  # 0和1代表签到签退
        'address': '',  # 打卡地址
        'signDay': '',  # 目前看来是空格不填
        'planId': '',  # 实习id 固定获取一次 写死
    }
    r = requests.post(url=url_reg, json=qd, headers=headers1, timeout=5000, verify=False)
    print(r.text)

if __name__ == '__main__':
    get_register()
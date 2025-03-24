import requests


def test(url):
    try:
        rsp = requests.get(url)
        if rsp.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False

if __name__ == '__main__':
    success_list = []
    fail_list = []
    for i in range(1,48):
        url = f'http://bd{i}.jinzhuedu.org'
        if test(url):
            success_list.append(i)
        else:
            fail_list.append(i)
    print(f'成功列表:{success_list}')
    print(f'失败列表:{fail_list}')

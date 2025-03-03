import requests
import base64

def url_to_base64(image_url):
    # 从URL下载图片并获取二进制数据
    response = requests.get(image_url)
    response.raise_for_status()  # 检查请求是否成功
    binary_data = response.content
    
    # 转换为Base64编码字符串（不带MIME前缀）
    base64_str = base64.b64encode(binary_data).decode('utf-8')
    return base64_str


import requests
import csv
import base64
import datetime

# FOFA API的基础URL
BASE_URL = "https://fofa.info/api/v1/search/all"

# FOFA email和key，需要替换成自己的
FOFA_EMAIL = "52725351@qq.com"
FOFA_KEY = "0d98791ef653f285f5245914ea1499a8"

# 从txt文件中读取FOFA语句
def read_queries(file_path):
    queries = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            queries.append(line.strip())
    return queries

# 查询FOFA API并将结果存储在CSV文件中
def query_fofa_api(query):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    params = {
        "email": FOFA_EMAIL,
        "key": FOFA_KEY,
        "qbase64": base64.b64encode(query.encode('utf-8')).decode('utf-8'),
        "fields": "host,ip,title,port,protocol"
    }
    response = requests.get(BASE_URL, params=params, headers=headers, timeout=100)
    if response.status_code == 200:
        results = response.json()["results"]
        write_to_csv(results)
    else:
        print("Failed to query FOFA API for query: {}".format(query))

# 将结果写入CSV文件中
def write_to_csv(results):
    columns_li = ['host','ip','title','port','protocol']
    now = datetime.datetime.now()
    now_str = now.strftime("%Y%m%d")
    filename = f"{now_str}_fofa_res.csv"
    with open(f"{filename}", "a", encoding="utf_8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(columns_li)
        for result in results:
            result_str = str(result)
            try:
                host, ip, title, port, protocol = result_str.split(",")
                writer.writerow([host, ip, title, port, protocol])
            except ValueError as e:
                print("Error processing result: {}".format(result))
                print(e)

# 主函数
if __name__ == "__main__":
    queries = read_queries("fofa_queries.txt")
    for query in queries:
        query_fofa_api(query)

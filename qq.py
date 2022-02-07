

if __name__ == "__main__":
# 请输入自己的API KEY & SECRET
    key = "？？？？？？？？？？？？？？？？？？？？？？"
    secret = "？？？？？？？？？？？？？？？？？？？？？？？"
    
    
    bf = BianceFutureHttpClient(api_key=key, api_secret=secret)
    data = bf.get_server_status()
    print(data)
    
    
    servertime = bf.get_server_time()
    print(servertime)

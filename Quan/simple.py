import zhenzismsclient as smsclient
appId = '110873'
appSecret = '64ff8a00-9d5f-4317-a7b9-e0009a8715'
apiUrl = 'https://sms_developer.zhenzikj.com'
zhenzi_client = smsclient.ZhenziSmsClient(apiUrl, appId, appSecret)
params = {};
params['number'] = '19108471035';
params['templateId'] = '8110';
params['templateParams'] = ['9988', '15分钟'];
print(zhenzi_client.send(params));

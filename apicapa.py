import requests
my_domain = 'luizcaparelli.pythonanywhere.com'
username = 'luizcaparelli'
token = '68de0d81a0ca30cc83cebfd78d3f5df8cd0bf9ce'

response = requests.post(
  'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
      username=username, domain=my_domain
  ),
  headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
  print('All OK')
else:
  print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))

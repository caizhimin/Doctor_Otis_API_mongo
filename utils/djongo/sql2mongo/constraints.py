from utils.djongo.exceptions import NotSupportedError
djongo_access_url = 'https://www.patreon.com/nesdis'
print(f'This version of djongo does not support constraints. Visit {djongo_access_url}')
raise NotSupportedError('constraints')

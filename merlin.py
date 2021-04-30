def get_merlin(q):
	import http.client
	import json
	import urllib.parse
	conn = http.client.HTTPSConnection("8ball.delegator.com")
	question = urllib.parse.quote(q)
	conn.request('GET', '/magic/JSON/' + question)
	response = conn.getresponse()
	ans=(json.loads(response.read()))
	return (ans['magic']['answer'])
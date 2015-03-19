import urllib2, json
input = "politics"
request = urllib2.Request('https://algorithmia.com/algorithms/mia5kovic/scrape_topic')
request.add_header('Content-Type', 'application/json')
request.add_header('Authorization', 'c969aaca93e4435d85436c4f4b43660d')
request.add_header('Accept', 'application/json')
response = urllib2.urlopen(request, json.dumps(input))
print response.read()
def movie_info(id):
	### FILL IN YOUR FUNCTION with what you learned above
	"""
	return a dictionary
	{
	"title":"movie title"
	"description":""
	"rating":"PG"
	"actors":["list","of","actors"]
	}
	"""
	import requests
	from bs4 import BeautifulSoup
	import json
	movie_dict={}
	actorList=[]
	r = requests.get("https://www.imdb.com/title/"+id+"/")
	b = BeautifulSoup(r.text, "lxml")
	movie_dict["title"]=b.title.text
	movie_dict["description"]=b.find("div","summary_text").text.strip()
	stuff = b.find("script",type="application/ld+json")
	rating = json.loads(stuff.text)
	movie_dict["rating"]=rating["contentRating"]
	actors = json.loads(b.find('script', type='application/ld+json').text)['actor']
	for i in actors:
		actorList.append(i["name"])
	movie_dict["actors"]=actorList



	return movie_dict

Adrift = movie_info('tt6306064')
print(Adrift)

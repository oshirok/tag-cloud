from instagram.client import InstagramAPI
import operator

test_tags = {}
# Don't forget to remove the client id!
api = InstagramAPI(client_id='')

# The tag search term
tag_search="universityofwashington"
next_ = None
for x in range(0, 300):
	if next_ is None:
		popular_media, next_ = api.tag_recent_media(count=33, tag_name=tag_search)
	else:
		popular_media, next_ = api.tag_recent_media(count=33, tag_name=tag_search, with_next_url=next_)

	for media in popular_media:
		for tag in media.tags:
			if not str(tag)[5:] in test_tags:
				test_tags[str(tag)[5:]] = 1
			else:
				test_tags[str(tag)[5:]] += 1
		print(media.tags)

	print ("loaded:",x)


sorted_test_tags = sorted(test_tags.items(), key=operator.itemgetter(1), reverse=True)

for x in range(0, 101):
	print str(sorted_test_tags[x][1])

f = open('tempfile', 'w')

for x in range(1, 201):
	word = sorted_test_tags[x]
	print word
	for y in range(0, word[1]):
		f.write(str(word[0]) + ' ')

f.close()
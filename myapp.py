from flask import Flask, jsonify
all_records = [{"albums": [{"description": "\n\tThe King of Limbs is the eighth studio album by English rock band Radiohead, \n\t\t\t\tproduced by Nigel Godrich. It was self-released on 18 February 2011 as a download in MP3 and WAV \n\t\t\t\tformats, followed by physical CD and 12\" vinyl releases on 28 March, a wider digital release via AWAL,\n\t\t\t\t and a special \"newspaper\" edition on 9 May 2011. The physical editions were released through the\n\t\t\t\t  band's Ticker Tape imprint on XL in the United Kingdom, TBD in the United States, and Hostess \n\t\t\t\t  Entertainment in Japan.\n      ", "songs": [{"length": "5:15", "title": "Bloom"}, {"length": "4:41", "title": "Morning Mr Magpie"}, {"length": "4:27", "title": "Little by Little"}, {"length": "3:13", "title": "Feral"}, {"length": "5:01", "title": "Lotus Flower"}, {"length": "4:47", "title": "Codex"}, {"length": "4:50", "title": "Give Up the Ghost"}, {"length": "5:20", "title": "Separator"}], "title": "The King of Limbs"}, {"description": "\n\tOK Computer is the third studio album by the English alternative rock band \n\t\t\t\tRadiohead, released on 16 June 1997 on Parlophone in the United Kingdom and 1 July 1997 by \n\t\t\t\tCapitol Records in the United States. It marks a deliberate attempt by the band to move away \n\t\t\t\tfrom the introspective guitar-oriented sound of their previous album The Bends. Its layered \n\t\t\t\tsound and wide range of influences set it apart from many of the Britpop and alternative rock \n\t\t\t\tbands popular at the time and laid the groundwork for Radiohead's later, more experimental work.\n  ", "songs": [{"length": "4:44", "title": "Airbag"}, {"length": "6:23", "title": "Paranoid Android"}, {"length": "4:27", "title": "Subterranean Homesick Alien"}, {"length": "4:24", "title": "Exit Music (For a Film)"}, {"length": "4:59", "title": "Let Down"}, {"length": "4:21", "title": "Karma Police"}, {"length": "1:57", "title": "Fitter Happier"}, {"length": "3:50", "title": "Electioneering"}, {"length": "4:45", "title": "Climbing Up the Walls"}, {"length": "3:48", "title": "No Surprises"}, {"length": "4:19", "title": "Lucky"}, {"length": "5:24", "title": "The Tourist"}], "title": "OK Computer"}], "name": "Radiohead"}, {"albums": [{"description": "\n\tDummy is the debut album of the Bristol-based group Portishead. Released in \n\t\t\t\tAugust 22, 1994 on Go! Discs, the album earned critical acclaim, winning the 1995 Mercury Music Prize.\n\t\t\t\t It is often credited with popularizing the trip-hop genre and is frequently cited in lists of the best \n\t\t\t\t albums of the 1990s. Although it achieved modest chart success overseas, it peaked at #2 on the UK Album \n\t\t\t\t Chart and saw two of its three singles reach #13. The album was certified gold in 1997 and has sold two \n\t\t\t\t million copies in Europe. As of September 2011, the album was certified double-platinum in the United Kingdom \n\t\t\t\t and has sold as of September 2011 825,000 copies.\n      ", "songs": [{"length": "5:02", "title": "Mysterons"}, {"length": "4:11", "title": "Sour Times"}, {"length": "3:55", "title": "Strangers"}, {"length": "4:16", "title": "It Could Be Sweet"}, {"length": "4:51", "title": "Wandering Star"}, {"length": "3:49", "title": "It's a Fire"}, {"length": "3:54", "title": "Numb"}, {"length": "5:02", "title": "Roads"}, {"length": "3:39", "title": "Pedestal"}, {"length": "5:01", "title": "Biscuit"}, {"length": "5:06", "title": "Glory Box"}], "title": "Dummy"}, {"description": "\n\tThird is the third studio album by English musical group Portishead, \n\t\t\t\treleased on 27 April 2008, on Island Records in the United Kingdom, two days after on Mercury \n\t\t\t\tRecords in the United States, and on 30 April 2008 on Universal Music Japan in Japan. \n\t\t\t\tIt is their first release in 10 years, and their first studio album in eleven years. \n\t\t\t\tThird entered the UK Album Chart at #2, and became the band's first-ever American Top 10 \n\t\t\t\talbum on the Billboard 200, reaching #7 in its entry week.\n      ", "songs": [{"length": "4:58", "title": "Silence"}, {"length": "3:57", "title": "Hunter"}, {"length": "3:16", "title": "Nylon Smile"}, {"length": "4:29", "title": "The Rip"}, {"length": "3:27", "title": "Plastic"}, {"length": "6:27", "title": "We Carry On"}, {"length": "1:31", "title": "Deep Water"}, {"length": "4:43", "title": "Machine Gun"}, {"length": "6:45", "title": "Small"}, {"length": "3:32", "title": "Magic Doors"}, {"length": "5:45", "title": "Threads"}], "title": "Third"}], "name": "Portishead"}]

app = Flask(__name__)
@app.route('/')
def hello():
	return "<h1>Hello, World!</h1>"
@app.route('/records/all_bands/', methods=['GET'])

@app.route('/records/', methods=['GET'])
def get_records():
	return jsonify(all_records)

def get_bands():
	response = [item['name'] for item in all_records]
	return jsonify(response)

@app.route('/records/albums_by_band/<bandname>/', methods=['GET'])
def get_album_by_band(bandname):
	response={bandname:'Not Found!'}
	for item in all_records:
		if item["name"]==bandname:
			response = [x["title"] for x in item["albums"]]
			break
	return jsonify(response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

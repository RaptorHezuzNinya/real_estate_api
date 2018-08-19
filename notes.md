notes for pip3

### how to work with virutalenv
## 1: create virtualenv
# $ virtualenv projectName_venv

## 2: activate virtual env
# $ source projectName_venv/bin/activate

## 3: install packages with pip3
# $ pip3 install package_name

## 4: done working in virtenv
# $ deactivate

#$ 5: In order to keep your environment consistent we FREEZE
# $ pip3 freeze > requirements.txt

## To reinstall packages 
# $ pip3 install -r requirements.txt

####################### Notes ######################################
virtualenv = real_state_API_venv

<!-- used to interact with application from command line -->
# export FLASK_APP=app.py



<!-- [
  {
    "Datum": 20180717,
    "Naam / Omschrijving": "Hr W Verhoef personal",
    "Rekening": "NL46INGB0701357983",
    "Tegenrekening": "NL44INGB0009399983",
    "Code": "GT",
    "Af Bij": "Af",
    "Bedrag (EUR)": "4,50",
    "MutatieSoort": "Online bankieren",
    "Mededelingen": "Naam: Hr W Verhoef personal Omschrijving: Terugbetaling printerette dd17 contract IBAN: NL44INGB0009399983"
  },
  {
    "Datum": 20180717,
    "Naam / Omschrijving": "Hr W Verhoef",
    "Rekening": "NL46INGB0701357983",
    "Tegenrekening": "",
    "Code": "GT",
    "Af Bij": "Bij",
    "Bedrag (EUR)": "30,00",
    "MutatieSoort": "Online bankieren",
    "Mededelingen": "Van Oranje spaarrekening V76937365"
  }] -->

	json_data = json.load(file) # list containing json object (in python dictionaries)
	json_dump = json.dumps(json_data)
	# return render_template('uploadfile.html', var=json_dump)
return jsonify(json_data)
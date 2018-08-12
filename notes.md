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




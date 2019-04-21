
source real_estate_API_venv/bin/activate

pip3 install $1

deactivate

pip3 freeze > requirements.txt

echo "ppackageee: $1 installed and frozen in req.txt"

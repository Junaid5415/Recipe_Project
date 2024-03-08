echo " BUILD START"
C:/Users/Lenovo/.virtualenvs/Recipes-gRl7-pcY/Scripts/python.exe -m pip install -r requirements.txt
C:/Users/Lenovo/.virtualenvs/Recipes-gRl7-pcY/Scripts/python.exe manage.py collectstatic --noinput --clear
echo " BUILD END"
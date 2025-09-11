1. stexcum enq >> .venv >> anunov folder
2. pip install pipenv
3. pipenv shell   >>   lcnum enq .venv folder@, amen angam erb vor project sksenq
4. pipenv install requests   >>   zaprosneri hamar
5. pip install pillow        >>   tarber tesaki nkarneri hamar
6. pipenv install Django    >> pipenv ov em anum vor @ngni .venv is mej, voch te kompi


# stexcum enq djangoi projecti blank@
7. django-admin startproject base .


# amboxj project@ ashxatum a manage.py ov
# stexcum enq mer app-@ manage.py i mijocov
8. python .\manage.py startapp golden


# base/settings.py >> Debub=True, erb vor qcum enq server, petqa False sarqel
# base/settings.py >> Nshum enq te vor web ic karox en mer beqin mianal
# base/settings.py >> INSTALLED_APPS >> petq a mer bolor app-er@ @tex avelacnenq



# project@ start anum enq aysenc >> 
python manage.py runserver



# erb vor visual studion pakum enq u project@ taza aktivacnum enq,
# menq petq e activacnenq mer .venv@, u amen angam terminalum grel >> 
1. pipenv shell
2. python manage.py runserver






# anum enq migracianer@, bayc skzbic petq e stexcenq mer golden/views.py fayl@, 
# ev stexcum mer golden/urls.py fayl@ ev mer base/urls.py i mej avelacnum >> 
# path('golden/', include("golden.urls"))





# migracianer
1. python manage.py makemigrations
2. python manage.py migrate



# stexcel superuser-@
python manage.py createsuperuser
# POKEDEX - DJANGO BACKEND BY DDBC

References to the OFFICIAL POKEDEX SITE point to https://pokeapi.co

## CURRENT ISSUES

    - Sometimes crashes when downloading data from the OFFICIAL POKEDEX SITE

## SETTING UP

1. Open terminal where you want to download the project then run
   - git clone https://github.com/DharylOfficial/pokedex_django
2. Go into the next two pokedex_django folders
   - /pokedex_djang/pokedex_django
3. Run a virtual python environment
   - pipenv shell
4. Install the necessary requirements
   - pip install -r requirements.txt
5. Run the development server
   - python manage.py runserver

## AVAILABLE ENDPOINTS

These endpoints are RESTful:

- /api/pokemon
- /api/pokemon/:id
- /api/type
- /api/type/:id

These endpoints gather data from the OFFICIAL POKEDEX SITE

- /api/reset
  deletes stored pokemon and types and downloads the first 151 pokemon and types
- /pull
  downloads the first 151 pokemon and types
- /pull/types
  downloads all types
- /pull/pokemon
  downlods first 151 pokemon
- /get/types
  returns JSON of all types for GET requests
- /delete/pokemon
  deletes all stored pokemon

# POKEDEX - DJANGO BACKEND BY DDBC

References to the OFFICIAL POKEDEX SITE point to https://pokeapi.co

## CURRENT ISSUES

    - Sometimes crashes when downloading data from the OFFICIAL POKEDEX SITE

## AVAILABLE ENDPOINTS:

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

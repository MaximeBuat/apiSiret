from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/{siret}")
async def root(siret: str):
    api_url = "https://api.insee.fr/entreprises/sirene/V3/siret/"+siret
    response = requests.get(api_url, headers={'Authorization': 'Bearer [key]'})
    res = response.json()['etablissement']

    siren = res['siren']

    address = res['adresseEtablissement']['numeroVoieEtablissement'] + ' ' + res['adresseEtablissement'][
        'typeVoieEtablissement'] + ' ' + res['adresseEtablissement']['libelleVoieEtablissement'] + ' ' + \
              res['adresseEtablissement']['codePostalEtablissement'] + ' ' + res['adresseEtablissement'][
                  'libelleCommuneEtablissement']


    if res['uniteLegale']['denominationUniteLegale'] is None :
        name = res['uniteLegale']['denominationUsuelle1UniteLegale']
    else :
        name = res['uniteLegale']['denominationUniteLegale']


    return {"siren": siren, "Address": address, "name": name}

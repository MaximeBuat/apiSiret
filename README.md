# Api Insee

Install requests package
```bash
python -m pip install requests
```

Install fastApi with

```bash
python -m pip install fastapi
```

And uvicorn

```bash
python -m pip install uvicorn[standard]
```

Then run this command line into the terminal

```bash
uvicorn main:app --reload
```

http://127.0.0.1:8000/api/ {siret number} will return the siren of the company, it’s address and it’s name in JSON format

In main, replace [key] with the key provided by the INSEE at [https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee](https://api.insee.fr/catalogue/site/themes/wso2/subthemes/insee/pages/item-info.jag?name=Sirene&version=V3&provider=insee)

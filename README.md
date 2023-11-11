# Junction2023-Sriep

The repo for the best Junction 2023 Project


## Setup Frontend
To run ionic. You need to do the following.
change the directory to visiorelief
```bash
cd .\visiorelief
```
Run npm install.
```bash
npm install
```
Install ionic client
```bash
npm install -g @ionic/cli
```
Windows by default does not allow you to execute scripts. Run this in an admin powershell prompt if the issue arises.
```bash
Set-ExecutionPolicy -Scope LocalMachine Unrestricted
```
Serve on ionic
```bash
ionic serve
```

## Setup Backend
```bash
python -m venv openai-env
```
```bash
openai-env\Scripts\activate
```
```bash
pip install -r requirements.txt
```

## Testing back-end
Running the back-end:
```bash
python .\visiorelief-backend\main.py
```
JSON example:
```json
{"scene":"Clouds","sounds:["Zen Garden", "Fire Crackling", "Ocean Waves"]","length:100"}
```
CMD example:
```bash
curl -X POST -H "Content-Type: application/json" -d '{\"scene\": \"Clouds\", \"sounds\": [\"Zen Garden\", \"Fire Crackling\", \"Ocean Waves\"], \"length\": 100}' http://127.0.0.1:1337/query
```
Powershell example:
```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:1337/query' -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"scene": "Clouds", "sounds": ["Zen Garden", "Fire Crackling", "Ocean Waves"], "length": 100}'
```

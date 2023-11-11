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

## Testing backend
```bash
python .\visiorelief-backend\main.py
```
```bash
curl http://localhost:5000/query -d "data=I want a scene where I walk through a forest?" -X PUT
```


# Junction2023-Sriep

## ❔ Problem Description:
VisioRelief addresses the pervasive issue of chronic headaches and migraines, providing a comprehensive solution to ease the persistent head pain of people. Chronic headaches not only impact physical well-being but also contribute to emotional and mental distress, affecting the overall quality of life for those who suffer from them.

## 🌍 Real-World Impact:
VisioRelief offers guided imagery sessions that transport users to peaceful landscapes with sounds, promoting relaxation and creating a mental escape from the pain. This approach provides an accessible solution for immediate relief and contributes to the overall well-being of users.

## 💻 Technological Solutions:
- **Text-to-Speech Technology:** Converts written text into natural-sounding speech, enhancing the immersive experience of guided imagery.
- **ChatGPT Integration:** Incorporates advanced conversational AI to interactively guide users through personalized and soothing imagery sessions, tailoring the experience to individual preferences.
- **Flask:** The backbone of our web application, Flask, a lightweight and flexible web framework in Python, facilitates the smooth integration of various components, ensuring responsiveness and efficiency.
- **Vue.js:** Empowering the frontend, Vue.js brings dynamic and reactive user interfaces to life.
- **Node.js:** Asynchronous and event-driven, Node.js serves as the server-side runtime for handling real-time interactions, ensuring smooth communication between the frontend and backend components of VisioRelief.
- **Python:** Instrumental in implementing complex functionalities, including text-to-speech integration and AI-powered features.
- **TypeScript:** Enhancing code maintainability and scalability, TypeScript is employed to add static typing to the JavaScript codebase, reducing errors and enhancing the overall reliability of VisioRelief.

## 💭 Future Enhancements:
VisioRelief remains committed to continual improvement and expansion with:
- **Longer sessions:** Extending session durations to provide sustained relief and cater to varying user needs.  
- **Different voices:** Introducing diverse voices to accommodate user preferences, ensuring a customizable and inclusive experience.
- **Optimization advances:** Striving for even better optimization to enhance the effectiveness of guided imagery sessions and further elevate the overall user experience.

By addressing the challenges associated with chronic headaches and migraines, VisioRelief not only provides immediate relief based on research but also lays the foundation for ongoing advancements to better cater to the diverse needs of its users. This project illustrates a significant step towards chronic pain management without painkillers.


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
curl -X POST -H "Content-Type: application/json" -d '{\"scene\": \"Clouds\", \"sounds\": [\"Zen Garden\", \"Fire Crackling\", \"Ocean Waves\"], \"length\": 100}' http://127.0.0.1:1337/query-text
```
Powershell example:
```powershell
Invoke-RestMethod -Uri 'http://127.0.0.1:1337/query-text' -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"scene": "Clouds", "sounds": ["Zen Garden", "Fire Crackling", "Ocean Waves"], "length": 100}'
```

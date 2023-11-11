import scenes from "@/helpers/scenes";
import sounds from "@/helpers/sounds";

export default async () => {
    //Generate random variables
    const scene = scenes[Math.floor(Math.random() * scenes.length)];
    const sound1_index = Math.floor(Math.random() * sounds.length);
    const sound2_index = Math.floor(Math.random() * sounds.length - 1);
    const sound1 = sounds.splice(sound1_index, 1)[0];
    const sound2 = sounds[sound2_index];
    sounds.push(sound1);
    const chosen_sounds = [sound1, sound2];

    const url = "http://localhost:5000/query"

    //start playing the sounds as intro.
    var audio = new Audio(sound1+'.mp3');
    audio.play();

    console.log(scene)
    console.log(chosen_sounds)

    //Send request to backend with the required variables
    fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' // Specify the content type as JSON
        },
        body: JSON.stringify({scene: scene, sounds: chosen_sounds, length: 100}) // Convert the dataObject to a JSON string
      })
        .then(response => {
          // Handle the response
          if (response.ok) {
            return response.json(); // Parse the JSON response if needed
          } else {
            throw new Error('Network response was not ok.');
          }
        })
        .then(data => {
          // Handle the data returned from the server
          console.log(data);
        })
        .catch(error => {
          // Handle errors
          console.error('There was a problem with the fetch operation:', error);
        });
    //wait 2 minutes to TTS the text

    //ask user for how they felt after the session

    //store the session review in browser storage.
}

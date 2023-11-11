import scenes from "@/helpers/scenes";
import sounds from "@/helpers/sounds";

function play_sound_until_callback(sound: string, callback) {
    console.log("playing: ", sound);
    const audio = new Audio('/sounds/' + sound.toLowerCase() + '.mp3');
    audio.addEventListener('ended', function () {
        this.currentTime = 0;
        this.play();
    }, false);
    audio.play();
}

export default async () => {
    //Generate random variables
    const scene = scenes[Math.floor(Math.random() * scenes.length)];
    const sound1_index = Math.floor(Math.random() * sounds.length);
    const sound2_index = Math.floor(Math.random() * (sounds.length - 1));
    const sound1 = sounds.splice(sound1_index, 1)[0];
    const sound2 = sounds[sound2_index];
    sounds.push(sound1);
    const chosen_sounds = [sound1, sound2];

    //start playing the sounds as intro
    play_sound_until_callback(sound1, () => {
    });
    setTimeout(() => play_sound_until_callback(sound2, () => {
    }), 5000);
    console.log(scene)
    console.log(chosen_sounds)

    //get the text from the backend
    const url = "http://localhost:1337/query"
    //Send request to backend with the required variables
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Specify the content type as JSON
        },
        body: JSON.stringify({scene: scene, sounds: chosen_sounds, length: 100}) // Convert the dataObject to a JSON string
    })
    let text = "";
    // Handle the response
    if (response.ok) {
        text = await response.json(); // Parse the JSON response if needed
    } else {
        throw new Error('Network response was not ok.');
    }
    let utterance = new SpeechSynthesisUtterance("");
    utterance.text = text;
    utterance.rate *= 0.60;
    console.log(utterance.rate);
    window.speechSynthesis.speak(utterance);

    //wait 2 minutes to TTS the text

    //ask user for how they felt after the session

    //store the session review in browser storage.
}

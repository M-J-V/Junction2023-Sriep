import scenes from "@/helpers/scenes";
import sounds from "@/helpers/sounds";
import {arrayBuffer} from "stream/consumers";

const ctx = new AudioContext();

//Loop sound
function play_sound_until_callback(sound: string) {
    console.log("playing: ", sound);
    const audio = new Audio('/sounds/' + sound.toLowerCase() + '_norm_loop.mp3');
    audio.volume = 0.1;
    audio.addEventListener('ended', loop_sound, false);
    return audio
}

//Function ran when looping sounds
function loop_sound(this: HTMLAudioElement) {
    this.currentTime = 0;
    this.play();
}

//default function for relief. When this is run, two random sounds get selected and a scene.
// This will be sent to the backend to generate a prompt to think about
export default async (): Promise<{sounds: string[], scene: string}> => {
    //Generate random scene
    const scene = scenes[Math.floor(Math.random() * scenes.length)];
    // Generate two random sounds with different indexes
    const sound1_index = Math.floor(Math.random() * sounds.length);
    const sound2_index = Math.floor(Math.random() * (sounds.length - 1));
    const sound1 = sounds.splice(sound1_index, 1)[0];
    const sound2 = sounds[sound2_index];
    sounds.push(sound1);

    // turn it into an array
    const chosen_sounds = [sound1, sound2];

    //start playing the sounds as intro
    let sound1_handle = play_sound_until_callback(sound1);
    let sound2_handle = play_sound_until_callback(sound2);
    //play sound 1
    sound1_handle.play()
    //play sound 2, 5 seconds later
    setTimeout(() => sound2_handle.play(), 5000);

    // Get the audio from the backend.
    // For the hackathon, we have used a constant variable. Of cousre, when creating better backend,
    // this should be replaced with a dynamic variable based on a config file or an env variable
    // TODO: Replace static url with one collected from environment variable
    const url = "http://localhost:1337/query"

    // Send request to backend with the required variables
    let response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Specify the content type as JSON
        },
        body: JSON.stringify({scene: scene, sounds: chosen_sounds, length: 100}) // Convert the dataObject to a JSON string
    })

    if (!response.ok) {
        throw new Error("Network Error");
    }
    //Turn the gathered data from the server to an audio element
    let blob = await response.blob();
    const audioURL = URL.createObjectURL(blob);
    let talker = new Audio(audioURL);

    //Return a promise for when the voice is done with playing
    return new Promise((resolve, reject) => {
        //This event listener waits for the speech to be done playing and then resolves the promise.
        //Ideally this is run by different functions and not done with one single function
        talker.addEventListener('ended', function () {
            //5 seconds after the talk is done, remove the looping for the ambient sounds and resolve the promise
            setTimeout(() => {
                sound1_handle.removeEventListener("ended", loop_sound);
                sound2_handle.removeEventListener("ended", loop_sound);
                resolve({sounds: chosen_sounds, scene});
            }, 5000)
        }, false);
        //play the speech
        talker.play();
    });
}

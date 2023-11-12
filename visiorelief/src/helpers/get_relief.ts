import scenes from "@/helpers/scenes";
import sounds from "@/helpers/sounds";
import {arrayBuffer} from "stream/consumers";

const ctx = new AudioContext();

//Loop sound until callback is ran
function play_sound_until_callback(sound: string) {
    console.log("playing: ", sound);
    const audio = new Audio('/sounds/' + sound.toLowerCase() + '_norm_loop.mp3');
    audio.volume = 0.1;
    audio.addEventListener('ended', loop_sound, false);
    return audio
}

function loop_sound(this: HTMLAudioElement) {
    this.currentTime = 0;
    this.play();
}

export default async (): Promise<{sounds: string[], scene: string}> => {
    //Generate random variables
    const scene = scenes[Math.floor(Math.random() * scenes.length)];
    const sound1_index = Math.floor(Math.random() * sounds.length);
    const sound2_index = Math.floor(Math.random() * (sounds.length - 1));
    const sound1 = sounds.splice(sound1_index, 1)[0];
    const sound2 = sounds[sound2_index];
    sounds.push(sound1);
    const chosen_sounds = [sound1, sound2];

    //start playing the sounds as intro
    let sound1_handle = play_sound_until_callback(sound1);
    let sound2_handle = play_sound_until_callback(sound2);
    sound1_handle.play()
    setTimeout(() => sound2_handle.play(), 5000);
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

    if (!response.ok) {
        throw new Error("Network Error");
    }
    let blob = await response.blob();
    const audioURL = URL.createObjectURL(blob);
    let talker = new Audio(audioURL);
    return new Promise((resolve, reject) => {
        talker.addEventListener('ended', function () {
            //2 minutes
            setTimeout(() => {
                sound1_handle.removeEventListener("ended", loop_sound);
                sound2_handle.removeEventListener("ended", loop_sound);
                resolve({sounds: chosen_sounds, scene});
            }, 5000)
        }, false);
        talker.play();
    });
    // const playSound = ctx.createBufferSource();
    // playSound.buffer = audio;
    // playSound.connect(ctx.destination)
    // playSound.start(ctx.currentTime)


    //wait 2 minutes to TTS the text

    //ask user for how they felt after the session

    //store the session review in browser storage.
}

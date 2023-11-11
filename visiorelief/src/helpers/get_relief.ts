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

    //start playing the sounds as intro
    console.log(scene);
    console.log(chosen_sounds);

    //Send request to backend with the required variables
    fetch('/backend');

    //wait 2 minutes to TTS the text

    //ask user for how they felt after the session

    //store the session review in browser storage.
}

<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div id="background"></div>
      <div id="container" class="background-container">
        <ion-button @click="relieve_user" shape="round">Relief</ion-button>
      </div>
      <screen-cover @done="submit_response" v-if="relieving" :done="done"/>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import {IonButton, IonContent, IonPage} from '@ionic/vue';
import get_relief from '@/helpers/get_relief'
import {ref} from "vue";
import ScreenCover from "@/components/ScreenCover.vue";
import {Session} from "@/helpers/session";
import {Ref} from "@vue/reactivity";
import {Storage} from "@ionic/storage";

// setup dynamic variables
const relieving = ref(false);
const done = ref(false);
const sounds: Ref<string[]> = ref([]);
const scene = ref("");

function relieve_user() {
  //set the relieving scene to on
  relieving.value = true;
  //play the sound
  get_relief().then(
      //when done with talking
      response => {
        //set that we're done with talking and which sounds got generated
        done.value = true;
        scene.value = response['scene'];
        sounds.value = response['sounds'];
      }
  )
}

//create store for storage on the browser
const session_store = new Storage();
session_store.create();

//create a log for how the person felt after the session
async function submit_response(response: number) {
  //disable the relieving scene
  done.value = false;
  relieving.value = false;
  //check if the session variable has been set before
  let sessions = await session_store.get('session')
  //if not, create one
  if (sessions == null) {
    sessions = {};
  }
  //get the current date
  let d = new Date();
  //store the date in a dictionary
  sessions[d.toISOString()] = {
    day: d,
    setting: scene.value,
    sounds: [sounds.value[0], sounds.value[1]],
    response,
  };
  //set the chosen variable
  await session_store.set('session', sessions)
}
</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 80%;
  transform: translateY(-50%);
}

#background {
  background-image: url('/logo.png');
  height: 75%;
  width: 100%;
  background-size: contain;
  background-position: center;
  background-repeat: no-repeat;
  flex-direction: column;
  position: absolute;
  top: 0;

}

ion-button {
  width: 10rem;
  height: 5rem;
  font-size: 1.5rem;
}
</style>
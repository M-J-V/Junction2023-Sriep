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
import {IonButton, IonContent, IonHeader, IonPage, IonTitle, IonToolbar} from '@ionic/vue';
import get_relief from '@/helpers/get_relief'
import {ref} from "vue";
import ScreenCover from "@/components/ScreenCover.vue";
import {Session} from "@/helpers/session";
import {Ref} from "@vue/reactivity";
import {Storage} from "@ionic/storage";

const relieving = ref(false);
const done = ref(false);

const sounds: Ref<string[]> = ref([]);
const scene = ref("");

function relieve_user() {
  relieving.value = true;
  get_relief().then(
      response => {
        done.value = true;
        scene.value = response['scene'];
        sounds.value = response['sounds'];
      }
  )
  done.value = true;
}

const session_store = new Storage();
session_store.create();

async function submit_response(response: number) {
  console.log("i got called with number", response)
  done.value = false;
  relieving.value = false;
  let sessions = await session_store.get('session')
  if (sessions == null) {
    sessions = {};
  }
  let d = new Date();
  sessions[d.toISOString()] = {
    day: d,
    setting: scene.value,
    sounds: [sounds.value[0], sounds.value[1]],
    response,
  };
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
  background-image: url('logo.png');
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
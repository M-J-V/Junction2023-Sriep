<template>
  <div id="container">
      <ion-card v-for="(day, name, index) in days" class="row">
        <div class="icon">
          <font-awesome-icon v-if="day.response == -1" :icon="['fas', 'frown']" style="color: #f6555d" />
          <font-awesome-icon v-else-if="day.response == 0" :icon="['fas', 'meh']" style="color: #e56f00"/>
          <font-awesome-icon v-else-if="day.response == 1" :icon="['fas', 'smile']" style="color: #06b443"/>
        </div>
        <div style="flex:1">
          <ion-card-header>
            <ion-card-title>Session log {{index+1}}</ion-card-title>
            <ion-card-subtitle>Date: {{day.day.toISOString().split('T')[0]}}</ion-card-subtitle>
          </ion-card-header>
          <ion-card-content>
            <ion-text>Setting: {{day.setting}}</ion-text><br>
            <ion-text>Sounds: {{day.sounds.join(', ')}}</ion-text>
          </ion-card-content>
        </div>
      </ion-card>
  </div>
</template>

<script setup lang="ts">
import sounds from '@/helpers/sounds.ts';
import scenes from '@/helpers/scenes.ts';

import {IonText, IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent} from '@ionic/vue';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faSmile, faMeh, faFrown } from '@fortawesome/free-solid-svg-icons'

import {Session} from '@/helpers/session';

/* import storage */
import { Storage } from  '@ionic/storage';
import {ref} from "vue";
import {Ref} from "@vue/reactivity";

// Setup the session store
const session_store = new Storage();
session_store.create();
// session_store.clear();

async function store_session(day: Date, session: Session) {
  let sessions = await session_store.get('session')
  if (sessions == null) {
    sessions = {};
  }
  sessions[day.toISOString()] = session;
  await session_store.set('session', sessions)
}

async function get_sessions(): Promise<Array<Session>> {
  return await session_store.get('session')
}

library.add(faSmile)
library.add(faMeh)
library.add(faFrown)

function getRandomInt(max: number) {
  return Math.floor(Math.random() * max);
}

let days: Ref<Session[]> = ref([]);
get_sessions().then((sessions) => {
  console.log(sessions)
  days.value = sessions
})

</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column-reverse;
}

.row {
  display: flex;
}

.icon {
  height: 100%;
  font-size: 5rem;
  display: flex;
  justify-content: center;
  margin: 1rem;
}

ion-card {
  display: flex;
  justify-content: center;
}

font-awesome-icon {
  height: 100%;
}
</style>

<template>
  <div id="container">
    <div>
      <ion-card v-for="(day, index) in days.reverse()" class="row">
        <div class="icon">
          <font-awesome-icon v-if="day.response == -1" :icon="['fas', 'frown']" style="color: #f6555d" />
          <font-awesome-icon v-else-if="day.response == 0" :icon="['fas', 'meh']" style="color: #e56f00"/>
          <font-awesome-icon v-else-if="day.response == 1" :icon="['fas', 'smile']" style="color: #06b443"/>
        </div>
        <div style="flex:1">
          <ion-card-header>
            <ion-card-title>Session log {{days.length - index}}</ion-card-title>
            <ion-card-subtitle>Date: {{day.day.toISOString().split('T')[0]}}</ion-card-subtitle>
          </ion-card-header>
          <ion-card-content>
            <ion-text>Setting: {{day.setting}}</ion-text><br>
            <ion-text>Sounds: {{day.sounds.join(', ')}}</ion-text>
          </ion-card-content>
        </div>
      </ion-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import sounds from '@/helpers/sounds.ts';
import scenes from '@/helpers/scenes.ts';

import {IonText} from '@ionic/vue';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faSmile, faMeh, faFrown } from '@fortawesome/free-solid-svg-icons'

/* import storage */
import { Storage } from  '@ionic/storage';

// Setup the session store
const session_store = new Storage();
await session_store.create();

async function store_session(day: Date, session: any) {
  session_store.set(day.toString(), session);
  
  console.log(session_store.keys())
}

async function get_session(day: Date) {
  return session_store.get(day.toString())
}

async function reset_session_store() {
  session_store.clear()
}

// If you want to reset the store after every refresh, comment out if not
reset_session_store()

library.add(faSmile)
library.add(faMeh)
library.add(faFrown)

function getRandomInt(max: number) {
  return Math.floor(Math.random() * max);
}

var d = new Date();
let days = [];
for (let i = 0; i < 10; i++) {
  const randomElement = scenes[Math.floor(Math.random() * scenes.length)];
  const sound1_index = Math.floor(Math.random() * sounds.length);
  const sound2_index = Math.floor(Math.random() * sounds.length - 1);
  const sound1 = sounds.splice(sound1_index, 1)[0];
  const sound2 = sounds[sound2_index];
  sounds.push(sound1);
  let session = {
    day: d,
    setting: randomElement,
    sounds: [sound1, sound2],
    response: getRandomInt(3)-1,
  }
  await store_session(d, session)
  // days.push(session);
  d.setDate(d.getDate() - 1);
}

</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  display: flex;
  flex-direction: column;
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

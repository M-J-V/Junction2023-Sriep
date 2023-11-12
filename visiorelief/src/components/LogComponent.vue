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
//Load used Ionic components
import {IonText, IonCard, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent} from '@ionic/vue';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import { faSmile, faMeh, faFrown } from '@fortawesome/free-solid-svg-icons'
/* Register font-awesome icons */
library.add(faSmile)
library.add(faMeh)
library.add(faFrown)

/* import the session type*/
import {Session} from '@/helpers/session';

/* import storage */
import { Storage } from  '@ionic/storage';
import {ref} from "vue";
import {Ref} from "@vue/reactivity";

// Set up the session store
const session_store = new Storage();
session_store.create();

//Create a session array with ref
let days: Ref<Session[]> = ref([]);

//define async function to get sessions
async function get_sessions(): Promise<Array<Session>> {
  return await session_store.get('session')
}

//Load sessions from the storage
get_sessions().then((sessions) => {
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

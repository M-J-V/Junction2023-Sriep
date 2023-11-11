<template>
  <ion-page>
<!--    <ion-header>-->
<!--      <ion-toolbar>-->
<!--        <ion-title>Tab 2</ion-title>-->
<!--      </ion-toolbar>-->
<!--    </ion-header>-->
    <ion-content :fullscreen="true">
      <ion-header collapse="condense"  class="ion-no-border">
        <ion-toolbar>
          <ion-title size="large" style="text-align: center">Relief</ion-title>
        </ion-toolbar>
      </ion-header>
      <div id="background"></div>
      <div id="container" class="background-container">
        <ion-button @click="relieve_user" shape="round">Relief</ion-button>
      </div>
      <screen-cover v-if="relieving" :done="done"/>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton } from '@ionic/vue';
import get_relief from '@/helpers/get_relief'
import {ref} from "vue";
import ScreenCover from "@/components/ScreenCover.vue";

const relieving = ref(false);
const done = ref(false);
function relieve_user() {
  relieving.value = true;
  get_relief().then(
      () => done.value = true
  )
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
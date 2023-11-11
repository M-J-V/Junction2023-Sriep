<template>
  <ion-page>
<!--    <ion-header>-->
<!--      <ion-toolbar>-->
<!--        <ion-title>Tab 2</ion-title>-->
<!--      </ion-toolbar>-->
<!--    </ion-header>-->
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Relief</ion-title>
        </ion-toolbar>
      </ion-header>
      <div id="container">
        <ion-button @click="relieve_user" shape="round">Relief</ion-button>
      </div>
      <screen-cover v-if="relieving"/>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonButton } from '@ionic/vue';
import get_relief from '@/helpers/get_relief'
import {ref} from "vue";
import ScreenCover from "@/components/ScreenCover.vue";

const relieving = ref(false);

function relieve_user() {
  relieving.value = true;
  get_relief()
}
</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 75%;
  transform: translateY(-50%);
}

ion-button {
  width: 10rem;
  height: 5rem;
  font-size: 1.5rem;
}
</style>
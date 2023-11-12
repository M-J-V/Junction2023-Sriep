<template>
  <ion-page>
    <ion-header  class="ion-no-border">
      <ion-toolbar>
        <ion-title style="text-align: center">Settings</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense"  class="ion-no-border">
        <ion-toolbar>
          <ion-title size="large">Settings</ion-title>
        </ion-toolbar>
      </ion-header>
      <div id="container">
          <ion-button routerLink="./about" size="large" shape="round">About us</ion-button><br>
<!--          <ion-button size="large" shape="round">Customize</ion-button><br>-->
          <ion-button id="wipe_alert" size="large" color="danger" shape="round">Clear Data</ion-button><br>
          <ion-alert
              trigger="wipe_alert"
              header="WARNING: This will wipe all your logs"
              sub-header="Pressing this option will remove all of your data"
              message="Are you sure you want to delete it?"
                :buttons="alertButtons"
              @didDismiss="dismiss_me"
          ></ion-alert>
      </div>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent, IonAlert, IonButton } from '@ionic/vue';
import LogComponent from '@/components/LogComponent.vue';
import {Storage} from "@ionic/storage";

function dismiss_me(test) {
  if (test.detail.role == 'confirm') {
    const session_store = new Storage();
    session_store.create();
    session_store.clear();
  }
}

const alertButtons = [
  {
    text: 'Cancel',
    cssClass: 'alert-button-cancel',
    role: 'cancel'
  },
  {
    text: 'YES - WIPE',
    cssClass: 'alert-button-confirm',
    role: 'confirm'
  },
];

function clear_data_modal() {

}

</script>
<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}
</style>

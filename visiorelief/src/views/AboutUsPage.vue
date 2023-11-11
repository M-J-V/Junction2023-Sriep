<script setup lang="ts">
import {IonBackButton, IonContent, IonHeader, IonPage, IonText, IonTitle, IonToolbar} from '@ionic/vue'
</script>

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button></ion-back-button>
        </ion-buttons>
        <ion-title>About us</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">About us</ion-title>
        </ion-toolbar>
      </ion-header>
      <div id="content">
        <ion-text>
          We are committed to redefining the approach to chronic pain management. VisioRelief is more than an app; it's a partner on your journey toward a life with less pain and more moments of joy.

          We envision a world where chronic pain is met with personalized, holistic solutions that extend beyond traditional approaches. By integrating cutting-edge technology, our platform offers a unique blend of visual and auditory experiences tailored to bring you comfort, serenity, and relief.
        </ion-text>
      </div>
    </ion-content>
  </ion-page>
</template>

<style scoped>
#content {
  margin: 5%;
  display: flex;
  text-align: center;
  justify-content: center;
}

ion-text {
  max-width: 52rem;
}
</style>
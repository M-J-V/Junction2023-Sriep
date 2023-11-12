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
        <div class="logo">
          <!-- Your logo image goes here -->
          <img src="/logo.png" alt="Logo">
        </div>
        <div>
          <ion-text>
          We are committed to redefining the approach to chronic pain management. VisioRelief is more than an app; it's a partner on your journey toward a life with less pain and more moments of joy.

          We envision a world where chronic pain is met with personalized, holistic solutions that extend beyond traditional approaches. By integrating cutting-edge technology, our platform offers a unique blend of visual and auditory experiences tailored to bring you comfort, serenity, and relief.
        </ion-text>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<style scoped>
#content {
  height: 100vh;
  display: flex;
  flex-direction: column; /* Arrange children in a column layout */
  align-items: center; /* Align to the top */
  justify-content: center;
  text-align: center;
  margin: 0 10%;
}

.logo {
  margin-bottom: 20px; /* Adjust as needed to provide space between the logo and text */
  display: flex;
  justify-content: center;
  align-content: center;
}

.logo img {
  max-width: 80%; /* Ensure the logo does not exceed its container's width */
}

ion-text {
  max-width: 52rem;
}
</style>
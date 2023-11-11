<template>
  <ion-page>
    <ion-header  class="ion-no-border"> 
      <ion-toolbar>
        <ion-title style="color: #415D7A;">Migraine history</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Migraine history</ion-title>
        </ion-toolbar>
      </ion-header>

      <log-component/>
    </ion-content>
  </ion-page>
</template>

<script setup lang="ts">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import LogComponent from "@/components/LogComponent.vue";
</script>

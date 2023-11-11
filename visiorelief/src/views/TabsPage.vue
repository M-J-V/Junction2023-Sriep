<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        <ion-tab-button tab="migraine_logs" href="/tabs/migraine_logs">
          <ion-icon aria-hidden="true" :icon="folder" />
          <ion-label>Sessions</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="relief" href="/tabs/relief">
          <ion-icon aria-hidden="true" :icon="home" />
          <ion-label>Home</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="tab1" href="/tabs/tab1">
          <ion-icon aria-hidden="true" :icon="cog" />
          <ion-label>Settings</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script setup lang="ts">
import { IonTabBar, IonTabButton, IonTabs, IonLabel, IonIcon, IonPage, IonRouterOutlet } from '@ionic/vue';
import {cog, ellipse, folder, home, statsChartOutline, triangle} from 'ionicons/icons';
</script>

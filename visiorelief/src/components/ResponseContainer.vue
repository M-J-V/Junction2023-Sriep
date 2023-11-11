<template>
  <div id="container">
    <strong>How is your migraine feeling now?</strong>
    <div>
      <ion-button fill="clear" color="success">
        <font-awesome-icon :icon="['fas', 'smile']" />
      </ion-button>
      <ion-button fill="clear" color="warning">
        <font-awesome-icon :icon="['fas', 'meh']" />
      </ion-button>
      <ion-button fill="clear" color="danger">
        <font-awesome-icon :icon="['fas', 'frown']" />
      </ion-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import {IonButton} from '@ionic/vue';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faSmile, faMeh, faFrown } from '@fortawesome/free-solid-svg-icons'

library.add(faSmile)
library.add(faMeh)
library.add(faFrown)

defineProps({
  name: String,
});

function play_the_sound() {
  let msg = new SpeechSynthesisUtterance();
  msg.text = "Hello World. This is a short demo to see if this works";
  console.log("speaking")
  window.speechSynthesis.speak(msg);
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

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}

ion-button {
  height: 10rem;
  width: 10rem;
  font-size: 5rem;
  margin: 1rem;
}
</style>

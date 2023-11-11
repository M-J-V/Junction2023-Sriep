<script setup lang="ts">
import {IonText} from "@ionic/vue";
import ResponseContainer from "@/components/ResponseContainer.vue";
const props = defineProps({
  done: Boolean
})

const emit = defineEmits(['done'])
function done(value: number) {
  emit('done', value);
}

</script>

<template>
  <div id="cover">
    <div id="top_half">

    </div>
    <div id="bottom_half">

    </div>
    <div id="top_cover" v-if="!props.done">
      <ion-text>
        Make your room dark
      </ion-text>
      <div class="img-container">
        <img style="position: relative" src="/icons/merged.svg" alt="curtain">
      </div>
      <ion-text>
        Get yourself in a comfortable position,
      </ion-text>
      <div class="img-container">
        <img src="/icons/bed.svg" alt="bed">
      </div>
      <ion-text>
        Close your eyes, and listen.
      </ion-text>
      <div class="img-container">
        <img src="/icons/eyes.png" alt="eyes">
      </div>
    </div>
    <response-container @done="done" v-else/>
  </div>
</template>

<style scoped>


@keyframes setOpacity {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes slideInFromTop {
  0% {
    top: -50%;
  }
  100% {
    top: 0;
  }
}

@keyframes slideInFromBottom {
  0% {
    bottom: -50%;
  }
  100% {
    bottom: 0;
  }
}

#cover {
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
}

#top_half {
  height: 50%;
  width: 100%;
  background-color: black;
  animation: 3s ease-in-out 0s 1 slideInFromTop;
  position: relative;
}

#bottom_half {
  height: 50%;
  width: 100%;
  background-color: black;
  position: relative;
  animation: 3s ease-in-out 0s 1 slideInFromBottom;
}

#top_cover {
  position: absolute;
  height: 100%;
  text-align: center;
  width: 100%;
  color: white;
  opacity: 0;
  top: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-content: center;
  animation: 3s ease-in 3s 1 setOpacity;
  animation-fill-mode: forwards;
}

.img-container {
  height: 25%;
}

img {
  height: 100%;
}
</style>
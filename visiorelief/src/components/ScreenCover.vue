<script setup lang="ts">

</script>

<template>
  <div id="cover">
    <div id="top_half">

    </div>
    <div id="bottom_half">

    </div>
    <div id="top_cover">
      hello world
    </div>
  </div>
</template>

<style scoped>

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
  top:0;
  left:0;
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
  width: 100%;
  color: white;
  top: 0;
}
</style>
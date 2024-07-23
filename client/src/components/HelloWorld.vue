<script setup lang="ts">
import {ref} from 'vue'

defineProps<{ msg: string }>()

const count = ref(0)
</script>

<template>
<!--  <h1>{{ msg }}</h1>-->

<!--  <div class="card">-->
<!--    <button type="button" @click="count++">count is {{ count }}</button>-->
<!--  </div>-->

  <div>
    <!--    <iframe width="560" height="315" src="https://www.kongregate.com/games/maxblive/flappy-bird-flash#"-->
    <!--            title="YouTube video player"-->
    <!--            frameborder="0"-->
    <!--            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"-->
    <!--            referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>-->

<!--        <iframe width="560" height="700" frameBorder=0 allowfullscreen allow="geolocation; microphone;camera"-->
<!--                src="http://flappybird.io/"></iframe>-->

    <!--    <iframe src="https://www.crazygames.com/embed/flappy-bird" style="width: 100%; height: 100%;" frameborder="0"-->
    <!--            allow="gamepad *;"></iframe>-->

    <iframe id="iframehtml5" width="500" height="700" frameborder="0" border="0" scrolling="no" class="iframe-default"
            allowfullscreen="true" src="https://flappybird.gg/game"></iframe>


  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

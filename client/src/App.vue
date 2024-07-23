<script setup lang="ts">
import { onMounted, ref } from 'vue'


//GET REQUEST//
const testvalue = ref([])
onMounted(async () => {
  testvalue.value = await getattractions()
})
async function getattractions() {
  let myObject = await fetch("/api/testclass");
  let myattractions = await myObject.json();
  return myattractions
}

//POST REQUEST//
async function start_bot() {
    const response = await fetch("/api/start_game_bot", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
    })
    console.log(response.statusText)
}


const count = ref(0)
</script>

<template>
<!--  <HelloWorld msg="Vite + Vue" />-->
  <section class="hero-section">
    <div class="nav-wrapper">
      <img src="/flappy_bird.png" loading="lazy" alt="flappy bird icon" width="50" height="60">
      <div class="nav-buttons-wrapper">
        <button class="nav-button" type="button" @click="count++">Play</button>
        <button class="nav-button" type="button" @click="count++">About</button>
      </div>
    </div>
    <div class="main-page-wrapper">
      <div class="hero-content-wrapper">
<!--        <h1 class="hero-title">Flappy Bird</h1>-->
      </div>
      <div class="game-section-wrapper">
        <div class="left-hero-section-wrapper">
          <div class="left-hero-section-content">
            <h1 class="hero-title">Flappy Bird</h1>
            <button class="play-button" type="button" @click="start_bot()">Auto Play</button>
            <div>
              <Suspense>{{testvalue}}</Suspense>
            </div>
          </div>
        </div>
        <iframe id="iframehtml5" width="500" height="700" frameborder="0" border="0" scrolling="no" class="iframe-default"
                allowfullscreen="false" src="https://flappybird.gg/game">
        </iframe>
        <div class="right-hero-section-wrapper">
          <div class="right-hero-section-content"></div>
        </div>
      </div>
      <div class="bottom-content-wrapper">
<!--        <Suspense>{{testvalue}}</Suspense>-->
      </div>
    </div>

  </section>

</template>

<style scoped>
h1 {
  margin: 0px;
  padding: 0px;
}

.nav-wrapper {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  background-color: #b8f0fb;
  justify-content: space-between;
  padding: 11px;
  display: flex;
}

.nav-buttons-wrapper {
  grid-column-gap: 30px;
  grid-row-gap: 36px;
  background-color: rgba(33, 255, 0, 0.26);
  border-radius: 200px;
  margin: 12px;
  padding: 10px 20px;
  display: flex;
}

.nav-button {
  color: #ffffff;
  background-color: rgba(148, 63, 63, 0); font-size: 16px;
  font-weight: 600;
  text-decoration: none;
}

.nav-button:hover {
  color: #ffdddd;
}

.nav-button:focus {
  color: #001975;
}

.main-page-wrapper {
  padding: 19px;
  background-color: transparent;
}

.game-section-wrapper {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: space-between;
  padding: 0px;
  margin-top: 20px;
  display: flex;
}

.left-hero-section-wrapper {
  width: 400px;
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
}

.left-hero-section-content {
  padding: 20px;
}

.hero-title {
  //font-size: 30px;
  font-weight: 600;
  padding: 5px 10px;
  color: #ffffff;
  background-color: #b8f0fb;
  border-radius: 30px;
  margin-bottom: 10px;
}

.play-button {
  color: #ffffff;
  background-color: #ffafaf;
  font-size: 16px;
  font-weight: 600;
  text-decoration: none;
}

.play-button:hover {
  color: #ffdddd;
}

.play-button:focus {
  color: #001975;
}

.right-hero-section-wrapper {
  width: 400px;
}
</style>

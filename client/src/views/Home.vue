<script setup lang="ts">
import { onMounted, ref } from 'vue'


//GET REQUEST//
const flap_highscores = ref([])
onMounted(async () => {
  flap_highscores.value = await getHighscores()
})
async function getHighscores() {
  let myObject = await fetch("/api/testclass");
  let highscores = await myObject.json();
  return highscores
}

//POST REQUEST//
async function start_bot() {
  const response = await fetch("/api/start_game_bot", {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
  })
  console.log(response.statusText)
}

//POST REQUEST//
async function stop_bot() {
  const response = await fetch("/api/stop_game_bot", {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
  })
  console.log(response.statusText)
}

</script>

<template>
  <!--  <HelloWorld msg="Vite + Vue" />-->
  <section class="hero-section">
    <div class="nav-wrapper">
      <img src="/flappy_bird.png" loading="lazy" alt="flappy bird icon" width="50" height="60">
      <div class="nav-buttons-wrapper">
        <router-link to="/" class="nav-play-button">Play</router-link>
        <router-link to="/about" class="nav-button">About</router-link>
        <!--        <button class="nav-button" type="button" @click="count++">Play</button>-->
        <!--        <button class="nav-button" type="button" @click="count++">About</button>-->
      </div>
    </div>
    <div class="main-page-wrapper">
      <div class="hero-content-wrapper">
      </div>
      <div class="game-section-wrapper">
        <div class="left-hero-section-wrapper">
          <div class="left-hero-section-content">
            <h1 class="hero-title">Flappy Bird</h1>
            <div class="button-wrapper">
              <button class="play-button" type="button" @click="start_bot()">Start Auto Play</button>
            </div>
          </div>
        </div>
        <iframe id="iframehtml5" width="500" height="700" frameborder="0" border="0" scrolling="no" class="iframe-default"
                allowfullscreen="false" src="https://flappybird.gg/game">
        </iframe>
        <div class="right-hero-section-wrapper">
          <div class="right-hero-section-content">
            <h1 class="hero-title">High Scores</h1>
            <table>
              <tr>
                <th class="table-left">#</th>
                <th>Date</th>
                <th class="table-right">Score</th>
              </tr>
              <template v-for="(score, index) in flap_highscores">
                <tr>
                  <td><Suspense>{{ index + 1 }}</Suspense></td>
                  <td><Suspense>{{ score[1] }}</Suspense></td>
                  <td><Suspense>{{ score[2] }}</Suspense></td>
                </tr>
              </template>
            </table>
          </div>
        </div>
      </div>
      <div class="bottom-content-wrapper">
      </div>
    </div>

  </section>

</template>

<style scoped>
.game-section-wrapper {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: space-between;
  padding: 0px;
  margin-top: 20px;
  display: flex;
}

.left-hero-section-wrapper {
  width: 420px;
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
  margin-left: 30px;
}

.right-hero-section-wrapper {
  width: 420px;
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
  margin-right: 30px;
}

.left-hero-section-content {
  padding: 20px;
}

.right-hero-section-content {
  padding: 20px;
}

.high-score-table {
  margin-top: 20px;
  color: #ffffff;
  background-color: #ffb9b9;
  border-radius: 20px;
  height: 600px;
  padding: 10px;
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

.button-wrapper {
  margin-top: 25px;
  //justify-content: center;
  //display: flex
}

.play-button {
  color: #ffffff;
  background-color: #ffafaf;
  font-size: 16px;
  font-weight: 600;
  text-decoration: none;
  border-radius: 15px;
  padding: 10px
}

.play-button:hover {
  color: #ffdddd;
}

.play-button:active {
  background-color: #fd9292;
}

.nav-play-button {
  color: #ffffff;
  background-color: rgba(148, 63, 63, 0); font-size: 16px;
  font-weight: 600;
  text-decoration: none;
}


table {
  border-collapse: collapse;
  width: 100%;
  margin-top: 20px;
}

th {
  background-color: #ffb9b9;
  color: white;
  text-align: left;
  padding: 8px;
}

.table-left{
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
}

.table-right{
  border-top-right-radius: 15px;
  border-bottom-right-radius: 15px;
}

td {
  text-align: left;
  padding: 8px;
  color: #515151;
}

tr:nth-child(even){
  //background-color: #ff6d6d
}

</style>

<script setup lang="ts">

</script>

<template>
  <!--  <HelloWorld msg="Vite + Vue" />-->
  <section class="hero-section">
    <div class="nav-wrapper">
      <img src="/flappy_bird.png" loading="lazy" alt="flappy bird icon" width="50" height="60">
      <div class="nav-buttons-wrapper">
<!--        <a href="client/src/App.vue"><button class="nav-button" type="button" @click="count++">Play</button></a>-->
<!--        <a href="About.vue"><button class="nav-button" type="button" @click="count++">About</button></a>-->
        <router-link to="/home" class="nav-button">Play</router-link>
        <router-link to="/about" class="nav-button">About</router-link>
      </div>
    </div>
    <div class="main-page-wrapper">
      <div class="hero-content-wrapper">
      </div>
      <div class="game-section-wrapper">
        <div class="left-hero-section-wrapper">
          <h1 class="hero-title">Flappy Bird</h1>
        </div>
        <div class="right-hero-section-wrapper"></div>
      </div>
      <div class="bottom-content-wrapper">
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
  background-color: rgba(255, 255, 255, .9);
  border-radius: 200px;
  margin: 12px;
  padding: 10px 20px;
  display: flex;
}

.nav-button {
  color: #000;
  background-color: rgba(148, 63, 63, 0); font-size: 16px;
  font-weight: 600;
  text-decoration: none;
}

.nav-button:hover {
  color: #ca1c1c;
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
}

.right-hero-section-wrapper {
  width: 400px;
}
</style>

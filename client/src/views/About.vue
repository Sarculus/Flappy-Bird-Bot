<script setup lang="ts">

</script>

<template>
  <section class="hero-section">
    <div class="nav-wrapper">
      <img src="/flappy_bird.png" loading="lazy" alt="flappy bird icon" width="50" height="60">
      <div class="nav-buttons-wrapper">
        <router-link to="/" class="nav-button">Play</router-link>
        <router-link to="/about" class="nav-about-button">About</router-link>
      </div>
    </div>
    <div class="main-page-wrapper">
      <div class="hero-content-wrapper">
        <div class="left-hero-section-content">
          <h1 class="hero-title">Flappy Bird</h1>
          <p class="main-text">
            Flappy Bird is a mobile game developed by Vietnamese video game artist and programmer Dong Nguyen, under his game development company dotGears. The game is a side-scroller where the player controls a bird, attempting to fly between columns of green pipes without hitting them. Nguyen created the game over the period of several days, using a bird protagonist which he had designed for a cancelled game in 2012.
          </p>
        </div>
      </div>
<!--      <div class="main-section-wrapper">-->
<!--        <div class="left-hero-section-wrapper">-->
<!--          <div class="left-hero-section-content">-->
<!--&lt;!&ndash;            <h1 class="hero-title">Flappy Bird</h1>&ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="middle-hero-section-wrapper">-->
<!--          <div class="middle-hero-section-content">-->
<!--&lt;!&ndash;            <h1 class="hero-title">Flappy Bird</h1>&ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="right-hero-section-wrapper">-->
<!--          <div class="right-hero-section-content">-->
<!--&lt;!&ndash;            <h1 class="hero-title">Flappy Bird</h1>&ndash;&gt;-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
      <div class="bottom-content-wrapper">
<!--        <h1 class="hero-title">Flappy Bird</h1>-->
      </div>
    </div>
  </section>
</template>

<style scoped>
.main-section-wrapper {
  grid-column-gap: 0px;
  grid-row-gap: 0px;
  justify-content: space-between;
  padding: 0px;
  margin-top: 20px;
  display: flex;
}

.hero-content-wrapper {
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
}

.left-hero-section-wrapper {
  //width: 400px;
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
}

.middle-hero-section-wrapper {
  //width: 400px;
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
}

.right-hero-section-wrapper {
  //width: 400px;
  background-color: rgba(255, 255, 255, 0.47);
  border-radius: 30px;
}

.left-hero-section-content {
  padding: 20px;
}

.middle-hero-section-content {
  padding: 20px;
}

.right-hero-section-content {
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

.nav-about-button {
  color: #ffffff;
  background-color: rgba(148, 63, 63, 0); font-size: 16px;
  font-weight: 600;
  text-decoration: none;
}

.main-text{
  margin-left: 10px;
}

</style>

<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'

//GET REQUEST//
const testvalue = await getattractions()  //TODO: make vue work with await keyword (vue tutorial)
async function getattractions() {
  let myObject = await fetch("/api/testclass");
  //console.log(myObject)
  let myattractions = await myObject.json();
  console.log(myattractions)
  return myattractions
}
console.log(testvalue)

//POST REQUEST//
start_bot()  //TODO: make vue work with await keyword (vue tutorial)
async function start_bot() {
    const response = await fetch("/api/start_game_bot", {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
    })
    console.log(response.statusText)
}
</script>

<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />
  <Suspense>{{testvalue}}</Suspense>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

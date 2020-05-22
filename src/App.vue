<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import Calculator from './components/Calculator.vue'
/* eslint-disable */
export default {
  name: 'app',
  components: {
    Calculator
  }
}
</script>

<style>
#app {
  font-family: "Poppins";
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

body {
  overflow:hidden;
}
</style>

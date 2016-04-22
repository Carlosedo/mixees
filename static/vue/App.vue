<template>
  <div id="app">
    <!-- <div class="nav">
      <cocktails></cocktails>
    </div> -->
    <div class="main">
      <maker></maker>
    </div>
  </div>
</template>

<script>
var Hello = require('./components/Hello.vue');
var Cocktails = require('./components/Cocktails.vue');
var Maker = require('./components/Maker.vue');

export default {
  components: {
    Hello,
    Cocktails,
    Maker
  }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}

.nav {
    float: left;
}

.main {
    float: right;
    width: 100%;
}
</style>

<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>String: {{ string }}</p>
    <input v-model="msg">
    <button v-on:click="square">Square</button>
  </div>
</template>

<script>
var msg = 2
export default {
  data () {
    return {
      'msg': msg
    }
  },

  computed: {
    string: () => {
      return `this is an interpolation ${msg}`
    }
  },

  methods: {
    square: function () {
      this.msg = parseInt(this.msg, 10) * parseInt(this.msg, 10)
    }
  }
}
</script>

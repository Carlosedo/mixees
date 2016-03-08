<template>
  <div class="cocktails">
    <ul>
      <li v-for="cocktail in cocktails">
        {{ cocktail.node.title }}
      </li>
    </ul>
  </div>
</template>

<script>
var $ = require('jquery')

export default {
  data () {
    return {
      'cocktails': []
    }
  },

  created: function () {
    this.loadData()
  },

  methods: {
    loadData: function () {
      $.ajax({
        url: 'http://localhost:8000/graphql/',
        type: 'GET',
        crossDomain: true,
        data: {query: '{ allCocktails { edges { node { id, title } } } }'}
      }).done(data => {
        this.cocktails = data.data.allCocktails.edges
      })
    }
  }
}
</script>

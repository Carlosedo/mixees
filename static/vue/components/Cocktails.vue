<template>
  <div class="cocktails">
    <ul>
      <li v-for="cocktail in cocktails">
        {{ cocktail._source.title }}
      </li>
    </ul>
  </div>
</template>

<script>
var $ = require('jquery')

var elasticsearch = require('elasticsearch')
var es_client = new elasticsearch.Client({
  host: 'localhost:9200',
  log: 'trace'
})

export default {
  data () {
    return {
      'cocktails': []
    }
  },

  created: function () {
    this.loadESData()
  },

  methods: {
    loadESData: function () {
      es_client.search({
        index: 'cocktails',
        type: 'cocktail',
        ignore: [404]
      }).then( body => {
        this.cocktails = body.hits.hits
      }, error => {
        console.trace(error.message)
      })
    }
  }
}
</script>

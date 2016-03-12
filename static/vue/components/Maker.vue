<template>
  <div class="maker container">
    <a href="home.com" v-on:click.prevent="say('nah')">Go home</a>
    <div class="row">
      <div class="col-xs-3 ingredient__list">
        <div class="input-wrapper" v-for="spirit in spirits" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby">
          <input type="checkbox" v-bind:value="spirit.node.slug" v-model="selected_spirits">
          <label v-bind:for="spirit.node.slug">{{ spirit.node.name }}</label>
        </div>
      </div>

      <div id="glass" class="col-xs-6">
        <template v-for="item in selected_spirits">
          <div class="added {{ item }}"></div>
        </template>
        <template v-for="item in selected_mixers">
          <div class="added {{ item }}"></div>
        </template>
      </div>

      <div class="col-xs-3 ingredient__list">
        <div class="input-wrapper" v-for="mixer in mixers">
          <input type="checkbox" v-bind:value="mixer.node.slug" v-model="selected_mixers">
          <label v-bind:for="mixer.node.slug">{{ mixer.node.name }}</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var $ = require('jquery')

export default {
  data () {
    return {
      'spirits': [],
      'mixers': [],
      'added': [],
      'selected_spirits': [],
      'selected_mixers': []
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
        data: {query: `{
          allSpirits { edges { node { id, name, slug } } },
          allMixers { edges { node { id, name, slug } } }
        }`}
      }).done(data => {
        this.spirits = data.data.allSpirits.edges
        this.mixers = data.data.allMixers.edges
      })
    },

    say: function (msg) {
      alert(msg)
    },

    add_nearby: function (e) {
      $(e.target).prev('.input-wrapper').addClass('nearby')
      $(e.target).next('.input-wrapper').addClass('nearby')
    },

    remove_nearby: function (e) {
      $(e.target).prev('.input-wrapper').removeClass('nearby')
      $(e.target).next('.input-wrapper').removeClass('nearby')
    },

  }

}
</script>

<style lang="sass">
@import 'static/scss/bootstrap-custom';

#glass {
    height: 300px;
    width: 150px;
    background-color: grey;
}

.added {
  height: 30px;
}

/* Spirits */
.vodka {
    background-color: #E5E5E5;
}
.gin {
    background-color: #81C7F9;
}
.rum {
    background-color: #450F00;
}
.whiskey {
    background-color: #CD530D;
}
.tequila {
    background-color: #F3A000;
}
.cointreau {
    background-color: #C26114;
}

/* Mixers */
.orange {
    background-color: #F69800;
}
.coke {
    background-color: #211212;
}
.tonic {
    background-color: #CBC1AA;
}
.red-bull {
    background-color: #00009F;
}
.sweet-sour {
    background-color: #EDE564;
}

.ingredient__list div label {
  display: block;
  -webkit-transition: 0.15s linear;
}

.ingredient__list div:hover {
  margin-top: 9px; margin-bottom: 9px;
  z-index: 200;
}

.ingredient__list div:hover label {
  -webkit-transform-origin: center bottom;
  -webkit-transform: scale(1.5);
}

.ingredient__list div.nearby {
  margin-top: 6px; margin-bottom: 6px;
  z-index: 100;
}

.ingredient__list div.nearby label {
  -webkit-transform-origin: center bottom;
  -webkit-transform: scale(1.25);
}
</style>
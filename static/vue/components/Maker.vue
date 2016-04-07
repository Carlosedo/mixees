<template>
  <div class="maker container">
    <a href="home.com" v-on:click.prevent="say('nah')">Go home</a>
    <div class="row">
      <div class="col-xs-3 ingredient__list spirits">
        <div class="input-wrapper" v-for="spirit in spirits" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby">
          <input id="spirit-{{ $index }}" type="checkbox" v-bind:value="spirit.node.slug" v-model="selected_spirits">
          <label for="spirit-{{ $index }}">{{ spirit.node.name }}</label>
        </div>
      </div>

      <div class="col-xs-6">
        <div id="glass">
          <template v-for="item in selected_spirits">
            <div class="added {{ item }}"></div>
          </template>
          <template v-for="item in selected_mixers">
            <div class="added {{ item }}"></div>
          </template>
        </div>
      </div>

      <div class="col-xs-3 ingredient__list mixers">
        <div class="input-wrapper" v-for="mixer in mixers" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby">
          <input id="mixer-{{ $index }}" type="checkbox" v-bind:value="mixer.node.slug" v-model="selected_mixers">
          <label for="mixer-{{ $index }}">{{ mixer.node.name }}</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var $ = require('jquery')
var slugify = require('slugify');

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

        this.generateCSS()
      })
    },

    generateCSS: function() {
      let css_classes = ''

      for (let spirit of this.spirits) {
        let name = slugify(spirit.node.name).toLowerCase()

        let hex_values = '0123456789abcdef'
        let color = '#'

        for (var i = 0; i < 6; i++) {
          let randomIndex = Math.floor(Math.random() * hex_values.length)
          color += hex_values[randomIndex]
        }

        css_classes += '.' + name + '{background-color:' + color + ';} '
      }

      let style = document.createElement('style')
      style.type = 'text/css'
      style.innerHTML = css_classes

      document.getElementsByTagName('head')[0].appendChild(style);
    },

    say: function (msg) {
      alert(msg)
    },

    add_nearby: function (e) {
      $(e.currentTarget).prev('.input-wrapper').addClass('nearby')
      $(e.currentTarget).next('.input-wrapper').addClass('nearby')
    },

    remove_nearby: function (e) {
      $(e.currentTarget).prev('.input-wrapper').removeClass('nearby')
      $(e.currentTarget).next('.input-wrapper').removeClass('nearby')
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
    margin: 0 auto;
}

input[type="checkbox"] {
  display: none;
}

input[type="checkbox"]:checked + label {
  color: blue;
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
}

.ingredient__list div:hover {
  padding-top: 10px; padding-bottom: 9px;
  z-index: 200;
}

.ingredient__list div:hover {
  -webkit-transform-origin: left bottom;
}

.ingredient__list.spirits div:hover {
  -webkit-transform: scale(1.5) translate(15px, 0);
}

.ingredient__list.mixers div:hover {
  -webkit-transform: scale(1.5) translate(-15px, 0);
}

.ingredient__list div:hover label {
  margin-bottom: 0;
  color: #aaa;
}

.ingredient__list div.nearby {
  padding-top: 6px;
  padding-bottom: 6px;
  z-index: 100;
  -webkit-transform-origin: left bottom;
}

.ingredient__list.spirits div.nearby {
  -webkit-transform: scale(1.25) translate(10px, 0);
}

.ingredient__list.mixers div.nearby {
  -webkit-transform: scale(1.25) translate(-10px, 0);
}

.ingredient__list div.nearby label {
  color: #777;
}
</style>
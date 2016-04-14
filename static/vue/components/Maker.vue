<template>
  <div class="maker container">
    <div class="row">
      <div class="col-xs-3 ingredient__list spirits">
        <div class="input-wrapper" v-for="spirit in spirits" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby">
          <input id="spirit-{{ $index }}" type="checkbox" value="{{ spirit.node.slug }}" v-model="selected_spirits">
          <label for="spirit-{{ $index }}">{{ spirit.node.name }}</label>
        </div>
      </div>

      <div class="col-xs-6">
        <div id="glass-container">
          <div id="glass">
            <template v-for="item in selected_spirits">
              <div class="banner added">
                <div class="fill">
                    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="300px" height="300px" viewBox="0 0 300 300" enable-background="new 0 0 300 300" xml:space="preserve">
                      <path class="waveShape {{ item }}" d="M300,300V2.5c0,0-0.6-0.1-1.1-0.1c0,0-25.5-2.3-40.5-2.4c-15,0-40.6,2.4-40.6,2.4
                  c-12.3,1.1-30.3,1.8-31.9,1.9c-2-0.1-19.7-0.8-32-1.9c0,0-25.8-2.3-40.8-2.4c-15,0-40.8,2.4-40.8,2.4c-12.3,1.1-30.4,1.8-32,1.9
                  c-2-0.1-20-0.8-32.2-1.9c0,0-3.1-0.3-8.1-0.7V300H300z"/>
                    </svg>
                </div>
              </div>
            </template>
            <template v-for="item in selected_mixers">
              <div class="added {{ item }}"></div>
            </template>
            <div id="bottom"></div>
          </div>
        </div>
      </div>

      <div class="col-xs-3 ingredient__list mixers">
        <div class="input-wrapper" v-for="mixer in mixers" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby">
          <input id="mixer-{{ $index }}" type="checkbox" value="{{ mixer.node.slug }}" v-model="selected_mixers">
          <label for="mixer-{{ $index }}">{{ mixer.node.name }}</label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
var $ = require('jquery');
var slug = require('slug');
var unslug = require('unslug');

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
        let name = slug(spirit.node.name).toLowerCase()

        let hex_values = '0123456789abcdef'
        let color = '#'

        for (var i = 0; i < 6; i++) {
          let randomIndex = Math.floor(Math.random() * hex_values.length)
          color += hex_values[randomIndex]
        }

        css_classes += '.' + name + '{fill:' + color + ';} '
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

.mixers {
  text-align: right;
}

input[type="checkbox"] {
  display: none;
}

input[type="checkbox"]:checked + label {
  color: blue;
}

#glass-container {
  display: table;
  margin: 0 auto;
}

#glass {
  position: relative;
  display: table-cell;
  vertical-align: bottom;
  height: 300px;
  width: 150px;
  border-radius: 5px;
  border: 4px solid #999;
  border-top: 0px;
}

#bottom {
  height: 30px;
  width: 146px;
  border-radius: 3px;
  border-top: 4px solid #999;
  background-color: #eee;
  margin-top: 1px;
}

.added {
  height: 50px;
  border-radius: 3px;
  border: 1px solid white;
  p {
    text-shadow: -1px 0 #fff, 0 1px #fff, 1px 0 #fff, 0 -1px #fff;
  }
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
  margin-top: 10px;
  padding-bottom: 9px;
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

.banner {
  background: #fff;
  width: 146px;
  height: 50px;
  overflow: hidden;
  -webkit-backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
}
.banner .fill {
  -webkit-animation-name: fillAction;
  -webkit-animation-iteration-count: 1;
  -webkit-animation-timing-function: cubic-bezier(.2, .6, .8, .4);
  -webkit-animation-duration: 1s;
  -webkit-animation-fill-mode: forwards;
}
.banner .waveShape {
  -webkit-animation-name: waveAction;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-timing-function: linear;
  -webkit-animation-duration: 0.5s;
}
@-webkit-keyframes fillAction {
  0% {
      -webkit-transform: translate(0, 50px);
  }
  100% {
      -webkit-transform: translate(0, -5px);
  }
}
@-webkit-keyframes waveAction {
  0% {
      -webkit-transform: translate(-150px, 0);
  }
  100% {
      -webkit-transform: translate(0, 0);
  }
}

</style>
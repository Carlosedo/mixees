<template>
  <div id="maker" class="container">
    <div class="row">
      <div class="col-xs-3 ingredient-list spirits">
        <div class="ingredient-list__title">Select a Spirit</div>
        <div class="input-wrapper ingredient-list__item" v-for="spirit in spirits" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby" transition="fadeOut">
          <input id="spirit-{{ $index }}" type="checkbox" value="{{ spirit.node.slug }}" v-model="selected_spirits">
          <label for="spirit-{{ $index }}" class="cursor-pointer">
            <span class="label__text">{{ spirit.node.name }}</span>
             <span class="label__delete cursor-pointer">x</span>
          </label>
        </div>
      </div>

      <div class="col-xs-6">
        <div class="ingredient-search">
          <form>
            <input type="text" placeholder="Search for ingredients!"></input>
          </form>
        </div>
        <div id="glass-container">
          <div id="glass">
            <template v-for="item in reverse(selected_spirits)">
              <div class="banner added">
                <div class="fill">
                  <div class="drink-label">{{ item | unslug }}</div>
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

      <div class="col-xs-3 ingredient-list mixers">
        <div class="ingredient-list__title">Select a Mixer</div>
        <div class="input-wrapper ingredient-list__item" v-for="mixer in mixers" v-on:mouseover="add_nearby" v-on:mouseout="remove_nearby">
          <input id="mixer-{{ $index }}" type="checkbox" value="{{ mixer.node.slug }}" v-model="selected_mixers">
          <label for="mixer-{{ $index }}">{{ mixer.node.name }}</label>
        </div>
      </div>
    </div>
    <div class="row row-centered">
      <div class="col-xs-3 col-centered cocktail-list__button">
        <div v-if="selected_spirits.length == 0 && selected_mixers.length == 0 && num_found_cocktails == 0">
          <p>Come on! Ad some ingredients to start searching for cocktails!</p>
        </div>
        <div v-else>
          <p v-if="num_found_cocktails == 0">Oops! We couldn't find any cocktail with those ingredients</p>
          <button v-else v-on:click="goToCoktails" class="cocktail-list__button">Click here to see {{ num_found_cocktails }} cocktails!</button>
        </div>
      </div>
    </div>
  </div>
  <div id="cocktail-list" class="container">
    <div class="row">
      <a v-for="cocktail in found_cocktails" href="cocktails/{{ cocktail._source.title | slug }}">
        <div class="col-xs-3" style="background-color:grey;">
          <p>{{ cocktail._source.title }}</p>
          <img src="http://icons.iconarchive.com/icons/flameia/fruity-hearts/128/cocktail-icon.png" alt="cocktail">
        </div>
      </a>
    </div>
  </div>
</template>

<script>
var $ = require('jquery');
var slug = require('slug');
var unslug = require('unslug');
var elasticsearch = require('elasticsearch')

var es_client = new elasticsearch.Client({
  host: 'localhost:9200',
  log: 'trace'
})

export default {
  data () {
    return {
      'spirits': [],
      'mixers': [],
      'added': [],
      'selected_spirits': [],
      'selected_mixers': [],
      'found_cocktails': [],
      'num_found_cocktails': 0
    }
  },

  watch: {
    selected_spirits: function(val) {
      if (val.length > 5) {
        $('.ingredient-list.spirits label').removeClass("cursor-pointer");
        val.pop()
      } else if (val.length == 5) {
        $('.ingredient-list.spirits label').removeClass("cursor-pointer");
      } else {
        $('.ingredient-list.spirits label').addClass("cursor-pointer");
      }

      es_client.search({
        index: 'cocktails',
        type: 'cocktail',
        body: {
          query: {
            match_phrase: {
              ingredients: val.join(' ')
            }
          }
        },
        ignore: [404]
      }).then( body => {
        this.found_cocktails = body.hits.hits
        this.num_found_cocktails = this.found_cocktails.length
      }, error => {
        console.trace(error.message)
      })
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

    searchIngredient: function(text) {
      es_client.search({
        index: 'ingredients',
        type: 'ingredient',
        body: {
          query: {
            match: {
              name: text
            }
          }
        },
        ignore: [404]
      }).then( body => {
        debugger
      }, error => {
        console.trace(error.message)
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

    goToCoktails: function (event) {
      $('html,body').animate(
        {scrollTop: $("#cocktail-list").offset().top},
        'slow'
      );
    },

    reverse: function (a) {
      if (a.length > 1) {
        var temp = [];
        for (var i = (a.length - 1); i >= 0; i--) {
            temp.push(a[i]);
        }
        return temp;
      } else {
        return a;
      }
    },

    add_nearby: function (e) {
      $(e.currentTarget).prev('.input-wrapper').addClass('nearby')
      $(e.currentTarget).next('.input-wrapper').addClass('nearby')
    },

    remove_nearby: function (e) {
      $(e.currentTarget).prev('.input-wrapper').removeClass('nearby')
      $(e.currentTarget).next('.input-wrapper').removeClass('nearby')
    }
  },

  filters: {
    slug: function(text) {
      return slug(text.toLowerCase());
    },

    unslug: function(text) {
      return unslug(text);
    }
  }

}
</script>

<style lang="sass">
@import 'static/scss/maker';

/* MAIN LAYOUT */
#maker {
  min-height: 100vh;
}

#cocktail-list {
  min-height: 100vh;
}

/* GLASS */
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
  background: #fff;
  width: 146px;
  height: 50px;
  overflow: hidden;
  -webkit-backface-visibility: hidden;
  -webkit-transform: translate3d(0, 0, 0);
  border-radius: 3px;
  border: 1px solid white;
  p {
    text-shadow: -1px 0 #fff, 0 1px #fff, 1px 0 #fff, 0 -1px #fff;
  }
  & .fill {
    -webkit-animation-name: fillAction;
    -webkit-animation-iteration-count: 1;
    -webkit-animation-timing-function: cubic-bezier(.2, .6, .8, .4);
    -webkit-animation-duration: 1s;
    -webkit-animation-fill-mode: forwards;
  }
  & .waveShape {
    -webkit-animation-name: waveAction;
    -webkit-animation-iteration-count: infinite;
    -webkit-animation-timing-function: linear;
    -webkit-animation-duration: 0.5s;
  }
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

.drink-label {
  position: absolute;
  top: 20px;
  text-align: center;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 0 5px;
  color: #fff;
  text-shadow: -1px 0 #000, 0 1px #000, 1px 0 #000, 0 -1px #000;
}


/* INGREDIENT LIST */
.ingredient-search {
  text-align: center;
  margin-bottom: 20px;
}

.mixers {
  text-align: right;
}

.ingredient-list__item input[type="checkbox"] {
  display: none;
}

.ingredient-list__item input[type="checkbox"]:checked + label {
  & .label__text {
    background-color: #08FE66;
  }
  & .label__delete {
    display: inline;
    color: red;
  }
}

.ingredient-list {
  height: 410px;
}

.ingredient-list label {
  display: block;
  margin-bottom: 7px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  & .label__text {
    padding: 0 3px;
  }
  & .label__delete {
    display: none;
  }
}

.ingredient-list .input-wrapper:hover {
  margin-top: 10px;
  padding-bottom: 9px;
  z-index: 200;
  -webkit-transform-origin: left bottom;

  & label {
    margin-bottom: 0;
    color: $emperor;
  }
}

.ingredient-list div.nearby {
  padding-top: 6px;
  padding-bottom: 6px;
  z-index: 100;
  -webkit-transform-origin: left bottom;
  & label {
    color: $tundora;
  }
}

.ingredient-list.spirits {
  & div.nearby {
    -webkit-transform: scale(1.25) translate(10px, 0);
  }
  & .input-wrapper:hover {
    -webkit-transform: scale(1.5) translate(15px, 0);
  }
}

.ingredient-list.mixers {
  & div.nearby {
    -webkit-transform: scale(1.25) translate(-95px, 0);
  }
  & .input-wrapper:hover {
    -webkit-transform: scale(1.5) translate(-100px, 0);
  }
}

.cocktail-list__button {
  text-align: center;
}

/* INGREDIENT COLORS */
// Spirits
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

// Mixers
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

</style>
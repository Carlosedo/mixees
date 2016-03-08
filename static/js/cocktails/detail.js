$ = require('jquery');

function add_ingredient(total_parts, amount, ingredient) {
    var height = 210 * amount / total_parts;
    $('#drawing').append(
        '<div class="ingredient ' + ingredient +  '" style="height:' + height + 'px"> \
            <p class="ingredient-name">' + ingredient + '</p> \
        </div>'
    )
}

function draw_cocktail(total_parts, spirits, mixers) {
    for (var spirit in spirits) {
        if (spirits[spirit]['measurement'] == 4) {
            add_ingredient(
                total_parts,
                spirits[spirit]['amount'],
                spirits[spirit]['ingredient']
            )
        }
    }

    for (var mixer in mixers) {
        if (mixers[mixer]['measurement'] == 4) {
            add_ingredient(
                total_parts,
                mixers[mixer]['amount'],
                mixers[mixer]['ingredient']
            )
        }
    }
}

function bind_events() {
    $(".ingredient").hover(
        function() {
            $(".ingredient-name", this).show();
        },
        function () {
            $(".ingredient-name", this).hide();
        }
    );
}

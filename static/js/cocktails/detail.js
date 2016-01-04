function add_cocktail(amount, ingredient) {
    $('#drawing').append(
            '<div class="ingredient parts-'+ amount + ' ' + ingredient +  '"></div>'
        )
}

function draw_cocktail(spirits, mixers) {
    for (var spirit in spirits) {
        add_cocktail(spirits[spirit]['amount'], spirits[spirit]['ingredient'])
    }

    for (var mixer in mixers) {
        add_cocktail(mixers[mixer]['amount'], mixers[mixer]['ingredient'])
    }
}

function add_ingredient(total_parts, amount, ingredient) {
    var height = 210 * amount / total_parts;
    $('#drawing').append(
        '<div class="ingredient ' + ingredient +  '" style="height:' + height + 'px"> \
            <p class="ingredient-name">' + ingredient + '</p> \
        </div>'
    )
}

function draw_cocktail(total_parts, spirits) {
    for (var spirit in spirits) {
        add_ingredient(
            total_parts,
            spirits[spirit]['amount'],
            spirits[spirit]['ingredient']
        )
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


$('#likes').click(function(){
    var cocktail_id;
    cocktail_id = $(this).attr("data-cocktail-id");
    already_liked = $(this).attr("data-cocktail-liked");
    $.get(
        '/cocktails/like-cocktail/',
        {cocktail_id: cocktail_id, already_liked: already_liked},
        function(data_dict){
            $('#like_count').html(data_dict.likes);
            $('#likes').attr("data-cocktail-liked", data_dict.liked_by_user);

            if (data_dict.liked_by_user) {
                $('#likes').addClass('btn-danger');
            } else {
                $('#likes').removeClass('btn-danger');
            }
        }
    );
});

$(document).ready(function () {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val()
        $.ajax({
            url: '/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well games">
                                <a href="/games/${d.id}">
                                    <img class="card-img-top"><img  src ="${ d.image }" width=150 height=150>
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                             </div>`
                });
                $('games').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                // #TODO: Show toastr
                console.error(error);
            }
        })
    });

});
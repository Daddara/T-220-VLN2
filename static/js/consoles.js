$(document).ready(function () {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val()
        $.ajax({
            url: '/consoles?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="col-lg-4 col-md-6 mb-4">
                                <div class="card h-100">
                                <a href="/consoles/${d.id}">  
                                    <img class="card-img-top" src ="${ d.image }" width=150 height=150/>
                                    <h4>${d.name}</h4>  </a>
                             </div>`
                });
                $('#row-1').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        })
    });

});
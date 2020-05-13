$(document).ready(function () {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val()
        $.ajax({
            url: '/games?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="col-lg-4 col-md-6 mb-4">
                                <div class="card h-100">                   
                                 <a href="#" style="text-align: center"><img class="card-img-top"><img src ="${ d.image }" width=150 height=150</a>
                                 <div class="card-body">
                                    <h4 class="card-title">
                                        <a href="/consoles/${d.id}">${d.name}</a>
                                    </h4>
                                    <h5>$${d.price}</h5>
                                    </div>
                                    <div class="card-footer">
                                     <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small>
                                        </div>
                                        </div>
                                    
                                    
                             </div>`
                });
                $('#row-1').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                // #TODO: Show toastr
                console.error(error);
            }
        })
    });
    $('#sort-games').change(function(){
        const hs = this.value
        window.location = '/games?sort=' + hs
    });

});


$(document).ready(function() {
    $("#book").on('keyup change', function() {
        let input = $("#book").val();
        $.ajax({
            url: `/jsonResult?q=${input}`,
            success: data => {
                $(".row").empty();
                let array = data.items;
                console.log(array);
                for (let i = 0; i < array.length; i++) {
                    let title = array[i].volumeInfo.title || 'title isn\'t available 😢';
                    let subtitle = array[i].volumeInfo.subtitle || 'subtitle doesn\'t exist 😔';
                    let image = array[i].volumeInfo.imageLinks.thumbnail || 'we don\'t have the image';
                    $(".row").append(
                        `<div class="col">
                            <div class="card">
                                <img src="${image}" class="card-img-top imgs" alt="${title}-image">
                                <div class="card-body">
                                    <h5 class="card-title">${title}</h5>
                                    <p class="card-text">${subtitle}</p>
                                </div>
                            </div>
                        </div>`
                    );
                }
            }
        });
    });
});

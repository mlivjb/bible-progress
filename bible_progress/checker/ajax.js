$('chapter_read').on('submit', function (event) {
    event.preventDefault();
    $.ajax({
        url: '/submit/',
        type: 'POST',
        data: $(this).serialize(),
        success: function (data) {
            console.log(data);
        }
    });
});
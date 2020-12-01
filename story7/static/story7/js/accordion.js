$(document).ready(function () {
    $("#accordion")
        .accordion({
            header: "> div > h3",
            collapsible: true
        })
        .sortable({
            handle: "h3",
            placeholder: "ui-state-highlight",
            placeholder: "ui-state-highlight",
            over: function (event, ui) {
                $('#accordion').accordion({ active: false });
            },
            stop: function (event, ui) {
                // IE doesn't register the blur when sorting
                // so trigger focusout handlers to remove .ui-state-focus
                ui.item.children("h3").triggerHandler("focusout");

                $(this).accordion("refresh");
            }
        });

    $(".button-up").click(function(e) {
        const currentItem = $(this).parent().parent();
        currentItem.insertBefore(currentItem.prev())
        e.preventDefault();
        e.stopPropagation();
    });

    $(".button-down").click(function(e) {
        const currentItem = $(this).parent().parent();
        currentItem.insertAfter(currentItem.next())
        e.preventDefault();
        e.stopPropagation();
    });
});
var item = $('.my-name');

function cssStuff(){
    $(this).css({
        "color": "gray"
    });
}

$(document).ready(
    function(){
        $('.loading').remove();
    }
);

item.on({
    mouseenter : cssStuff,
    mouseleave : function(){
        $(this).css({
            "color": "#fff"
        })
    }
});

function dismiss(){
    $(".alert").addClass("hidden");
}
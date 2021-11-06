var item = $('.my-name');

function cssStuff(){
    $(this).css({
        "color": "white"
    });
}

$(document).ready(
    function(){
        $('#loading_wrap').remove();
});

item.on({
    mouseenter : cssStuff,
    mouseleave : function(){
        $(this).css({
            "color": "gray"
        })
    }
});
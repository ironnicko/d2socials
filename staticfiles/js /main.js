var item = $('.my-name');
var bac = $('body');
var change = {"background-image": "url('/srm2.jpg')"};
body.css(change)
item.on('click', function(){
    $(this).toggleClass('turnBlue');
})
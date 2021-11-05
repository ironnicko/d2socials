var item = document.querySelector(".my-name");
var body = document.querySelector("body");
body.style.backgroundImage = "/srm2.jpg";
item.addEventListener("moveover", function(){
    item.style.color = "red";
    item.style.fontSize = "2rem";
})
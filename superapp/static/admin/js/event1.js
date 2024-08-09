//profile acc

    var profile_acc1 =  document.getElementById("super_adm_event1")
    var profile_acc2 = document.getElementById("super_adm_event2")


    profile_acc1.addEventListener("click",function(){

        profile_acc2.classList.toggle("active")
    
    })

//navbtn

var navbtn = document.getElementById("super_adm_navbtn")
var btnpop = document.getElementById("super_admin_event1")


navbtn.addEventListener("click",function(){

    btnpop.classList.toggle("popups")
    navbtn.classList.toggle("popup")
      
})
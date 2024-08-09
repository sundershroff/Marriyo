	


// loading 

    let load1 = document.querySelector(".super_adm_load_percent1")

    let loadval1 = 0

    let loadval1end = 24

    let loadspeed1 = 30


    let loadprog1 = setInterval(()=>{
        loadval1++;

        load1.style.background = `#72C7D8`
        load1.style.width = `${loadval1}%`

        if(loadval1 == loadval1end){
            clearInterval(loadprog1)
        }
    },loadspeed1)



    let load2 = document.querySelector(".super_adm_load_percent2")

    let loadval2 = 0

    let loadval2end = 65

    let loadspeed2 = 30


    let loadprog2 = setInterval(()=>{
        loadval2++;

        load2.style.background = `#72C7D8`
        load2.style.width = `${loadval2}%`

        if(loadval2 == loadval2end){
            clearInterval(loadprog2)
        }
    },loadspeed2)



    let load3 = document.querySelector(".super_adm_load_percent3")

    let loadval3 = 0

    let loadval3end = 35

    let loadspeed3 = 30


    let loadprog3 = setInterval(()=>{
        loadval3++;

        load3.style.background = `#72C7D8`
        load3.style.width = `${loadval3}%`

        if(loadval3 == loadval3end){
            clearInterval(loadprog3)
        }
    },loadspeed3)



//profile acc

    var profile_acc1 =  document.getElementById("super_adm_event1")
    var profile_acc2 = document.getElementById("super_adm_event2")


    profile_acc1.addEventListener("click",function(){

        profile_acc2.classList.toggle("active")
    
    })

 // gender
    let progressbar = document.querySelector(".circle")
    let malevalue = document.querySelector(".maleper")
    let femalevalue = document.querySelector(".femaleper")


    let progressvalue  = 0
    
    let progressvalend = 35

    let speed1 = 50
    let progress = setInterval( ()=>{
        progressvalue++;
    
        progressbar.style.background = `conic-gradient(
        #FF8DDF ${progressvalue * 3.6}deg,
        #1D2182 ${progressvalue * 3.6}deg
        )`
        
        

        if(progressvalue == progressvalend){
            clearInterval(progress)
        }


    },speed1)

    let malval = 0
   
    let malvalend  = 65

    let speed2 = 10

    let genval1 = setInterval( ()=>{

        malval++;

        malevalue.textContent = `${malval}%`

        if(malval == malvalend){
            clearInterval(genval1)
        }

    },speed2)

    let fmalval = 0
   
    let fmalvalend  = 35

    let speed3 = 10

    let genval2 = setInterval( ()=>{

        fmalval++;

        femalevalue.textContent = `${fmalval}%`

        if(fmalval == fmalvalend){
            clearInterval(genval2)
        }

    },speed3)

//navbtn

var navbtn = document.getElementById("super_adm_navbtn")
var btnpop = document.getElementById("super_admin_event1")


navbtn.addEventListener("click",function(){

    btnpop.classList.toggle("popups")
    navbtn.classList.toggle("popup")
      
})
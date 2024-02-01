<template>
    <nav class="navbar">
 
 <!-- Image and text -->
 <div >
 <b-navbar variant="faded" type="light">
   <b-navbar-brand href="/">
   <div class="css-1kdt6ud">
   <!-- <img style="height: 24px;" src="/logo.png"> #3c2601 -->
   </div>
 
  <a  href="/" > 
     <p class="css-1ctifg4 " ><span style="color: #fcd535;">BIT</span>FRIENDLY</p>
     </a>
   </b-navbar-brand>
 </b-navbar>
 </div>
 <div>
 <button 
 class="toggle-button"
  data-bs-target="#collapseTarget" 
  data-bs-toggle="collapse">
  <span class="material-symbols-outlined">
density_medium
</span>
</button>
<div class="collapse py-2 justify-content-start text-start toggle-links" id="collapseTarget">
  <li ><a  href="/inscribe">Inscribe</a></li>
  <li><a href="#">Collections</a></li>
    <li><a href="/">Market</a></li>
      <li><a href="/wallet">Wallet</a></li>
</div>
</div>

   <div class="navbar-links">
 <ul class="nav-menu " >
   <li><a href="/inscribe">INSCRIBE</a></li>
   <li><a href="#">COLLECTIONS</a></li>
   <li><a href="/">MARKET</a></li>
 <li  >
 <a href="/wallet" >
   <button class="cut-edge" tabindex="0" type="button">
  
    <svg focusable="false" class="" data-icon="wallet" width="1em" height="1em" fill="currentColor" aria-hidden="true" viewBox="64 64 896 896">
                            <path
                                d="M880 112H144c-17.7 0-32 14.3-32 32v736c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V144c0-17.7-14.3-32-32-32zm-40 464H528V448h312v128zm0 264H184V184h656v200H496c-17.7 0-32 14.3-32 32v192c0 17.7 14.3 32 32 32h344v200zM580 512a40 40 0 1080 0 40 40 0 10-80 0z">
                            </path>
                        </svg>
  <p class="space">Wallet</p></button>

   </a>
   
</li>

</ul>
</div>

 </nav>
 <div class="hr1"></div>
</template>


<script>
  export default {
    data() {
      return {
        visible: false
      }
    }
  }
</script>

<style lang="scss" scoped>
  .navbar {
    display: flex;
    position: relative;
    justify-content: space-between;
    align-items: center;
    background-color: #2b3139 !important;
    color: white;
    //padding: 2px;
}

.brand-title {
    font-size: 1.1rem;
    margin: .5rem;
}

.navbar-links {
    height: 100%;
}
.space{
  padding: 4px;
  margin-top: 4px;

}

.navbar-links ul {
    display: flex;
    margin: 0;
    padding: 0;
}
a {
    text-decoration: none; /* Removes the underline */
  }

.toggle-links {
    padding: 2px;
    //background-color: #868387;
    color: white !important;
    font-display: 400;
    margin-top: 25px;
    list-style: none;
    display: none;
    right: 0;
    
}
.toggle-links li a{
  color: white !important;
  flex-direction: column;
  justify-content: space-between;
  right: 0;
  font-size:22px;
  text-align: left;
}

.navbar-links li {
    list-style: none;
}
.nav-menu.active {
  left: 0;
}


.navbar-links li a {
    display: block;
    text-decoration: none;
    color: white;
    padding: 1.8rem;
}

.navbar-links li:hover {
  padding: 3px;
    background-color: #523b52;
    border-radius: 15px;
    height: 5rem;
    
}

.toggle-button {
    position: absolute;
    top: .40rem;
    right: 2.2rem;
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 40px;
    height: 35px;
    //background-color: aliceblue;
    align-items: center;

}

.toggle-button .bar {
    height: 3px;
    width: 100%;
    border-radius: 15px;
    background-color: #fcd535;
    
}

@media (max-width: 1200px) {
    .navbar {
        flex-direction: column;
        align-items: flex-start;
    }

    .nav-menu{
      display: none;
    }

    .toggle-button {
        display: flex;
        margin-bottom: 20rem !important;
        padding-bottom: 23px;
        
        
    }
    .css-side{
      color: white !important;
    }


    .navbar-links {
        display: none;
        //width: 100%;
    }

    .navbar-links ul {
        width: 100%;
        flex-direction: column;
        
    }
    .toggle-links{
      display: flex;
      text-align: center;
      padding: .5rem 1rem;
      flex-direction: column;
      text-decoration: none;

    }

    .navbar-links ul li {
        text-align: center;
        text-decoration: none;
    }

    .navbar-links ul li a {
        padding: .5rem 1rem;
        
       
    }

    .navbar-links.active {
        display: none;
    }
}
.material-symbols-outlined {
  font-size: 2rem;
  margin-right: 12px;
  color: black;
  align-items: center;
  font-variation-settings:
  'FILL' 0,
  'wght' 700,
  'GRAD' 0,
  'opsz' 24,
 
}
.material-symbols-outlined-2 {
  font-size: 1.38rem;
  margin-right: 8px;
  color: bold black;
  font-variation-settings:
  'FILL' 0,
  'wght' 700,
  'GRAD' 0,
  'opsz' 24,
 
}
.cut-edge {
  position: sticky;
  top: -5px;
  text-overflow: ellipsis;
  white-space: nowrap;
  height: 40px;
  display: inline-flex;
  -moz-box-align: center;
  align-items: center;
  -moz-box-pack: center;
  justify-content: center;
  position: relative;
  box-sizing: border-box;
  outline: currentcolor none 0px;
  border: 0px none;
  cursor: pointer;
  user-select: none;
  vertical-align: middle;
  appearance: none;
  text-decoration: none;
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1.6rem;
  line-height: 1.27rem;
  letter-spacing: 0.02857em;
  text-transform: uppercase;
  min-width: 5rem;
  padding: 8px 8px ;
  border-radius: 5px;
  //transition: background-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, box-shadow 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, border-color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms, color 250ms cubic-bezier(0.4, 0, 0.2, 1) 0ms;
  // color: rgb(255, 255, 255);
  //background-color: rgb(250, 4, 211);
  //box-shadow: rgba(0, 0, 0, 0.2) 0px 3px 1px -2px, rgba(0, 0, 0, 0.14) 0px 2px 2px 0px, rgba(0, 0, 0, 0.12) 0px 1px 5px 0px;
  margin-left: -0px;
  margin-right: -15px;
  }

  .css-1kdt6ud{
    width: 35px;
    //height: 35px;
    border-radius: 18px;
    text-align: center;
    -moz-box-align: center;
    align-items: center;
    display: flex;
    -moz-box-pack: center;
    justify-content: center;
    background: #2b3139 none repeat scroll 0% 0%;
    overflow: hidden;
    //margin-right: 108px;
    padding: 2px;
  }

    
    


.css-1ctifg4  {
    margin: 0px;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    line-height: 20px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-weight: 900;
    letter-spacing: 0.2rem;
    font-size: 30px;
    cursor: pointer;
    color: white; 
    margin-left: 10px;
    margin-top: -35px;
    padding: 5px;
  
  }

.small-button.MuiButton-root {
  padding: 2px 8px;
  font-size: 12px;
  min-width: 30px;
}

.css-1r11lh4 {
  display: flex;
  place-items: center;
  cursor: pointer;
  padding: 16px;
  }

  .css-1i17ufj {
    display: inline-flex;
    -moz-box-align: center;
    align-items: center;
    -moz-box-pack: center;
    justify-content: center;
    box-sizing: border-box;
    background-color: transparent;
    outline: currentcolor none 0px;
    border: 0px none;
    margin: 0px;
    border-radius: 0px;
    cursor: pointer;
    user-select: none;
    vertical-align: middle;
    appearance: none;
    text-decoration: none;
    font-family: "Roboto", "Helvetica", "Arial", sans-serif;
    font-weight: 500;
    font-size: 0.875rem;
    line-height: 1.15;
    letter-spacing: 0.01857em;
    text-transform: uppercase;
    max-width: 360px;
    min-width: 90px;
    position: relative;
    min-height: 48px;
    flex-shrink: 0;
    padding: 11px 16px;
    overflow: hidden;
    white-space: normal;
    text-align: center;
    flex-direction: column;
    color: rgba(155, 155, 155, 0.7);
  }
.css-krltcp {
  max-width: 100%;
  display: flex;
  flex-wrap: wrap;
  -moz-box-align: center;
  align-items: center;
  gap: 10px;
  padding: 6px 11px 0px;
}
</style>
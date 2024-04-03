<template>
    <div class="full-css ">
      <button class="material-symbols-outlined button-45" @click="hide">
      arrow_back
      </button>
      <div class="content-container-234"  >
     <Content />
    </div>
    </div>
  </template>
  
  <script>
    import Content from "@/components/Content";

  export default {
    name: "DashboardSendBTC",
    components: {
    Content,
    },

    methods: {
      hide() {
        this.$emit('close');
      }
    }
  }
  </script>
  
  <style scoped>
 
  .full-css {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 50%;
    min-width: 50%;
    min-height: 95%;
    max-height: 100%;
    background-color: #231F20;
    padding-right: 20px;
     /* Ensure it's above other content */
    }

    .content-container-234 {
        margin-left: auto;
        margin-right: auto;
        padding: 20px ;
        padding-top: 5px;
        min-height: auto;
        max-width: 100%;
        font-weight: 63px;
        }
   
.material-symbols-outlined {
  position: fixed;
  top: 5%;
  left: 8%;
  transform: translate(-50%, -50%);
  color: #fff;
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 24
}

.button-45{
  background-color: transparent !important;
  border: none;
}


/* For devices smaller than 600px */
@media only screen and (max-width: 600px) {
  .full-css {
    /* Adjust the properties as needed for .full-css */
    
    min-width: 100%;
    min-height: 100%;
  }

  .content-container-234 {
    /* Adjust the properties as needed for .content-container-234 */
    max-width: 100%;
    min-width: 100%;
    font-size: 16px; /* Adjust font size as needed */
  }

  .material-symbols-outlined {
    /* Adjust the properties as needed for .material-symbols-outlined */
    max-width: 100%;
    min-width: 100%;
    font-size: 16px; /* Adjust font size as needed */
  }

  .button-45 {
    /* Adjust the properties as needed for .button-45 */
    max-width: 100%;
    min-width: auto;
    font-size: 16px; /* Adjust font size as needed */
  }
}

  </style>

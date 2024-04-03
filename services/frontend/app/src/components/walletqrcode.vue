<template>
    <!-- walletqrcode.vue template -->
 
    <div class="popup-234" v-if="modelValue">

       <!-- Your pop-up content goes here -->
    <div class="popup-content-23"  v-on:click="hide">
      <!-- <div v-if="walletInfo"> -->
    
   
        

<QRCodeVue3
       :width="200"
       :height="200"
       :value="taproot_address" 
       :qrOptions="{ typeNumber: 0, mode: 'Byte', errorCorrectionLevel: 'H' }"
       :imageOptions="{ hideBackgroundDots: true, imageSize: 0.4, margin: 0 }"
       :dotsOptions="{
         type: 'dots',
         color: '#26249a',
         gradient: {
           type: 'linear',
           rotation: 0,
           colorStops: [
             { offset: 0, color: '#26249a' },
             { offset: 1, color: '#26249a' },
           ],
         },
       }"
       :backgroundOptions="{ color: '#ffffff' }"
       :cornersSquareOptions="{ type: 'dot', color: '#000000' }"
       :cornersDotOptions="{ type: undefined, color: '#000000' }"
       fileExt="png"
       :download="false"
       myclass="my-qur"
       imgclass="img-qr"
       
     />

     
        <p class="button-400" id="address">{{ taproot_address }}</p>
        <button class="copy-button" @click="copyText('address')"><span class="material-symbols-outlined">
        content_copy
        </span></button>
      
    </div>
    <notifications  classes="my-custom-class" />
  </div>
  </template>
  <!-- broken add wine thing hazard rude net million remind script stereo height -->
  
  <script>
  import { ref, watch, onMounted, onUnmounted } from 'vue';
  import { useStore } from 'vuex';
  import { notify } from "@kyvg/vue3-notification";
  import QRCodeVue3 from "qrcode-vue3";

  export default {
    name: 'walletqrcode',
    props: { 
      modelValue: Boolean,
    },
    setup(props, { emit }) {
      const store = useStore();
      const taproot_address = ref('');
      let clickOutsideEvent;

      onMounted(() => {
        taproot_address.value = store.state.taproot_address;
        // clickOutsideEvent = window.addEventListener('click', handleClickOutside);
      });

      watch(() => props.modelValue, (newValue) => {
        if (!newValue) {
          closePopup();
        }
      });

      const closePopup = () => {
        emit('update:modelValue', false);
      };

      const copyText = (id) => {
        const textToCopy = document.getElementById(id).innerText;
        navigator.clipboard.writeText(textToCopy).then(() => {
          console.log("Copied to clipboard: " + textToCopy);
          notify({ type: "Important message", text: 'Wallet Copied!' });
        }, (error) => {
          console.error('Could not copy text: ', error);
          notify({ type: 'error', text: 'Failed to copy text!' });
        });
      };
      return { 
        closePopup,
        copyText,
      };
    },
    computed: {
      taproot_address() {
        let address = this.$store.state.taproot_address;
        return address;
      },
      
    },
    components: {
      QRCodeVue3
    },
    methods: {
      hide() {
            console.log('click registered');
            this.$emit('close')
        }}
  };
</script>



<style scoped>


.my-custom-class {
      background: #123456 !important;
      font-size: 15px;
      max-width: 10px;
      min-width: 10px;
      min-height: 5px;
    }


@media (min-width:320px) { /* smartphones, iPhone, portrait 480x320 phones */
  .popup-234 {
        position: absolute;
        text-align: center;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        background-color: #2b3139 !important;
      }

      .popup-content-23 {
        background-color: #2b3139 !important;
        position: absolute;
        max-width: 100px; /* Increase the max-width */
        min-width: 300px; /* Increase the min-width */
        height: 300px;
        font-size: 24px; /* Increase the font-size */
        padding: 40px; /* Increase the padding */
        color: #EDEAE0;
        align-items: center;
        text-align: center;
        border-radius: 15px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: 500;
    }
    .copy-button{
        top: 80%;
        left: 88%;
        transform: translate(-50%, -50%);
        position: absolute;
        background-color: #2b3139;
        color: white;
        border: none;
        cursor: pointer;
        max-width: 50px; /* Increase the max-width */
        min-width: 30px; /* Increase the min-width */

      }


.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 24
}



.copy-button:hover {
  background-color: #123456;
}

.button-400 {
      position: absolute;
      border-radius: 5px;
      background-color: none;
      padding-right: 5px;
      color: white;
      max-width: 100px;
      min-width: 180px;
      text-align: center;
      border: none;
      height: 45px;
      font-size: 15px;
      top: 88%;
      left: 50%;
      transform: translateX(-50%);
      overflow: hidden; /* Hide overflow content */
    }


}
@media (min-width:1281px) { /* hi-res laptops and desktops */

  .alerts {
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background-color: rgba(0, 0, 0, 0.5);
      color: white;
      padding: 10px 20px;
      border-radius: 5px;
      z-index: 9999;
    }


  .button-400 {
      position: absolute;
      border-radius: 5px;
      background-color: none;
      padding-right: 5px;
      color: white;
      max-width: 100px;
      min-width: 180px;
      text-align: center;
      border: none;
      height: 45px;
      font-size: 15px;
      top: 88%;
      left: 50%;
      transform: translateX(-50%);
      overflow: hidden; /* Hide overflow content */
    }


  .popup-234 {
        position: absolute;
        text-align: center;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        padding: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        background-color: #2b3139 !important;
      }

      .popup-content-23 {
        background-color: #2b3139 !important;
        position: absolute;
        max-width: 100px; /* Increase the max-width */
        min-width: 300px; /* Increase the min-width */
        height: 300px;
        font-size: 24px; /* Increase the font-size */
        padding: 40px; /* Increase the padding */
        color: #EDEAE0;
        align-items: center;
        text-align: center;
        border-radius: 15px;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: 500;
    }
  .copy-button{
    top: 80%;
    left: 88%;
    transform: translate(-50%, -50%);
    position: absolute;
    background-color: #2b3139;
    color: white;
    border: none;
    cursor: pointer;
    max-width: 50px; /* Increase the max-width */
    min-width: 30px; /* Increase the min-width */

  }


.material-symbols-outlined {
  font-variation-settings:
  'FILL' 0,
  'wght' 400,
  'GRAD' 0,
  'opsz' 24
}



.copy-button:hover {
  background-color: #123456;
}



}


</style>
  
  


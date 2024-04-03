<template>
  <div class="secret-phrase-container" >
    <div class="phrase-container">
  <div v-for="(word, index) in phrase" :key="index" class="phrase-box">
    <span class="number">{{ sequence[index] }}</span>
    <!-- <span class="number">{{ index + 1 }}</span> -->
    <span class="dotcss">&bull;</span>
    <span  class="word" > {{ word }}</span>
</div>
</div>


   
    <!-- <p>Phrase: {{ phrase }}</p> -->
  </div>
  <!-- <span class="material-symbols-outlined">
      arrow_forward_ios
</span> -->
  <div class="subtitleClick"> Naver Share Your Secret Phrase With Anyone And Store It Secrely </div>
  <button style="background-color: transparent; border: none; padding: 29px;"  @click="showPopup()"><span class="material-symbols-outlined">
      arrow_forward_ios
</span></button>


<div v-if="popupVisible" class="popup" @click="closePopup">
<!-- Use v-model to control the pop-up visibility -->
<PopUp v-model="popupVisible" ref="popup">
  <!-- Your pop-up content goes here -->
  <p>This is a pop-up!</p>
</PopUp>
</div>
</template>

<script>
import PopUp from '../components/PopUp.vue'; // Adjust the path based on your project structure
import { ref } from 'vue';
import { Modal } from 'usemodal-vue3';

let isVisible = ref(false);

export default {
  components: {
    PopUp,
  },
  data() {
    return {
      error: '',
      phrase: ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10', 'word11', 'word12'], // Your list of words
      sequence: [], // This will be filled with the sequence from your function
      popupVisible: false,
      
    };
  },
  computed: {

    phrase() {
      return this.$store.state.phrase;
    },
   
  },
  mounted() {
    this.sequence = this.sequenceFunction(); // Call your sequence function to populate the sequence array
  },
 
  methods: {
    sequenceFunction() {
      let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
      return arr;
    },
    
    // Add other methods if needed
    showPopup() {
      // Set isVisible to true to show the pop-up
      // this.$refs.popup.isVisible = true;
      this.popupVisible = true;
    },
    closePopup() {
      this.popupVisible = false;

      // Remove the click event listener when closing the popup
      document.removeEventListener('click', this.closePopupOutside);
    },
    closePopupOutside(event) {
      // Check if the clicked element is outside the popup
      const popupElement = this.$refs.popup; // Adjust ref name if necessary

      if (popupElement && !popupElement.contains(event.target)) {
        this.closePopup();
      
      }}
  },
  // Add other component options if needed
};

</script>

<style lang="scss">





@media (min-width:320px) { /* smartphones, iPhone, portrait 480x320 phones */

.secret-phrase-container{
            position: absolute;
            max-width: 200px;
            font-size: 1.8rem;
            //background-color: rgba(21, 30, 61, 0.5); /* Faded version of #151e3d with 50% opacity */
            color: #EDEAE0;
            align-items: center;
            text-align: center;
            top: 40%;
            min-width: 58.5%;
            font-weight: 600;
            min-height: 200px;
            margin: auto;
            left: 50%;
            transform: translate(-50%, -50%);

          }


    .subtitleClick {
          position: absolute;
          max-width: 300%;
          font-size: 15px;
          //background-color: #ffff;
          color: rgb(190, 205, 50);
          text-align: center;
          border-radius: 15px;
          top: 82%;
          left: 50%;
          transform: translate(-50%, -50%);
          font-weight: 700;
        } 
        
        

.phrase-container {
    display: flex;
    flex-wrap: wrap;
    gap: 15px; /* Adjust the gap between boxes */
  }

  .material-symbols-outlined {
    position: absolute;
    max-width: 20%;
    font-size: 2px;
    top: 88%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-variation-settings:
    'FILL' 0,
    'wght' 500,
    'GRAD' 0,
    'opsz' 24,
  }

  .phrase-box {
    display: flex;
    align-items: center;
    padding: 5px 10px;
    // border: 1px solid #ccc;
    border-radius: 5px;
  }

  .number {
    margin-right: 1px;
    font-weight: bold;
  }

  .word {
    flex: 5;
    padding: 10px;
  }

  .dotcss {
              display: inline-block;
              vertical-align: middle;
              line-height: 0.5em;
              margin-right: 5px; /* Optional: Add some space between text and bullet */
              position: relative;
              top: 0.2em; /* Adjust the value to move the bullet down further */
          }
}

@media (min-width:1281px) { /* hi-res laptops and desktops */
  .subtitleClick {
          position: absolute;
          max-width: 200%;
          font-size: 18px;
          color: rgb(190, 205, 50);
          text-align: center;
          border-radius: 15px;
          top: 80%;
          left: 50%;
          transform: translate(-50%, -50%);
          font-weight: 700;
          }

  .phrase-container {
      display: flex;
      flex-wrap: wrap;
      gap: 15px; /* Adjust the gap between boxes */
    }

  .material-symbols-outlined {
    position: absolute;
    max-width: 20%;
    font-size: 2px;
    top: 80%;
    left: 68%;
    transform: translate(-50%, -50%);
    font-variation-settings:
    'FILL' 0,
    'wght' 500,
    'GRAD' 0,
    'opsz' 24,
  }


  .phrase-box {
    display: flex;
    align-items: center;
    padding: 5px 10px;
    // border: 1px solid #ccc;
    border-radius: 5px;
  }

  .number {
    margin-right: 1px;
    font-weight: bold;
  }

  .word {
    flex: 5;
    padding: 10px;
  }

  .dotcss {
              display: inline-block;
              vertical-align: middle;
              line-height: 0.5em;
              margin-right: 5px; /* Optional: Add some space between text and bullet */
              position: relative;
              top: 0.2em; /* Adjust the value to move the bullet down further */
          }

    .secret-phrase-container {
                position: absolute;
                max-width: 20vw;
                width: 20vw; /* Set the width to 30% of the viewport width */
                font-size: 1.8rem;
                //height: 36vw;
                //background-color: rgba(21, 30, 61, 0.5); /* Faded version of #151e3d with 50% opacity */
                color: #EDEAE0;
                align-items: center;
                text-align: center;
                top: 50%;
                font-weight: 600;
                margin: auto;
                left: 50%;
                transform: translate(-50%, -50%);
            }

}

</style>

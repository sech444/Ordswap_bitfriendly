<template>
  <div>
    <h3 class="section-title">Network Fee</h3>
    <div>
      <div class="container">
        <input type="radio" id="slow" name="networkFee" class="column-radio" v-model="selectedFee" value="slow" @change="gas_fee()">
        <label for="slow" class="column"><span class="slow-css">Slow</span> {{ slow }} <br>Multiple days </label>

        <input type="radio" id="normal" name="networkFee" class="column-radio" v-model="selectedFee" value="normal" @change="gas_fee()">
        <label for="normal" class="column"><span class="Economy-css">Economy</span> {{ normal }} <br> 1 hour</label>

        <input type="radio" id="fast" name="networkFee" class="column-radio" v-model="selectedFee" value="fast" @change="gas_fee()">
        <label for="fast" class="column"><span class="fast-css">Fast <br></span> {{ fast }}<br> 30 minutes</label>

        <div v-if="selectedFee === 'custom'">
          <label for="customFee">Custom Fee (sat/vB):</label>
          <input type="number" id="customFee" v-model="customFee" @change="gas_fee()">
        </div>

        <input type="radio" id="custom" name="networkFee" class="column-radio" v-model="selectedFee" value="custom" @change="gas_fee()">
        <label for="custom" class="column">Custom Choose Fee</label>
      </div>
    </div>
  </div>
</template>


<script>
import { computed } from 'vue';
import axios from 'axios';

export default {
  name: "PriceTrackerWidget",
  data() {
    return {
      slow: null,
      normal: null,
      fast: null,
      selectedFee: null,
      customFee: null // Initialize customFee as null
    };
  },
  created() {
    this.create_gas_fee();
    setInterval(this.create_gas_fee, 60000); // Reload every 1 min
    this.gas_fee(); // Call gas_fee() to set the initial value
  },
  provide() {
    return {
      gasFee: computed(() => this.gas_fee()), // Reactive computed property
    };
  },
  methods: {
    create_gas_fee() {
      const api = axios.create({
        baseURL: 'http://127.0.0.1:5000',  // Update with your FastAPI backend address
      });

      api.get('/estimates_gas_free')
        .then(response => {
          console.log(response.data); // Inspect the response structure
          // Check if 'fast' property exists and has a valid value
          this.fast = response.data.fast;
          this.normal = response.data.normal;
          this.slow = response.data.slow;
          this.selectedFee = 'normal'; // Set a default value
        })
        .catch(error => {
          console.error('Error fetching gas fee:', error);
          // Handle API errors (e.g., display an error message)
        });
    },


gas_fee() {
  let feeValue ; // Variable to hold the value you'll emit

  switch (this.selectedFee) { // Consider using a switch for clearer logic
    case 'slow':
      feeValue = this.slow; 
      break;
    case 'normal':
      feeValue = this.normal; 
      break;
    case 'fast':
      feeValue = this.fast;
      break;
    case 'custom':
      feeValue = this.customFee ; 
      break; 
    default: 
      feeValue = this.normal; 
  }

  this.$emit('feeSelected', feeValue); // Emit the event
}


  }
};
</script>




<style lang="scss" scoped>
/* Your existing styles */
.price-container {
  max-width: 30vw;
  top: 15px;
}

.price-text {
  margin: 3rem 0.4rem;
  font-size: 2rem;
  justify-content: space-between;
  display: flex;
  color: #74cab3;
}

.slow-css {
  font-size: 1.4vw;
  padding: 55px;
}

.fast-css {
  font-size: 1.6vw;
  word-spacing: 12px;
  padding: 20px;
  text-align: center;
}

.Economy-css {
  font-size: 1.4vw;
  padding: 10px;
}

.column {
  flex: 1;
  padding: 20px;
  margin: 8px;
  color: #fff;
  font-size: 1vw;
  background-color: #231F20;
  border: 2px solid #ccc;
  cursor: pointer;
  text-align: center;
  min-height: 7.6vw;
  min-width: 9.5vw;
  border-radius: 15px;
  top: 35%;
}

.column-radio {
  display: none; /* Hide the radio buttons */
}

.column-radio:checked + label {
  background-color: #F7931A; /* Change background color when selected */
}

.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  max-height: 45rem;
  top: 70%;
}
.section-title{
  display: flex;
  text-align: left;
  padding-left: 10px;
}


/* Your original CSS code here... */

/* For devices smaller than 600px */
@media only screen and (max-width: 600px) {
  .price-container {
  max-width: 30vw;
  top: 15px;
}

.price-text {
  margin: 3rem 0.4rem;
  font-size: 2rem;
  justify-content: space-between;
  display: flex;
  color: #74cab3;
}

.slow-css {
  font-size: 4vw;
  padding-left: 15px;
  justify-content: center
}

.fast-css {
  font-size: 4vw;
  word-spacing: 12px;
  // padding: 20px;
  justify-content: center
}

.Economy-css {
  font-size: 4vw;
  // padding: 10px;
  justify-content: center
}

.column {
  flex: 1;
  padding: 5px;
  margin: 8px;
  color: #fff;
  font-size: 3vw;
  background-color: #231F20;
  border: 2px solid #ccc;
  cursor: pointer;
  text-align: center;
  min-height: 25.6vw;
  min-width: 20.5vw;
  border-radius: 15px;
  top: 30%;
  align-items: center
}

.column-radio {
  display: none; /* Hide the radio buttons */
}

.column-radio:checked + label {
  background-color: #F7931A; /* Change background color when selected */
}

.container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  max-height: 55rem;
  top: 70%;
  overflow: auto; 
  scrollbar-color: solid #ccc;
}
.section-title{
  display: flex;
  text-align: left;
  padding-left: 10px;
}

}

</style>


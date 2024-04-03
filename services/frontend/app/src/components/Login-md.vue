<!-- Login.vue -->
<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="submitForm">
        <label for="bitcoinAddress">Bitcoin Wallet Address:</label>
        <input
          type="text"
          id="bitcoinAddress"
          v-model="bitcoinAddress"
          placeholder="Enter your Bitcoin address"
          required
        />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        bitcoinAddress: "",
      };
    },
    methods: {
      submitForm() {
        this.$emit("login", this.bitcoinAddress);
      },
    },
  };
  </script>
  
<template>
    <div>
      <h2>Welcome to the Dashboard</h2>
      <p>User: {{ userAddress }}</p>
      <button @click="$emit('logout')">Logout</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      userAddress: String,
    },
  };
  </script>
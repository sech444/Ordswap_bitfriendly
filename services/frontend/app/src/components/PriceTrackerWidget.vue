<template>
  <div class="price-container">
    <h3 class="section-title">Current BTC Price</h3>
    <div class="price-text">
      <span>BTC/USD: </span>
      <span>{{price}}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "PriceTrackerWidget",
  computed: {
    price() {
      return this.$store.state.btcPrice.toFixed(2);
    }
  }
};
</script>

<style lang="scss" scoped>

.price-container {
  max-width: 30vw;
}

.price-text {
  margin: 3rem 0.4rem;
  font-size: 2rem;
  justify-content: space-between;
  display: flex;
  color: #74cab3;

}

@media only screen and (max-width: 768px) {
  .price-container {
    max-width: 80vw;
  }
}
</style>


<template>
  <div class="app-header">
    <div class="content-container" style="background-color: #2b3139;">
      <div class="row">
        <div class="content-block">
          <h1 class="logo-text bold">
            <a href="/">
              <span class="green-text">BIT</span>FRIENDLY Wallet
              <span class="green-text">UI</span>
            </a>
          </h1>
          <p class="header-wallet-text">
            <span class="green-text">Wallet address: </span
            ><span class="bold">{{ taproot_address }}</span>
          </p>
        </div>
      </div>
      <div class="d-grid gap-2 d-md-flex justify-content-md-end">
  <button class="btn btn-outline-secondary bold" type="button"  style="color: #ffd700;">Market</button>
  <button class="btn btn-outline-secondary bold" type="button"  style="color: #ffd700;">Inscribe</button>
  <button class="btn btn-outline-secondary bold" type="button"  style="color: #ffd700;">Private Key</button>
</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Headerbtc",
  computed: {
    taproot_address() {
      return this.$store.state.taproot_address;
    },
    private_key() {
      return this.$store.state.private_key;
    }
  }
};
</script>

<style lang="scss" scoped>
.green-text {
  color: #ffd700;
}
.header-wallet-text {
  color: #eaecef;
  font-weight: 300;
  margin-top: -90px;
  position: absolute;
  right: 6.23rem;
  padding-block-end: 10%;
  font-size: 18px;
}
.header-wallet {
  color: #fff;
  font-weight: 300;
  position: absolute;
  right: 9.23rem;
  padding-bottom: 45px;
}

a {
  text-decoration: none;
  color: inherit;
}
.content-block {
  padding-bottom: 12px;
}

.bold {
  font-weight: 600;
}

.app-header {
  
  min-height: 64px;
  width: 100%;
  padding: 20px;
  padding-bottom: 60px;
  border-radius: 35px;
  z-index: 2; // Set a higher z-index value
}

.logo-text {
  color: #ffffff;
  word-spacing: 12px;
  position: relative;
  top: -20px;
  
}

@media only screen and (max-width: 1700px) {
  // .app-header {
  //   padding-bottom: 50px;
  //   margin-bottom: 330px;
  //   float: top;
  // }
  .logo-text{
    font-size: 25px;
    padding: 12px;
    //padding-bottom: 50px;
  }

  .header-wallet-text {
    right: 2.23rem;
    display: none;
  }

  .header-wallet {
    right: 5.23rem;

  }
  .header-wallet-text {
  color: #eaecef;
  font-weight: 300;
  margin-top: -4rem;
  position: absolute;
  right: 4.23rem;
  padding-block-end: 10%;
  font-size: 18px;
  padding-left: 35px;
  padding-bottom: 50px;
}
}

</style>

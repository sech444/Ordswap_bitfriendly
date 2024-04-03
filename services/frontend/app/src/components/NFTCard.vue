<template>
  <div class="my-rows">
    <div class="card mb-3"  style="width: 18rem; height: 20rem; background-color: #s; padding: 12;">
      <div class="card__product-img" >
        <img 
          class="card__img"      alt="product-image" 
          :src="card?.img"
        >
      </div>
      <div class="card__content" >
        <p class="card__name">{{ name }} <span v-if="id">#{{ id }}</span></p>
        <!-- <p class="card__description" v-if="description">{{ description }}</p> -->
        <div class="card__content-bottom" >
          <div class="card__price">
            <div class="icon">
              <img src="@/assets/images/nft-card/icon-ethereum.svg" alt="">
            </div>
            <p>{{ price }} BTC</p>
          </div>
          <div v-if="time" class="card__time">
            <div class="icon">
              <img src="../assets/icons8-bitcoin-48.png" alt="">
            </div>
            <p>{{ time }} days left</p>
          </div>
        </div>
      </div>
      <!-- <div class="card__footer" >
        <div class="card__avatar">
          <img :src="require('@/static/images/' + avatar)" alt="avatar-image">
        </div>
        <p class="card__autor">Creation of <span class="card__autor--alt-color">{{ autor }}</span></p>
      </div> -->
    </div>

  </div>
  </template>
  
  <script>
  
  export default {
    props: {
      card: Object, // Or the appropriate type
      img: {
        type: String,
        default: '',
        required: true
      },
      name: {
        type: String,
        default: '',
        required: true
      },
      description: {
        type: String,
        default: ''
      },
      id: {
        type: [String, Number],
        default: null
      },
      price: {
        type: Number,
        default: 0,
        required: true
      },
      time: {
        type: [String, Number],
        default: ''
      },
    },

    
  }
  </script>
  
  <style scoped lang="scss">
  .icon {
    display: flex;
    @media screen and (min-width: 526px) {
      margin-left: 5px;
  }}

  .card-egde{
    box-sizing: border-box;
  display: flex;
  justify-content: center;
  margin-top: 20px;
  padding: 15px;
  //margin-bottom: 2px;
  // width: 18rem;
  // height: 30rem;
  // vertical-align: middle;
  @media screen and (min-width: 526px) {
      margin-top: 52px;
  }}
  .card {
  background-color: #15263F;
  color: rgb(250, 4, 211);
  border-radius: 16px;
  padding: 2px;
  width: 27px;
  height: 32rem;
  margin: 12px ;
  margin-top: 12px;
  font-size: 0.5rem;
  box-shadow: 0 25px 50px 0 rgba(0,0,0,0.1);
  @media screen and (min-width: 526px) {
    font-size: 1.6rem;
    width: 350px;
    padding-bottom: 32px;
    display: flex;
    justify-content: center;
  }
  .card__product-img {
    cursor: pointer;
    position: relative;
    border-radius: 2px;
    overflow: hidden;
    max-width: 30rem;
    @mixin hoverOpacity {
      content: "";
      position: absolute;
      left: 0;
      width: 100%;
      height: 100%;
      opacity: 0;
      transition: opacity 0.25s ease-out;
    }
    &::after {
      @include hoverOpacity;
      background: no-repeat rgba(0, 255, 255, 0.5) url(../assets/images/nft-card/icon-view.svg) center;
    }
    &:hover {
      &::after {
        opacity: 1;
      }
    }
  }
  .card__content {
    display: flex;
    flex-direction: column;
    gap: -102px;
    padding: 2px 0 6px 0;
    @media screen and (min-width: 526px) {
      gap: 16px;
      padding: 4px 2px;
    }
    .card__name {
      color: rgb(250, 4, 211);
      font-size: 1.8rem;
      font-weight: bold;
      cursor: pointer;
      &:hover {
        color: #00FFF8;
      }
    }
    .card__description {
      font-size: 1.4rem;
      line-height: 1.6rem;
      font-weight: lighter;
    }
    .card__content-bottom {
      display: flex;
      justify-content: space-between;
      padding-top: 4px;
      @media screen and (min-width: 562px) {
      padding-top: 16px;
      }
      > * {
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 600;
      }
      .card__price {
        color: #00FFF8;
        @media screen and (min-width: 526px) {
        padding-top: 12px;
        font-size:large;
      }
      }
    }
  }
  
}

//Transition
.fade-enter-active,
.fade-leave-active {
    transition: 0.25s ease-out;
}
.fade-leave-to,
.fade-enter-from {
  opacity: 0;
}
  </style>
<template>
  <div>
    <top-header></top-header>
    <TopMD></TopMD>

    <!-- <div >
    <LoginMD v-if="!isLoggedIn" @login="login" />
    <Dashboard v-else @logout="logout" :userAddress="userAddress" />
  </div> -->

    <b-pagination
      v-model="currentPage"
      :total-rows="list.length"
      :per-page="perPage"
      class="mb-3"
    ></b-pagination>

    <!-- <div class="my-rows">
      <NFTCard
        v-for="card in paginatedList"
        :key="card.id"
        :card="card"
        :img="imageSrc"
        :name="card.name"
        :id="card.title"
        :price="card.price"
        :time="card.time"
      ></NFTCard>
    </div>
    <div class="inscription-grid"></div>
      {{inscriptionGrid}}
     <img :src="imageSrc" /> 
     {{perview}} -->
    <div style="align-items:center">
      <Footer></Footer>
    </div>
  </div>
  
</template>



<script>
import JobCard from "@/components/JobCard.vue";
import NFTCard from "@/components/NFTCard.vue";
import TopHeader from "@/components/top-header.vue";
import TopMD from "@/components/top-md.vue";
import axios from 'axios';
import { ref } from 'vue';
import Footer from "@/components/Footer.vue";
import LoginMD from "@/components/Login-md.vue";
import Dashboard from "@/components/Dashboard.vue";



export default {
  name: 'Login',
  components: {
    //BPagination,
    NFTCard,
    TopHeader,
    JobCard,
    TopMD,
    Footer,
    Dashboard,
    LoginMD
  },
  data: () => ({
    list: [],
    inscriptionGrid: ref(null),
    currentPage: 1,
    perPage: 60,
    imageData: null,
    imageUrl: ref(null),
    perview: ref(null),
    isLoggedIn: false,
    userAddress: null,
  }),
  computed: {
    paginatedList() {
      // Your computed properties here
      const start = (this.currentPage - 1) * this.perPage;
      const end = start + this.perPage;
      return this.list.slice(start, end);
    },
  },
  async mounted() {
    try {
      // Fetch the list of inscriptions from the Ordapi API.
      let inscriptions = await axios.get("https://ordapi.xyz/feed");
      this.list = inscriptions.data?.rss?.channel?.item || [];
      let imageUrl = "https://ordinals.com/content/${list.link}";
      this.imageSrc = imageUrl;
    } catch (error) {
      console.error('API Request Error:', error.message);
    }
    try {
      //Fetch the list of inscriptions from the Ordapi API.
      let inscriptions = await axios.get("https://ordapi.xyz/feed");
      //this.list = inscriptions.data?.rss?.channel?.item || [];
      
    } catch (error) {
      console.error('API Request Error:', error.message);
    }
    
    
    try {
      // Fetch the list of inscriptions from the Ordapi API.
      let response = await axios.get("https://ordinals.com/content/7aa65adc99537fd5237d705c30bcdbcd7d9ab2e28747670caee0fb74410bfdc4i0");
  this.perview = response.data;
  
  this.perview.forEach((item, index) => {
    const containerDiv = document.createElement('div');
    containerDiv.classList.add('inscription-item');

    const imageContainer = document.createElement('div');
    imageContainer.classList.add('image-container');

    const image = document.createElement('img');
    image.src = `https://ordinals.com/content/${item.id}`; // Assuming 'id' is a property of 'item'
    image.id = `img${index}`;
    image.classList.add(`img${index}`);

    const link = document.createElement('a');
    link.href = `../inscription?id=${item.id}`; // Assuming 'id' is a property of 'item'
    link.id = `link${index}`;
    link.classList.add(`link${index}`);

    const title = document.createElement('title');
    title.href = `../inscription?id=${item.id}`; // Assuming 'id' is a property of 'item'
    title.id = `title${index}`;
    title.classList.add(`title${index}`);
    title.innerHTML = item.title; // Assuming 'title' is a property of 'item'

    const guid = document.createElement('a');
    guid.href = `../inscription?id=${item.id}`; // Assuming 'id' is a property of 'item'
    guid.id = `guid${index}`;
    guid.classList.add(`guid${index}`);

    imageContainer.appendChild(image);
    imageContainer.appendChild(document.createElement('hr'));
    imageContainer.appendChild(link);
    containerDiv.appendChild(imageContainer);
    containerDiv.appendChild(title);
    containerDiv.appendChild(document.createElement('br'));
    containerDiv.appendChild(guid);

      this.inscriptionGrid.appendChild(containerDiv); // Assuming 'inscriptionGrid' is a DOM element
    });
  } catch (error) {
    console.error('API Request Error:', error);
  }

  },
  async created() {
    //this.inscriptionid();
    this.fetchAndCreateHTML();
  },
  methods: {
    login(address) {
      // Simulate authentication logic
      // Check if the provided address is valid (you might want to use a library for Bitcoin address validation)
      if (this.isValidBitcoinAddress(address)) {
        this.userAddress = address;
        this.isLoggedIn = true;
      } else {
        alert("Invalid Bitcoin address. Please try again.");
      }
    },
    logout() {
      this.isLoggedIn = false;
      this.userAddress = null;
    },
    isValidBitcoinAddress(address) {
      // Simulate a basic Bitcoin address validation (you should use a proper library)
      const addressRegex = /^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$/;
      return addressRegex.test(address);
    },

    async fetchAndCreateHTML() {
     
      const start = 63339;
      const end = 64301;
      const limit = 1000;

      fetch(`https://ordapi.xyz/feed`)
        .then(response => response.json())
        .then(inscriptionData => {
          const inscriptionGrid = document.querySelector('.inscription-grid');
          console.log(response.data);

          fetch('ids.txt')
            .then(response => response.text())
            .then(ids => {
              const idList = ids.split('\n');
              onsole.log(ids);

              idList.forEach((id, index) => {
                const containerDiv = document.createElement('div');
                containerDiv.classList.add('inscription-item');

                const imageContainer = document.createElement('div');
                imageContainer.classList.add('image-container');

                const image = document.createElement('img');
                image.src = `https://ordinals.com/content/${id}`;
                image.id = `img${index}`;
                image.classList.add(`img${index}`);

                const link = document.createElement('a');
                link.href = `../inscription?id=${id}`;
                link.id = `link${index}`;
                link.classList.add(`link${index}`);

                const title = document.createElement('title');
                title.href = `../inscription?id=${id}`;
                title.id = `title${index}`;
                title.classList.add(`title${index}`);
                title.innerHTML = inscriptionData.title;

                const guid = document.createElement('a');
                guid.href = `../inscription?id=${id}`;
                guid.id = `guid${index}`;
                guid.classList.add(`guid${index}`);

                imageContainer.appendChild(image);
                imageContainer.appendChild(document.createElement('hr'));
                imageContainer.appendChild(link);
                containerDiv.appendChild(imageContainer);
                containerDiv.appendChild(title);
                containerDiv.appendChild(document.createElement('br'));
                containerDiv.appendChild(guid);

                inscriptionGrid.appendChild(containerDiv);
              });
            })
            .catch(error => {
              console.error('Error fetching IDs:', error);
            });
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
  },
}
</script>



<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');




* {
  margin: 0;
  box-sizing: border-box;
}

// html {
//   font-size: 62.5%;
// }
.paginatedList{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background-color: white
}

.my-rows {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

// body {
//   background-color: #0D192C;
//   font-family: 'Outfit', sans-serif;
// }

#my-home {
  //display: block;
  justify-content: center;
  display: flex;
  // margin-top: 62px;

  @media screen and (min-width: 768px) {
    margin-top: 152px;
  }
}


.body {
  // color: rgb(255, 255, 255);
  font-family: "Roboto", "Helvetica", "Arial", sans-serif;
  font-weight: 400;
  font-size: 1rem;
  line-height: 1.5;
  letter-spacing: 0.00938em;
}

.inscription-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0.6rem;
  margin-bottom: 50px;
}

.image-container {
  position: relative;
}

.inscription-item {
  background-color: #161718;
  border-radius: 15px;
  box-sizing: border-box;
  overflow: hidden;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
  width: 308.656px;
  height: 338.656px;
  margin: 10px;
  border: 0.1px solid #313539;
  margin: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  max-height: auto;
  object-fit: contain;
}

.inscription-item {
  background-color: #161718;
  border-radius: 15px;
  box-sizing: border-box;
  overflow: hidden;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
  width: 308.656px;
  height: 338.656px;
  margin: 10px;
  border: 0.1px solid #313539;
  margin: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  max-height: auto;
  object-fit: contain;
}

.inscription-item img {
  border: 1.5px solid #313539;
  box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  border-radius: 15px;
  display: block;
  width: 230.656px;
  height: 230.656px;
  margin-top: 30px;
}

.inscription-item a {
  text-decoration: none;
  font-size: 28px;
  color: #fff;
  margin-bottom: -8px;
  text-align: center;
  width: 100%;
  margin-top: 10px;
  font-weight: bold;
}

.inscription-item hr {
  margin: 0;
  width: 230.656px;
  margin-top: 10px;
  margin-bottom: 0px;
  border: 1px solid #313539;
}

.inscription-item .image-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}
</style>

 

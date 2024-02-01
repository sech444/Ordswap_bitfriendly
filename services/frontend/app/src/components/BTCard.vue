<template>
    <div>
      <!-- Your existing Vue template -->
      <div class="inscription-grid"></div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'App',
    data: () => ({
      list: [],
      currentPage: 1,
      perPage: 60,
      card: null,
    }),
    computed: {
      paginatedList() {
        // Your computed property logic here
      },
    },
    created() {
      this.fetchInscriptions(); // Fetch Vue data
      this.fetchAndCreateHTML(); // Fetch non-Vue data and create HTML
    },
    methods: {
      async fetchInscriptions() {
        // Fetch Vue data using axios
      },
      async fetchInscriptionsImage(link) {
        // Fetch image data for each item
      },
      async fetchAndCreateHTML() {
        const start = 63339;
        const end = 64301;
        const limit = 1000;
  
        
        fetch(`https://ordapi.xyz/inscriptions/?start=${start}&end=${end}&limit=${limit}`)
          .then(response => response.json())
          .then(inscriptionData => {
            // Get the container for the inscription grid
            const inscriptionGrid = document.querySelector('.inscription-grid');
  
            // Get the list of IDs from the text file
            fetch('ids.txt')
              .then(response => response.text())
              .then(ids => {
                // Split the IDs by line
                const idList = ids.split('\n');
  
                // Create the HTML elements for each inscription
                idList.forEach((id, index) => {
                  // Create the container div
                  const containerDiv = document.createElement('div');
                  containerDiv.classList.add('inscription-item');
  
                  // Create the image container
                  const imageContainer = document.createElement('div');
                  imageContainer.classList.add('image-container');
  
                  // Create the image element
                  const image = document.createElement('img');
                  image.src = `https://ordinals.com/content/${id}`;
                  image.id = `img${index}`;
                  image.classList.add(`img${index}`);
  
                  // Create the link element
                  const link = document.createElement('a');
                  link.href = `../inscription?id=${id}`;
                  link.id = `link${index}`;
                  link.classList.add(`link${index}`);
  
                  // Create the title element
                  const title = document.createElement('title');
                  title.href = `../inscription?id=${id}`;
                  title.id = `title${index}`;
                  title.classList.add(`title${index}`);
                  title.innerHTML = inscriptionData.title;
  
                  // Create the guid element
                  const guid = document.createElement('a');
                  guid.href = `../inscription?id=${id}`;
                  guid.id = `guid${index}`;
                  guid.classList.add(`guid${index}`);
  
                  // Add the elements to the container
                  imageContainer.appendChild(image);
                  imageContainer.appendChild(document.createElement('hr'));
                  imageContainer.appendChild(link);
                  containerDiv.appendChild(imageContainer);
                  containerDiv.appendChild(title);
                  containerDiv.appendChild(document.createElement('br'));
                  containerDiv.appendChild(guid);
  
                  // Add the container to the inscription grid
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
  };
  </script>
  

<style lang="scss" scoped>
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
<!-- <template>
  <b-container  fluid style="background-color: #191207;">
    <div>
      <b-row justify-content-center>
         <b-col sm="1" md="4" lg="3" xl="2" class="job-row">
          <b-card
            :title="name"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 25rem;"
            class=" mb-4 "
          >
            <b-card-text>
             #33,675,831
            </b-card-text>

            <b-button
              v-b-tooltip.hover
              title="Tooltip content"
              v-b-modal="modalId"
              variant="primary"
              >Go somewhere</b-button
            >
            <b-modal :id="modalId" title="BootstrapVue">
              <p class="my-4">Hello from modal!</p>
            </b-modal>
          </b-card>
        </b-col> -->

        <!-- Add 5 more b-col components here -->
        <!-- <b-col sm="1" md="4" lg="3" xl="2" class="job-row">
          <b-card
            :title="name"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 25rem;"
            class=" mb-4 "
          >
            <b-card-text>
             #33,675,831
            </b-card-text>

            <b-button
              v-b-tooltip.hover
              title="Tooltip content"
              v-b-modal="modalId"
              variant="primary"
              >Go somewhere</b-button
            >
            <b-modal :id="modalId" title="BootstrapVue">
              <p class="my-4">Hello from modal!</p>
            </b-modal>
          </b-card>
        </b-col>

        <b-col sm="1" md="4" lg="3" xl="2" class="job-row">
          <b-card
            :title="name"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 25rem;"
            class=" mb-4 "
          >
            <b-card-text>
             #33,675,831
            </b-card-text>

            <b-button
              v-b-tooltip.hover
              title="Tooltip content"
              v-b-modal="modalId"
              variant="primary"
              >Go somewhere</b-button
            >
            <b-modal :id="modalId" title="BootstrapVue">
              <p class="my-4">Hello from modal!</p>
            </b-modal>
          </b-card>
        </b-col>
         <b-col sm="1" md="4" lg="3" xl="2" class="job-row">
          <b-card
            :title="name"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 25rem;"
            class=" mb-4 "
          >
            <b-card-text>
             #33,675,831
            </b-card-text>

            <b-button
              v-b-tooltip.hover
              title="Tooltip content"
              v-b-modal="modalId"
              variant="primary"
              >Go somewhere</b-button
            >
            <b-modal :id="modalId" title="BootstrapVue">
              <p class="my-4">Hello from modal!</p>
            </b-modal>
          </b-card>
        </b-col>

        <b-col sm="1" md="4" lg="3" xl="2" class="job-row">
          <b-card
            :title="name"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 25rem;"
            class=" mb-4 "
          >
            <b-card-text>
             #33,675,831
            </b-card-text>

            <b-button
              v-b-tooltip.hover
              title="Tooltip content"
              v-b-modal="modalId"
              variant="primary"
              >Go somewhere</b-button
            >
            <b-modal :id="modalId" title="BootstrapVue">
              <p class="my-4">Hello from modal!</p>
            </b-modal>
          </b-card>
        </b-col>

        <b-col sm="1" md="4" lg="3" xl="2" class="job-row">
          <b-card
            :title="name"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 25rem;"
            class=" mb-4 "
          >
            <b-card-text>
             #33,675,831
            </b-card-text>

            <b-button
              v-b-tooltip.hover
              title="Tooltip content"
              v-b-modal="modalId"
              variant="primary"
              >Go somewhere</b-button
            >
            <b-modal :id="modalId" title="BootstrapVue">
              <p class="my-4">Hello from modal!</p>
            </b-modal>
          </b-card>
        </b-col>
   
  </b-row >
</div>
</b-container>
</template>


<script>
export default {
  props: ["name", "id"],
  computed: {
    modalId() {
      return `modal-${this.id}`;
    }
  }
};
</script>

<style>
.full-page {
  height: 100vh;
}
</style> --> 



<template>
  <!-- breakpoints: [`xs`, 'sm', 'md', 'lg', 'xl', 'xxl'] -->
  <b-container>
  <div>
    <b-row col="col-sm-2 col-md-6 col-lg-4 col-xl-3" >
      <b-col cols="12" md="auto"  xl="6"  class="job-row">
        <b-card
          :title="name"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20.50rem;"
          class=" mb-4 "
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button
            v-b-tooltip.hover
            title="Tooltip content"
            v-b-modal="modalId"
            variant="primary"
            >Go somewhere</b-button
          >
          <b-modal :id="modalId" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </b-card>
      </b-col>

       <!-- Add 5 more b-col components here -->
     <b-col cols="12" md="auto"  xl="6"  >
        <b-card
          :title="name"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20.50rem;"
          class=" mb-4 "
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button
            v-b-tooltip.hover
            title="Tooltip content"
            v-b-modal="modalId"
            variant="primary"
            >Go somewhere</b-button
          >
          <b-modal :id="modalId" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </b-card>
      </b-col>

      <b-col cols="12" md="auto"  xl="6"  >
        <b-card
          :title="name"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20.50rem;"
          class=" mb-4 "
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button
            v-b-tooltip.hover
            title="Tooltip content"
            v-b-modal="modalId"
            variant="primary"
            >Go somewhere</b-button
          >
          <b-modal :id="modalId" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </b-card>
      </b-col>

      <b-col cols="12" md="auto"  xl="6" >
        <b-card
          :title="name"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20.50rem;"
          class=" mb-4 "
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button
            v-b-tooltip.hover
            title="Tooltip content"
            v-b-modal="modalId"
            variant="primary"
            >Go somewhere</b-button
          >
          <b-modal :id="modalId" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </b-card>
      </b-col>

      <b-col cols="12" md="auto"  xl="6"  >
        <b-card
          :title="name"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20.50rem;"
          class=" mb-4 "
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button
            v-b-tooltip.hover
            title="Tooltip content"
            v-b-modal="modalId"
            variant="primary"
            >Go somewhere</b-button
          >
          <b-modal :id="modalId" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </b-card>
      </b-col>

      <b-col cols="12" md="auto"  xl="6" s>
        <b-card
          :title="name"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20.50rem;"
          class=" mb-4 "
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button
            v-b-tooltip.hover
            title="Tooltip content"
            v-b-modal="modalId"
            variant="primary"
            >Go somewhere</b-button
          >
          <b-modal :id="modalId" title="BootstrapVue">
            <p class="my-4">Hello from modal!</p>
          </b-modal>
        </b-card>
      </b-col>

      
    </b-row>
  </div>
  </b-container>
</template> 


<script>
export default {
  props: ["name", "id"],
  computed: {
    modalId() {
      return `modal-${this.id}`;
    }
  }
};
</script>

<style>
.full-page {
  height: 100vh;
}
</style>

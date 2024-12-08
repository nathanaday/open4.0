<template>
  <div class="flex gap-[2%] flex-wrap">

    <!-- Header -->
    <div class="w-full m-1">
      <div class="card bg-neutral text-neutral-content w-full">
        <!-- <div class="card-body"> -->
        <h1>Image Analysis Lab</h1>
        <!-- </div> -->
      </div>
    </div>
    <!-- END Header -->

    <!-- Sidebar -->
    <div class="w-1/4 h-1/2 ml-1">
      <div class="card bg-neutral text-neutral-content w-full">
        <!-- <div class="card-body"> -->
        <h2 class="card-title">Model Library</h2>
        <div class="drawer lg:drawer-open">
          <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
          <div class="drawer-side">
            <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
            <ul class="menu text-base-content w-60 p-1">
              <!-- Sidebar content here -->
              <li><a>Sidebar Item 1</a></li>
              <li><a>Sidebar Item 2</a></li>
            </ul>
          </div>
        </div>
        <!-- </div> -->
      </div>
    </div>
    <!-- END Sidebar -->

    <!-- Content -->
    <div class="grow h-3/4 mr-1">
      <div class="card bg-neutral text-neutral-content w-full">
        <h2 class="card-title">Image</h2>
        <div v-if="imageUrl">
          <img :src="imageUrl" alt="Uploaded Image" class="w-full max-w-md m-4" />
        </div>
        <div v-else>
          <div class="card bg-neutral text-neutral-content w-full">
            <p>No image uploaded</p>
            <p>Upload an image to get started</p>
          </div>
        </div>
        <div class="flex flex-row items-center gap-2">

        <input type="file" @change="onFileChange($event)"
          class="file-input file-input-bordered file-input-accent w-full max-w-xs" />
        <button class="btn btn-active btn-secondary w-full max-w-xs">Analyze</button>
      </div>
      </div>
    </div>
    <!-- END Content -->

    <!-- Footer -->
    <div class="w-full h-1/4 m-1">
      <div class="card bg-neutral text-neutral-content w-full">
        <h2 class="card-title">Results</h2>
        <p>If a dog chews shoes whose shoes does he choose?</p>
      </div>
    </div>
    <!-- END Footer -->
  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      imageUrl: ''
    };
  },
  methods: {
    onFileChange(payload: Event) {
      const event = payload as unknown as { target: { files: any[]; }; };
      const file = event.target.files[0];
      if (file) {
        this.imageUrl = URL.createObjectURL(file);
      }
    }
  }
};

</script>

<style scoped></style>

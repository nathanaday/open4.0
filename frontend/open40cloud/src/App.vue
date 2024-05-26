<template>
  <div id="app" class="min-h-screen flex flex-col items-center justify-center bg-light-gradient dark:bg-dark-gradient">
    <ExampleComponent />
  </div>
</template>
<script>
import ExampleComponent from './components/ExampleComponent.vue';

export default {
  name: 'App',
  components: {
    ExampleComponent,
  },
};
</script>

<style scoped>
/* Additional styles if needed */
</style>

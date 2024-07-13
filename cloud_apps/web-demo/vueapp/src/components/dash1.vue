<template>
    <div class="p-5 mx-auto shadow-lg flex items-center bg-gradient-to-r from-blue-600 via-blue-500 to-blue-400 top-0 w-full">
        <div>
            <h1 class="text-4xl font-medium text-white">Open4.0</h1>
        </div>
    </div>
    <div class="p-5 flex justify-center">
        <div class="card shadow-lg" style="height: 75vh; width: 80vw;">
            <PointView></PointView>
        </div>
    </div>
    <div class="p-2 flex justify-center">
        <div class="card shadow-lg bg-base-100">
            <div class="py-4 px-4 mx-auto text-center lg:py-16">
                Controls
                
            </div>
        </div>
    </div>
</template>

<script>
import PointView from './subcomponents/pointview.vue';

export default {
    name: 'Dash1',
    components: {
        PointView
    },
    data() {
        return {

        };
    },
    methods: {
    },
    mounted() {
        
    },
};
</script>

<style scoped>
.card {
  min-height: 500px; /* Example minimum height */
  min-width: 300px;;
}
</style>

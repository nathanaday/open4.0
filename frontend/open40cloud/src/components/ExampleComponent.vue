<template>
    <div class="p-4">
        <div class="card shadow-lg compact bg-base-100">
            <div class="card-body">
                <h2 class="card-title">Welcome to DaisyUI with Vue</h2>
                <p>This is a simple example using the Options API and DaisyUI components.</p>
                <div class="card-actions justify-end">
                    <button class="btn btn-primary w-64 rounded-full" @click="handleClick">Click Me</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ExampleComponent',
    data() {
        return {
            message: 'Hello, DaisyUI!',
        };
    },
    methods: {
        handleClick() {
            alert(this.message);
        },
    },
};
</script>

<style scoped></style>
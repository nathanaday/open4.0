<template>
    <div class="p-4 flex justify-center">
        <div class="card shadow-lg compact bg-base-100 max-w-xl mx-auto">
            <div class="py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16">
                <h1
                    class="mb-4 text-4xl font-bold tracking-tight leading-none text-gray-900 md:text-4xl lg:text-5xl dark:text-white">
                    Welcome to Open4.0
                </h1>
                <p class="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-4 lg:px-4 dark:text-gray-400">
                    The open-source framework for intelligent IoT applications
                </p>
                <div class="flex flex-col space-y-6 sm:flex-row sm:justify-center sm:space-y-0 sm:space-x-4">
                    <button
                        class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900">
                        Get started
                    </button>
                    <button
                        class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                        Source
                        <img :src="githubLogo" alt="GitHub Logo" class="w-6 h-6 ml-2">
                    </button>
                    <button
                        class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:outline-none focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                        Access demo
                        <!-- <svg class="w-4 h-4 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 14 10">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M1 5h12m0 0L9 1m4 4L9 9" />
                        </svg> -->
                        <img :src="mdiArrowRight" alt="Demo Logo" class="w-6 h-6 ml-2">
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import githubLogo from '../assets/icon-github-mark.svg';
import mdiArrowRight from '../assets/icon-mdi-arrow-right-drop-circle-outline.svg';

export default {
    name: 'ExampleComponent',
    data() {
        return {
            githubLogo,
            mdiArrowRight
        };
    },
    methods: {
        handleClick() {
        },
    },
};
</script>

<style scoped></style>
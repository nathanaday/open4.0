/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        'light-gradient': 'linear-gradient(135deg, #edf6ff 0%, #90c0ea 100%)',
        'dark-gradient': 'linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%)',
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
}

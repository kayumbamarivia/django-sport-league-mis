/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',  // Adjust based on where your HTML templates are located
    './static/**/*.{html,js}',     // Include your static JS files if they use Tailwind classes
    './**/*.html',                 // Include all HTML files if needed
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

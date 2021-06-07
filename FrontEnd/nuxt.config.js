export default {
    // Global page headers: https://go.nuxtjs.dev/config-head
    head: {
        title: "Data Insights",
        htmlAttrs: {
            lang: "en",
        },
        meta: [
            { charset: "utf-8" },
            { name: "viewport", content: "width=device-width, initial-scale=1" },
            { hid: "description", name: "description", content: "" },
        ],
        link: [
            { rel: "icon", type: "image/x-icon", href: "/favicon.ico" },
            {
                src: "https://code.jquery.com/jquery-3.3.1.slim.min.js",
                type: "text/javascript"
              },
              {
                src:
                  "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
                type: "text/javascript"
              },
        
            {
                href: "https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Poppins:wght@500&family=Roboto:wght@400;500;700&display=swap",
                rel: "stylesheet",
            },
            {
                href: "https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,600;1,700;1,800&display=swap",
                rel: "stylesheet",
            },
        ],
        
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        "@/assets/css/main.css",
        "@/node_modules/@mdi/font/css/materialdesignicons.min.css",
        "vue-slider-component/theme/antd.css"
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
        { src: '~/plugins/vue-slider-component', ssr: false }

    ],

    // Auto import components: https://go.nuxtjs.dev/config-components
    components: true,

    // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
    buildModules: [],

    // Modules: https://go.nuxtjs.dev/config-modules
    modules: [
        // https://go.nuxtjs.dev/bootstrap
        "bootstrap-vue/nuxt",
        // https://go.nuxtjs.dev/axios
        "@nuxtjs/axios",
    ],

    // Axios module configuration: https://go.nuxtjs.dev/config-axios
    axios: {
        // baseURL: "http://127.0.0.1:5000",
        // baseURL: "http://18.218.36.147/db",
        baseURL: "http://18.218.36.147/testingBE1",
    },

    // Build Configuration: https://go.nuxtjs.dev/config-build
    build: {
        vendor: [
            'vue-slider-component'
    ],
    },
    server: {
        port: 3001 // default: 3000
      }
};
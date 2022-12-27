import { createApp } from "vue";
import App from "./App.vue";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import { globalCookiesConfig } from "vue3-cookies";
globalCookiesConfig({
  expireTimes: "",
  path: "/",
  domain: "127.0.0.1",
  secure: true,
  sameSite: "None",
});

createApp(App).use(ElementPlus).mount("#app");

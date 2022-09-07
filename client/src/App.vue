<template>
  <div>
    <Header />
    <router-view />
    <Footer />
  </div>
</template>

<script>
import Header from "./components/header";
import Footer from "./components/footer";
import {Chat} from "vue-quick-chat";

export default {
  name: "App",
  components: {
    Header,
    Footer,
    Chat
  },
  created: function () {
    this.$http.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch("logout")
        }
        throw err;
      });
    });
  }

}
</script>


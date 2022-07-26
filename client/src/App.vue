<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/navbar";

export default {
  name: "App",
  components: {
    Navbar,
    Chat: () => import('vue-beautiful-chat')
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


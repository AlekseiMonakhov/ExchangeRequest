<template>
  <div>
    <Navbar />
    <Request />
  </div>
</template>

<script>
import Navbar from "./components/navbar";
import Request from "./components/request";

export default {
  name: "App",
  components: {
    Navbar,
    Request
  }

}
</script>


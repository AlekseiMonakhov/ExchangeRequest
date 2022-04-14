<template>
  <div>
    <Navbar />
    <RequestsList />
  </div>
</template>

<script>
import Navbar from "./components/navbar";
import Request from "./components/request";
import RequestsList from "./components/requestsList";

export default {
  name: "App",
  components: {
    Navbar,
    Request,
    RequestsList,
  }

}
</script>


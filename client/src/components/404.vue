<template>
  <div>
    <div class="container">
      <b>404</b>
    </div>
    <div class="container">
      <b>Страница не найдена</b>
    </div>
    <div class="container">
      <b-button @click="home" size="sm" pill variant="primary">На главную</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Error404",
  methods: {
    home() {
      this.$router.push({name: 'Создать заявку'});
    }
  },
};
</script>

<style scoped>
.container {
  display: flex;

  justify-content: center;
}

</style>

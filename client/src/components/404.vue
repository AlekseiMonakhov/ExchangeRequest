<template>
  <v-main>
    <v-container>
      <v-btn class="v-btn" @click="home" width=50 height=30><h1>404</h1>Страница не найдена</v-btn>
    </v-container>
  </v-main>
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
*{
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-top: 10px;
}

.v-btn{
  align-items: center;
}
</style>

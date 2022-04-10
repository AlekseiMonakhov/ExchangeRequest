<template>
  <b-navbar
    toggleable="md"
    type="dark"
    variant="primary">
    <b-navbar-nav>
      <b-nav-item :to="{ name: 'App' }">Создать заявку</b-nav-item>
      <b-nav-item href="#">Активные заявки</b-nav-item>
      <b-nav-item href="#">Панель администратора</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>
<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>

</style>

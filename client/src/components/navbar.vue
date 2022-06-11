<template>
  <b-navbar
    class="navbar"
    toggleable="lg"
    type="dark"
    variant="primary">
    <b-navbar-nav>
      <b-nav-item @click="$router.push('/')">Создать заявку</b-nav-item>
      <b-nav-item @click="$router.push('/requestsList')">Активные заявки</b-nav-item>
      <b-nav-item @click="$router.push('/adminPanel')">Панель администратора</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>
<script>
export default {
  name: 'Navbar',
}
</script>

<style>

</style>

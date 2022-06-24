<template xmlns="http://www.w3.org/1999/html">
  <b-navbar
    class="navbar"
    toggleable="lg"
    type="dark"
    variant="primary">
    <b-navbar-nav>
      <b-nav-item @click="$router.push('/')">Создать заявку</b-nav-item>
      <b-nav-item @click="$router.push('/requestsList')">Активные заявки</b-nav-item>
      <b-nav-item @click="$router.push('/adminPanel')">Панель администратора</b-nav-item>
      <div v-if="isLoggedIn" class="nav1">
      <b-nav-item @click="logout">Выйти</b-nav-item>
      </div>
    </b-navbar-nav>
  </b-navbar>
</template>
<script>
export default {
  name: 'Navbar',
  computed : {
    isLoggedIn : function(){ return this.$store.getters.isLoggedIn}
  },
  methods: {
    logout: function () {
      this.$store.dispatch('logout')
        .then(() => {
          this.$router.push('/login')
        })
    }
  },
}
</script>

<style>


</style>

<template xmlns="http://www.w3.org/1999/html">
  <b-navbar
    class="navbar"
    toggleable="lg"
    type="dark"
    variant="primary">
    <b-navbar-nav class="navbar">
      <b-nav-item class="link" @click="$router.push('/')">Создать заявку</b-nav-item>
      <b-nav-item class="link" @click="$router.push('/requestsList')">Активные заявки</b-nav-item>
      <b-nav-item class="link" v-if="isAdmin" @click="$router.push('/adminPanel')">Панель администратора
      </b-nav-item>
      <b-nav-item class="link" v-if="isLoggedIn" @click="logout">Выйти</b-nav-item>
    </b-navbar-nav>
  </b-navbar>
</template>
<script>
export default {
  name: 'Navbar',
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn
    },
    isAdmin: function () {
      return this.$store.getters.isAdmin
    }
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

<style scoped>
navbar {
  display: flex;
}

.link {
  margin-right: auto;
}


</style>

<template>
  <div
  >
    <v-app-bar
      color="#0080FF"

    >
      <v-app-bar-nav-icon @click="drawer = true"><strong>☰</strong></v-app-bar-nav-icon>
      <v-toolbar-title >ExchangeRequest</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
      >
        <v-list-item-group
        >
          <v-list-item>
            <v-list-item-title class="link" @click="$router.push('/')">Создать заявку</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title class="link" @click="$router.push('/requestsList')">Активные заявки</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title class="link" @click="$router.push('/myDeals')">Мои сделки</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title class="link" v-if="isAdmin" @click="$router.push('/adminPanel')">Админпанель</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title class="link" v-if="isLoggedIn" @click="logout">Выйти</v-list-item-title>
          </v-list-item>


        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "header",
  data: () => {
    return {
      drawer: false,

    };
  }
,computed: {
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

</style>

<template>
  <div class="main-element">
    <v-footer
      color="#0080FF"
      padless
      fixed
      height="80"
      rounded
    >
      <v-col>
        <div class="element-1">
        <v-btn text rounded x-small class="link"  @click="$router.push('/')">Создать заявку
        </v-btn>
        <v-btn text rounded x-small class="link" @click="$router.push('/requestsList')">Активные заявки
      </v-btn>
        <v-btn text rounded x-small class="link" @click="$router.push('/myDeals')">Мои сделки
        </v-btn>
        </div>
        <v-col
          class="primary lighten-2 text-center white--text"
        >
          {{ new Date().getFullYear() }}  <strong>ExchangeRequest</strong>
        </v-col>
      </v-col>
    </v-footer>
  </div>
</template>

<script>
export default {
  name: "footer"
}
</script>

<style scoped>
.main-element {
  margin-top: 120px;
}
.element-1 {
  display: flex;
  justify-content: center;

}
</style>

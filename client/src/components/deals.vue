<template>
  <div class="root-element">
    <div class="main-element" v-for="request in requests">
      <b-card bg-variant="light" text-variant="black">
        <b-card>
          <div class="element-1">
            <div class="element-2"><strong> Сделка {{ request.deal_id }} </strong>(Заявка {{ request.id }})</div>
            <div class="element-2" v-if="isCurrentUser(request.maker_username)"> Мейкер: Я</div>
            <div class="element-2" v-else> Мейкер: {{ request.maker_username }} Рейтинг: {{ request.maker_rank }}</div>
            <div class="element-2" v-if="isCurrentUser(request.taker_username)"> Тейкер: Я</div>
            <div class="element-2" v-else> Тейкер: {{ request.taker_username }} Рейтинг: {{ request.taker_rank }}</div>

            <div class="element-2"> {{ request.created_on.replace(/T/, ' ').slice(0, -7) }}</div>
            <div class="element-2"> Профит: {{ request.profit }}</div>
            <div class="element-2"> Статус: {{ request.status }}</div>
          </div>
          <div class="element-1">
            <div class="element-2"><strong>От Мейкера: </strong></div>
            <div class="element-2"> {{ request.current_amount }} {{ request.current_currency }}</div>
            <div class="element-2"> {{ request.current_type }}</div>
            <div class="element-2"> {{ request.current_country }} {{ request.current_city }}</div>
            <div class="element-2"> {{ request.current_bank }} {{ request.current_purpose }}</div>
          </div>
          <div class="element-1">
            <div class="element-2"><strong> От Тейкера: </strong></div>
            <div class="element-2"> {{ request.wanted_amount }} {{ request.wanted_currency }}</div>
            <div class="element-2"> {{ request.wanted_type }}</div>
            <div class="element-2"> {{ request.wanted_country }} {{ request.wanted_city }}</div>
            <div class="element-2"> {{ request.wanted_bank }} {{ request.wanted_purpose }}</div>
          </div>
        </b-card>
        <b-button @click="$router.push('/chat')" variant="primary">Чат сделки</b-button>
      </b-card>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Config from '../../envConfig'

export default {
  name: "deals",
  data() {
    return {
      requests: []
    }
  },
  methods: {
    async getData() {
      const currentUserId = JSON.parse(this.$store.getters.getUser)['id'].replace(/-/gi, '')
      const deals = await this.$store.getters.getDeals
      this.requests = deals.filter(function (deal) {
        deal.maker_id = deal.maker_id.replace(/-/gi, '')
        deal.taker_id = deal.taker_id.replace(/-/gi, '')
        return deal.taker_id === currentUserId || deal.maker_id === currentUserId
      })
    },
    isCurrentUser(username) {
      try {
        const currentUsername = JSON.parse(this.$store.getters.getUser)['username']
        return currentUsername === username
      } catch (e) {
        console.log(e)
      }
    },
    async deleteDeal(request) {
      try {
        await axios.delete(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/delete/${request.deal_id}`)
          .then(location.reload())

      } catch (e) {
        console.log(e)
        alert("Error!");
      }
    }
  },
  beforeMount() {
    this.getData()
  }
};
</script>

<style scoped>

.main-element {
  display: flex;
  flex-direction: column;
  margin-left: 1%;
  margin-top: 1%;
  justify-content: center;
}

</style>



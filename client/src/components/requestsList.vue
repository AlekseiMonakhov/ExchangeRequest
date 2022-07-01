<template>
  <div class="root-element">
    <div class="main-element" v-for="request in requests">
      <b-card bg-variant="light" text-variant="black">
        <b-card>
          <div class="element-1">
            <div class="element-2"><strong> {{ request.id }} </strong></div>
            <div class="element-2"> Создатель заявки: {{ request.maker_username }}</div>
            <div class="element-2"> Рейтинг: {{ request.maker_rank }}</div>
            <div class="element-2"> {{ request.created_on.replace(/T/, ' ').slice(0, -7) }}</div>
            <div class="element-2"> Вознаграждение: {{ request.profit }}</div>
          </div>
          <div class="element-1">
            <div class="element-2"><strong>Вы получите: </strong></div>
            <div class="element-2"> {{ request.current_amount }} {{ request.current_currency }}</div>
            <div class="element-2"> {{ request.current_type }}</div>
            <div class="element-2"> {{ request.current_country }} {{ request.current_city }}</div>
            <div class="element-2"> {{ request.current_bank }} {{ request.current_purpose }}</div>
          </div>
          <div class="element-1">
            <div class="element-2"><strong> Вы отдаете: </strong></div>
            <div class="element-2"> {{ request.wanted_amount }} {{ request.wanted_currency }}</div>
            <div class="element-2"> {{ request.wanted_type }}</div>
            <div class="element-2"> {{ request.wanted_country }} {{ request.wanted_city }}</div>
            <div class="element-2"> {{ request.wanted_bank }} {{ request.wanted_purpose }}</div>
          </div>
        </b-card>
        <b-button v-if="isNoMaker(request.maker_id)" @click="$router.push('/chat'), send(request)" variant="primary">
          Связаться
        </b-button>
        <b-button v-else disabled>Моя заявка</b-button>
      </b-card>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Config from '../../envConfig'
import request from "./request";

export default {
  name: "RequestsList",
  data() {
    return {
      requests: [],
    }
  },

  methods: {
    send: async function (request) {
      axios.post(`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/open-deal`, request)
        .catch(function (error) {
          console.log(error)
        })
    },
    async getData() {
      try {
        const requests = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/getlist`
        );
        this.requests = requests.data;
      } catch (e) {
        alert("Error!");
      }
    },
    isNoMaker: function (makerId) {
      const currentUserId = JSON.parse(this.$store.getters.getUser)['id'].replace(/-/gi, '')
      makerId = makerId.replace(/-/gi, '')
      if (currentUserId != makerId) {
        return true
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

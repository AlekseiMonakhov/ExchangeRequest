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
        <b-button v-else-if="isLoggedIn" variant="primary" disabled>Моя заявка</b-button>
        <b-button v-else @click="$router.push('/login')" variant="primary">Войти в аккаунт</b-button>
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
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn
    }
    },
  methods: {
    send: async function (request) {
      const data = {
        id: request.id,
        current_amount: request.current_amount,
        wanted_amount: request.wanted_amount,
        current_country: request.current_country || "",
        current_city: request.current_city  || "",
        wanted_city: request.wanted_city || "",
        current_bank: request.current_bank || "",
        wanted_bank: request.wanted_bank || "",
        current_purpose: request.current_purpose || "",
        wanted_purpose: request.wanted_purpose || "",
        wanted_country: request.wanted_country || "",
        current_currency: request.current_currency,
        wanted_currency: request.wanted_currency,
        current_type: request.current_type,
        wanted_type: request.wanted_type,
        profit: request.profit,
        maker_id: request.maker_id,
        taker_id: `${JSON.parse(this.$store.getters.getUser)['id']}`,
        maker_rank: request.maker_rank,
        taker_rank: `${JSON.parse(this.$store.getters.getUser)['rank']}`,
        maker_username: request.maker_username,
        taker_username: `${JSON.parse(this.$store.getters.getUser)['username']}`,
      }
      console.log(data)
      axios.post(`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/open-deal`, data)
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
    createChat: async function (request) {
      const data = {
        id: request.id,
        maker_id: request.maker_id,
        taker_id: `${JSON.parse(this.$store.getters.getUser)['id']}`,
        maker_username: request.maker_username,
        taker_username: `${JSON.parse(this.$store.getters.getUser)['username']}`,
      }
      console.log(data)
      axios.post(`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/open-deal`, data)
        .catch(function (error) {
          console.log(error)
        })
    },
    isNoMaker: function (makerId) {
      try {
        const currentUserId = JSON.parse(this.$store.getters.getUser)['id'].replace(/-/gi, '')
        makerId = makerId.replace(/-/gi, '')
        if (currentUserId != makerId) {
          return true
        }
      }
      catch (e) {
        console.log(e)
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

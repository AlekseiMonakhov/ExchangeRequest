<template>
  <v-container fluid>
    <template>
      <v-row>
        <v-col
          v-for="request in requests"
          :key="request.id"
          cols="12"
          sm="6"
          md="4"
          lg="3"
        >
          <v-card
          elevation="20"
          shaped
          >
            <v-list dense>
              <v-list-item>
                <v-list-item-content>
                  <strong>{{ request.id }}</strong>
                </v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.created_on.replace(/T/, ' ').slice(0, -7) }}
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content><strong>Создатель заявки:</strong></v-list-item-content>
                <v-list-item-content v-if="isCurrentUser(request.maker_username)" class="align-end">
                  Я
                </v-list-item-content>
                <v-list-item-content v-else class="align-end">
                  {{ request.maker_username }}
                </v-list-item-content>

              </v-list-item>

              <v-list-item>
                <v-list-item-content><strong>Рейтинг</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.maker_rank }}
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content><strong>ID</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.maker_id }}
                </v-list-item-content>
              </v-list-item>

              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content><strong>Вы отдаете:</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.wanted_amount }} {{ request.wanted_currency }}
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content v-if="request.wanted_type === 'Криптовалюта'" class="align-end">
                </v-list-item-content>
                <v-list-item-content v-else-if="request.wanted_type === 'Наличные'" class="align-end">
                {{request.wanted_city}}
                </v-list-item-content>
                <v-list-item-content v-else-if="request.wanted_type === 'Банковский перевод'" class="align-end">
                  {{request.wanted_country}}, {{request.wanted_bank}}
                </v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.wanted_type }}
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content><strong>Вы получите:</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.current_amount }} {{ request.current_currency }}
                </v-list-item-content>
              </v-list-item>

              <v-list-item>

                <v-list-item-content v-if="request.current_type === 'Криптовалюта'" class="align-end">
                </v-list-item-content>
                <v-list-item-content v-else-if="request.current_type === 'Наличные'" class="align-end">
                  {{request.current_city}}
                </v-list-item-content>
                <v-list-item-content v-else-if="request.current_type === 'Банковский перевод'" class="align-end">
                  {{request.current_country}}, {{request.current_bank}}
                </v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.current_type }}
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content><strong>Профит</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.profit }}
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content></v-list-item-content>
                <v-list-item-content>
                  <b-button v-if="isNoMaker(request.maker_id)" @click="send(request)" variant="primary">
                    Связаться
                  </b-button>
                  <b-button v-else-if="isLoggedIn" @click="deleteRequest(request)" variant="dark">Удалить заявку</b-button>
                  <b-button v-else @click="$router.push('/login')" variant="primary">Войти в аккаунт</b-button>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </v-container>
</template>

<script>
import axios from "axios";
import Config from '../../envConfig'
import {TYPE} from "vue-toastification";


export default {
  name: "requestsList",
  data() {
    return {
      requests: []
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
      if (this.isDealExist(data)) {
        this.$MyToast("Сделка уже открыта", TYPE.WARNING)
        await this.$router.push('/myDeals')
      } else {
        axios.post(`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/open-deal`, data)
          .then(this.$store.dispatch('getDeals'))
          .then(this.$router.push('/chat'))
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    async getData() {
      try {
        const requests = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/getlist`
        );
        this.requests = requests.data;
      } catch (error) {
        console.log(error)
        this.$MyToast("Ошибка", TYPE.ERROR);
      }
    },
    // createChat: async function (request) {
    //   const data = {
    //     id: request.id,
    //     maker_id: request.maker_id,
    //     taker_id: `${JSON.parse(this.$store.getters.getUser)['id']}`,
    //     maker_username: request.maker_username,
    //     taker_username: `${JSON.parse(this.$store.getters.getUser)['username']}`,
    //   }
    //   console.log(data)
    //   axios.post(`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/open-deal`, data)
    //     .catch(function (error) {
    //       console.log(error)
    //     })
    // },
    async deleteRequest(request) {
      try {
        await axios.delete(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/delete-request/${request.id}`)
          .then(this.$MyToast("Заявка удалена", TYPE.SUCCESS))
          .then(location.reload())

      } catch (error) {
        console.log(error)
        this.$MyToast("Ошибка", TYPE.ERROR);
      }
    },
    isNoMaker: function (makerId) {
      try {
        const currentUserId = JSON.parse(this.$store.getters.getUser)['id'].replace(/-/gi, '')
        makerId = makerId.replace(/-/gi, '')
        return currentUserId !== makerId
      }
      catch (e) {
        console.log(e)
      }
    },
    isCurrentUser(username) {
      try {
        const currentUsername = JSON.parse(this.$store.getters.getUser)['username']
        return currentUsername === username
      } catch (e) {
        console.log(e)
      }
    },
    isDealExist(data) {
      const deals = this.$store.getters.getDeals
      if (deals) {
        let thisDeal = []
        for (let deal of deals) {
          if (deal.id === data.id && deal.taker_username === data.taker_username) {
            thisDeal.push(deal)
          }
        }
        return thisDeal.length >= 1
      }}
  },
  beforeMount() {
    this.getData()
  }
};
</script>

<style scoped>

</style>

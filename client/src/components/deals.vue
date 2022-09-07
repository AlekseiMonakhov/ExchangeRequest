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
                  <strong><strong> Сделка {{ request.deal_id }} </strong>(Заявка {{ request.id }})</strong>
                </v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.created_on.replace(/T/, ' ').slice(0, -7) }}
                </v-list-item-content>
                </v-list-item>
              <v-list-item>
                <v-list-item-content class="align-end">
                  <strong>Статус:</strong>
                </v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.status }}
                </v-list-item-content>
              </v-list-item>
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content><strong>Мейкер:</strong></v-list-item-content>
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
                <v-list-item-content><strong>От мейкера:</strong></v-list-item-content>
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
                <v-list-item-content><strong>Тейкер:</strong></v-list-item-content>
                <v-list-item-content v-if="isCurrentUser(request.taker_username)" class="align-end">
                  Я
                </v-list-item-content>
                <v-list-item-content v-else class="align-end">
                  {{ request.taker_username }}
                </v-list-item-content>

              </v-list-item>

              <v-list-item>
                <v-list-item-content><strong>Рейтинг</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.taker_rank }}
                </v-list-item-content>
              </v-list-item>

              <v-list-item>
                <v-list-item-content><strong>От тейкера:</strong></v-list-item-content>
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
              <v-divider></v-divider>
              <v-list-item>
                <v-list-item-content><strong>Профит</strong></v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ request.profit }}
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content></v-list-item-content>
                <v-list-item-content>
                  <b-button @click="$router.push('/chat')" variant="primary">Чат сделки</b-button>
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

</style>



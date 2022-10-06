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
                  <strong> Сделка {{ request.deal_id }} </strong>(Заявка {{ request.id }})
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
                <v-list-item-content class="align-end">
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
                <v-list-item-content class="align-end">
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
                  <b-button @click="$router.push({name: 'adminChat', params: {deal: request}})" pill variant="primary">Чат сделки</b-button>
                  <b-button @click="deleteDeal(request)" size="sm" pill variant="danger">Отменить сделку</b-button>
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
import Config from '../../../envConfig'
import {TYPE} from "vue-toastification";

export default {
  name: "adminPanel",
  data() {
    return {
      requests: []
    }
  },
  methods: {
    async getData() {
      try {
        const requests = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/getOpenDeals`
        );
        this.requests = requests.data;
      } catch (error) {
        console.log(error)
        this.$MyToast("Ошибка", TYPE.ERROR);
      }
    },
    async deleteDeal(request) {
      try {
        await axios.delete(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/delete-deal/${request.deal_id}`)
          .then(this.$MyToast("Сделка удалена", TYPE.SUCCESS))
          .then(location.reload())

      } catch (error) {
        console.log(error)
        this.$MyToast("Ошибка", TYPE.ERROR);
      }
    }
  },
  beforeMount(){
    this.getData()
  }
};
</script>

<style scoped>

</style>


<template>
  <div class="container mt-4">
    <div class="row">
      <label><b>У меня есть</b></label>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_currency">
          <option disabled value="">Выберите валюту</option>
          <option
            v-for="currency in currencies"
            v-bind:key="currency.currency_name"
          >
            {{ currency.currency_name }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_type">
          <option disabled value="">Выберите тип платежа</option>
          <option v-if="current_currency === 'USDT'"> Криптовалюта </option>
          <option v-else v-for="type in paymentType" v-bind:key="type.type">
            {{ type.type }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <input
          class="form-control"
          type="number"
          placeholder="Укажите сумму"
          v-model.number="current_amount"
        />
      </div>


      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_city" v-if="current_type === 'Наличные'">
          <option disabled value="">Выберите город</option>
          <option
            v-for="city in cities"
            v-bind:key="city.city_name"
          >
            {{ city.city_name }}
          </option>
        </select>
        <select class="form-select" v-model="current_country" v-if="current_type === 'Банковский перевод'">
          <option disabled value="">Выберите страну</option>
          <option
            v-for="country in countries"
            v-bind:key="country.country_name"
          >
            {{ country.country_name }}
          </option>
        </select>
      </div>
        <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_bank" v-if="current_type === 'Банковский перевод'">
          <option disabled value="">Выберите банк</option>
          <option
            v-for="bank in banks"
            v-bind:key="bank.bank_name"
            v-if="bank.country == current_country"
          >
            {{ bank.bank_name }}
          </option>
        </select>
        </div>
        <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_purpose" v-if="current_type === 'Банковский перевод'">
          <option disabled value="">Назначение платежа</option>
          <option
            v-for="purpose in purposes"
            v-bind:key="purpose.purpose"
          >
            {{ purpose.purpose }}
          </option>
        </select>

      </div>


    </div>


    <div class="row mt-4">
      <label><b>Я хочу получить</b></label>
      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_currency">
          <option disabled value="">Выберите валюту</option>
          <option
            v-for="currency in currencies"
            v-bind:key="currency.currency_name"
          >
            {{ currency.currency_name }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_type">
          <option disabled value="">Выберите тип платежа</option>
          <option v-if="wanted_currency === 'USDT'"> Криптовалюта </option>
          <option v-else v-for="type in paymentType" v-bind:key="type.type">
            {{ type.type }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
          <input
            class="form-control"
            type="number"
            placeholder="Укажите сумму"
            v-model.number="wanted_amount"
          />
      </div>


      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_city" v-if="wanted_type === 'Наличные'">
          <option disabled value="">Выберите город</option>
          <option
            v-for="city in cities"
            v-bind:key="city.city_name"
          >
            {{ city.city_name }}
          </option>
        </select>
        <select class="form-select" v-model="wanted_country" v-if="wanted_type === 'Банковский перевод'">
          <option disabled value="">Выберите страну</option>
            <option
              v-for="country in countries"
              v-bind:key="country.country_name"
            >
              {{ country.country_name }}
            </option>
        </select>
      </div>
      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_bank" v-if="wanted_type === 'Банковский перевод'">
          <option disabled value="">Выберите банк</option>
          <option
            v-for="bank in banks"
            v-bind:key="bank.bank_name"
            v-if="bank.country == wanted_country"
          >
            {{ bank.bank_name }}
          </option>
        </select>
      </div>
        <div class="col-sm-3 mt-2">
          <select class="form-select" v-model="wanted_purpose" v-if="wanted_type === 'Банковский перевод'">
            <option disabled value="">Назначение платежа</option>

            <option
              v-for="purpose in purposes"
              v-bind:key="purpose.purpose"
            >
              {{ purpose.purpose }}
            </option>

        </select>

      </div>
    </div>

    <div >
      <b-button v-if="this.$store.getters.isLoggedIn" @click="send()" pill variant="primary">
        Разместить заявку
      </b-button>
      <b-button v-else @click="$router.push('/login')" pill variant="info">Войти в аккаунт</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Config from '../../envConfig'
import { TYPE } from "vue-toastification"


export default {
  name: "request",
  data() {
    return {
      countries: [],
      currencies: [],
      paymentType: [],
      cities: [],
      banks: [],
      purposes: [],
      current_country: "",
      current_city: "",
      current_bank: "",
      current_purpose: "",
      current_type: "",
      current_currency: "",
      current_amount: "",
      wanted_country: "",
      wanted_type: "",
      wanted_currency: "",
      wanted_amount: "",
      wanted_city: "",
      wanted_bank: "",
      wanted_purpose: "",
    };
  },
  methods: {
    send: async function () {
      if (
        this.current_type === "" ||
        this.current_currency === "" ||
        this.current_amount === "" ||
        this.wanted_type === "" ||
        this.wanted_currency === "" ||
        this.wanted_amount === ""
      ) {
        this.error = "All fields required!";
        this.$MyToast("Заполните все поля", TYPE.WARNING);
      }
      else if (
        this.current_type === 'Банковский перевод' && this.current_country === "" ||
        this.current_type === 'Банковский перевод' && this.current_bank === "" ||
        this.wanted_type === 'Банковский перевод' && this.wanted_country === "" ||
        this.wanted_type === 'Банковский перевод' && this.wanted_bank === ""
      ) {
        this.error = "All fields required!";
        this.$MyToast("Заполните все поля", TYPE.WARNING);
      }
      else if (
        this.current_type === 'Наличные' && this.current_city === "" ||
        this.wanted_type === 'Наличные' && this.wanted_city === ""
      ) {
        this.error = "All fields required!";
        this.$MyToast("Заполните все поля", TYPE.WARNING);
      }else {
        let data = {
          maker_id: `${JSON.parse(this.$store.getters.getUser)['id']}`,
          maker_rank: `${JSON.parse(this.$store.getters.getUser)['rank']}`,
          maker_username: `${JSON.parse(this.$store.getters.getUser)['username']}`,
          current_country: `${this.current_country}`,
          current_currency: `${this.current_currency}`,
          current_type: `${this.current_type}`,
          current_amount: `${this.current_amount}`,
          current_city: `${this.current_city}`,
          current_bank: `${this.current_bank}`,
          current_purpose: `${this.current_purpose}`,
          wanted_country: `${this.wanted_country}`,
          wanted_currency: `${this.wanted_currency}`,
          wanted_type: `${this.wanted_type}`,
          wanted_amount: `${this.wanted_amount}`,
          wanted_city: `${this.wanted_city}`,
          wanted_bank: `${this.wanted_bank}`,
          wanted_purpose: `${this.wanted_purpose}`,
          profit: `${await this.getRates(this.current_currency, this.current_amount, this.wanted_currency, this.wanted_amount)}`
        };
        axios({url:`http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/create`, data: data, method: 'POST', headers: {
          }})
          .then(() => {
            this.$MyToast("Ваша заявка размещена", TYPE.SUCCESS)})
          .then (() => this.$router.push('/requestsList') )
          .catch((error) => {
            console.log(error)
            this.$MyToast("Ошибка", TYPE.ERROR)
          }).then (() => this.$router.push('/requestsList') )

      }
    },
    async getRates(current_currency, current_amount, wanted_currency, wanted_amount) {
      try {
        const response = await fetch("https://openexchangerates.org/api/latest.json?app_id=7ed211f995bc422e95d391aa76b7e71e")
        const responseRates = await response.json()
        const RatesList = responseRates.rates
        current_currency == "USDT" ? current_currency = "USD": current_currency = current_currency
        wanted_currency == "USDT" ? wanted_currency = "USD": wanted_currency = wanted_currency
        const profit = ((current_amount / RatesList[`${current_currency}`]) - (wanted_amount / RatesList[`${wanted_currency}`]))/(wanted_amount / RatesList[`${wanted_currency}`]) * 100
        return this.profit = `${profit.toFixed(1)} %`
      } catch (error) {
        console.log(error)
      }
    },
    async getData() {
      try {
        const responseCountries = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/data/countries`
        );
        this.countries = responseCountries.data;
        const responseCurrencies = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/data/currencies`
        );
        this.currencies = responseCurrencies.data;
        const responsePaymentTypes = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/data/paymentType`
        );
        this.paymentType = responsePaymentTypes.data;
        const responseCities = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/data/cities`
        );
        this.cities = responseCities.data;
        const responseBanks = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/data/banks`
        );
        this.banks = responseBanks.data;
        const responsePurposes = await axios.get(
          `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/data/purposes`
        );
        this.purposes = responsePurposes.data;
      } catch (error) {
        console.log(error)
        this.$MyToast("Ошибка", TYPE.ERROR);
      }
    },
  },
  beforeMount(){
    this.getData()
  }
};
</script>

<style scoped>
.col-sm-3 {
  margin-right: 30px;
  float: left;
}
</style>

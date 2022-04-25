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
          <option v-for="type in paymentType" v-bind:key="type.type">
            {{ type.type }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <input
          class="form-control"
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
        <select class="form-select" v-model="current_bank" v-if="current_type === 'Банковский перевод'">
          <option disabled value="">Выберите банк</option>
          <option
            v-for="bank in banks"
            v-bind:key="bank.bank_name"
          >
            {{ bank.bank_name }}
          </option>
        </select>
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
          <option v-for="type in paymentType" v-bind:key="type.type">
            {{ type.type }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <input
          class="form-control"
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
        <select class="form-select" v-model="wanted_bank" v-if="wanted_type === 'Банковский перевод'">
          <option disabled value="">Выберите банк</option>
          <option
            v-for="bank in banks"
            v-bind:key="bank.bank_name"
          >
            {{ bank.bank_name }}
          </option>
        </select>
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

    <div>
      <button @click="send()" type="button" class="btn btn-primary mt-4">
        Разместить заявку
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Request",
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
    send: function () {
      if (
        this.current_type === "" ||
        this.current_currency === "" ||
        this.current_amount === "" ||
        this.wanted_type === "" ||
        this.wanted_currency === "" ||
        this.wanted_amount === ""
      ) {
        this.error = "All fields required!";
        alert("Заполните все поля!");
      } else {
        let data = {
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
          profit: "1%"
        }
        axios.post("http://localhost:5000/request/create", data)
          .then(function (response){
            alert("Ваша заявка размещена. Как только найдется подходящее предложение, Вы получите уведомление.");
            location.reload()
            }
          )
          .catch(function (error){
            console.log(error)
            alert("Error!")
          })

      }
    },
    async getData() {
      try {
        const responseCountries = await axios.get(
          "http://localhost:5000/data/countries"
        );
        this.countries = responseCountries.data;
        const responseCurrencies = await axios.get(
          "http://localhost:5000/data/currencies"
        );
        this.currencies = responseCurrencies.data;
        const responsePaymentTypes = await axios.get(
          "http://localhost:5000/data/paymentType"
        );
        this.paymentType = responsePaymentTypes.data;
        const responseCities = await axios.get(
          "http://localhost:5000/data/cities"
        );
        this.cities = responseCities.data;
        const responseBanks = await axios.get(
          "http://localhost:5000/data/banks"
        );
        this.banks = responseBanks.data;
        const responsePurposes = await axios.get(
          "http://localhost:5000/data/purposes"
        );
        this.purposes = responsePurposes.data;
      } catch (e) {
        alert("Error!");
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

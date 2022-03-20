<template>
  <div class="container mt-4">
    <div class="row">
      <label><b>You give</b></label>
      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_country">
          <option disabled value="">Choose country</option>
          <option
            v-for="country in countries"
            v-bind:key="country.country_name"
          >
            {{ country.country_name }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_currency">
          <option disabled value="">Choose currency</option>
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
          <option disabled value="">Choose payment method</option>
          <option v-for="type in paymentType" v-bind:key="type.type">
            {{ type.type }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <input
          class="form-control"
          placeholder="Amount"
          v-model.number="current_amount"
        />
      </div>
    </div>

    <div class="row mt-4">
      <label><b>You want</b></label>
      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_country">
          <option disabled value="">Choose country</option>
          <option
            v-for="country in countries"
            v-bind:key="country.country_name"
          >
            {{ country.country_name }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_currency">
          <option disabled value="">Choose currency</option>
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
          <option disabled value="">Choose payment method</option>
          <option v-for="type in paymentType" v-bind:key="type.type">
            {{ type.type }}
          </option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <input
          class="form-control"
          placeholder="Amount"
          v-model.number="wanted_amount"
        />
      </div>
    </div>

    <div>
      <button @click="send()" type="button" class="btn btn-primary mt-4">
        Create
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      countries: [],
      currencies: [],
      paymentType: [],
      current_country: "",
      current_type: "",
      current_currency: "",
      current_amount: "",
      wanted_country: "",
      wanted_type: "",
      wanted_currency: "",
      wanted_amount: "",
    };
  },
  methods: {
    send: function () {
      if (
        this.current_country === "" ||
        this.current_type === "" ||
        this.current_currency === "" ||
        this.current_amount === "" ||
        this.wanted_country === "" ||
        this.wanted_type === "" ||
        this.wanted_currency === "" ||
        this.wanted_amount === ""
      ) {
        this.error = "All fields required!";
        alert("All fields required!");
      } else {
        let data = {
          current_country: `${this.current_country}`,
          current_currency: `${this.current_currency}`,
          current_type: `${this.current_type}`,
          current_amount: `${this.current_amount}`,
          wanted_country: `${this.wanted_country}`,
          wanted_currency: `${this.wanted_currency}`,
          wanted_type: `${this.wanted_type}`,
          wanted_amount: `${this.wanted_amount}`,
        }
        axios.post("http://localhost:5000/request/create", data)
        .then(function (response){
          console.log(response)
          alert("Your request has been posted. As soon as a suitable offer appears, you will be notified.")
        })
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

<style>
.col-sm-3 {
  margin-right: 30;
  float: left;
}
</style>

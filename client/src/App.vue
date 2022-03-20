<template>
  <div class="container mt-4">
    <div class="row">
      <label><b>You give</b></label>
      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_country">
          <option disabled value="">Choose country</option>
          <option value="1">Россия</option>
          <option value="2">Турция</option>
          <option value="3">Эстония</option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_type">
          <option disabled value="">Choose payment method</option>
          <option value="1">Нал</option>
          <option value="2">Банковский счет</option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="current_currency">
          <option disabled value="">Choose currency</option>
          <option value="1">RUB</option>
          <option value="2">USD</option>
          <option value="3">BTC</option>
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
          <option value="1">Россия</option>
          <option value="2">Турция</option>
          <option value="3">Эстония</option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_type">
          <option disabled value="">Choose payment method</option>
          <option value="1">Cash</option>
          <option value="2">Visa/MasterCard</option>
          <option value="3">Blockchain</option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <select class="form-select" v-model="wanted_currency">
          <option disabled value="">Choose currency</option>
          <option value="1">RUB</option>
          <option value="2">USD</option>
          <option value="3">BTC</option>
        </select>
      </div>

      <div class="col-sm-3 mt-2">
        <input
          class="form-control"
          placeholder="Amount"
          v-model="wanted_amount"
        />
      </div>
    </div>
    <div>
      <button @click="send()" type="button" class="btn btn-primary mt-4">
        Создать заявку
      </button>
    </div>
  </div>
</template>

<script>
export default {
   data() {
    let data = {
      current_country: "",
      current_type: "",
      current_currency: "",
      current_amount: "",
      wanted_country: "",
      wanted_type: "",
      wanted_currency: "",
      wanted_amount: "",
    };
    return data;
  },
  methods: {
    send: function (submit) {
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
        this.error = "Заполните все поля!";
        alert("Заполните все поля!");
      } else {
    const requestOptions = {
    method: 'POST',
    mode: 'no-cors',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  };
  fetch('http://localhost:5000/request/create/', requestOptions)
    .then(async response => {
      const data = await response.json();
      if (!response.ok) {
        const error = (data && data.message) || response.status;
        return Promise.reject(error);
      }
    })
    .catch(error => {
      this.errorMessage = error;
      alert(error)
      console.error('There was an error!', error);
    });
      }
    }
  }
}
</script>

<style>
.col-sm-3 {
  margin-right: 30;
  float: left;
}
</style>

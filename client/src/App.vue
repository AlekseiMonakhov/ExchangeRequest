<template>
  <div class="container">
    <div class="row">
      <label><b>Отдаете</b></label>
      <div class="col-sm-3">
        <select class="form-select" v-model="current_country">
          <option disabled value="">Выберите страну</option>
          <option value="1">Россия</option>
          <option value="2">Турция</option>
          <option value="3">Эстония</option>
        </select>
      </div>

      <div class="col-sm-3">
        <select class="form-select" v-model="current_type">
          <option disabled value="">Выберите тип платежа</option>
          <option value="1">Нал</option>
          <option value="2">Банковский счет</option>
        </select>
      </div>

      <div class="col-sm-3">
        <select class="form-select" v-model="current_currency">
          <option disabled value="">Выберите валюту</option>
          <option value="1">RUB</option>
          <option value="2">USD</option>
          <option value="3">BTC</option>
        </select>
      </div>

      <div class="col-sm-3">
        <input
          type="amount"
          class="form-control"
          placeholder="Введите сумму"
          v-model="current_amount"
        />
      </div>
    </div>

    <div class="row">
      <label><b>Получаете</b></label>
      <div class="col-sm-3">
        <select class="form-select" v-model="wanted_country">
          <option disabled value="">Выберите страну</option>
          <option value="1">Россия</option>
          <option value="2">Турция</option>
          <option value="3">Эстония</option>
        </select>
      </div>

      <div class="col-sm-3">
        <select class="form-select" v-model="wanted_type">
          <option disabled value="">Выберите тип платежа</option>
          <option value="1">Нал</option>
          <option value="2">Банковский счет</option>
        </select>
      </div>

      <div class="col-sm-3">
        <select class="form-select" v-model="wanted_currency">
          <option disabled value="">Выберите валюту</option>
          <option value="1">RUB</option>
          <option value="2">USD</option>
          <option value="3">BTC</option>
        </select>
      </div>

      <div class="col-sm-3">
        <input
          type="amount"
          class="form-control"
          placeholder="Введите сумму"
          v-model="wanted_amount"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
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
};
</script>

<style>
.col-sm-3 {
  margin-right: 30;
  float: left;
}
</style>

<template>

  <div class="container-md-8">
    <div class="table-md">
      <th align="left"><strong>Вы получите</strong></th>
      <th align="center"><strong>Вы отдаете</strong></th>
    </div>
    <table class="table table-sm">
      <thead>
        <th scope="col" bgcolor="#add8e6" >Рейтинг</th>
        <th scope="col" bgcolor="#add8e6">Валюта</th>
        <th scope="col" bgcolor="#add8e6">Форма</th>
        <th scope="col" bgcolor="#add8e6">Банк</th>
        <th scope="col" bgcolor="#add8e6">Назначение</th>
        <th scope="col" bgcolor="#add8e6">Сумма</th>
        <th scope="col" bgcolor="#add8e6">Место</th>
        <th scope="col" bgcolor="#e0ffff">Валюта</th>
        <th scope="col" bgcolor="#e0ffff">Форма</th>
        <th scope="col" bgcolor="#e0ffff">Банк</th>
        <th scope="col" bgcolor="#e0ffff">Назначение</th>
        <th scope="col" bgcolor="#e0ffff">Сумма</th>
        <th scope="col" bgcolor="#e0ffff">Место</th>
        <th scope="col" bgcolor="#20b2aa">Дата</th>
        <th scope="col" bgcolor="#20b2aa">Вознаграждение</th>
        <th scope="col" bgcolor="#20b2aa">Связаться</th>
      </thead>
      <tbody>
      <tr v-for="request in requests">
        <td>4</td>
        <td>{{request.current_currency}}</td>
        <td>{{request.current_type}}</td>
        <td>{{request.current_bank}}</td>
        <td>{{request.current_purpose}}</td>
        <td>{{request.current_amount}}</td>
        <td>{{request.current_country}}</td>
        <td>{{request.wanted_currency}}</td>
        <td>{{request.wanted_type}}</td>
        <td>{{request.wanted_bank}}</td>
        <td>{{request.wanted_purpose}}</td>
        <td>{{request.wanted_amount}}</td>
        <td>{{request.wanted_country}}{{request.wanted_city}}</td>
        <td>{{request.created_on.replace(/T/, ' ').slice(0, -7)}}</td>
        <td> +1 %</td>
        <td> Кнопка чата </td>
      </tr>

      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RequestsList",
  data() {
    return {
      requests: []
    }
  },
  methods: {
    async getData() {
      try {
        const requests = await axios.get(
          "http://localhost:5000/request/getlist"
        );
        this.requests = requests.data;
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

</style>

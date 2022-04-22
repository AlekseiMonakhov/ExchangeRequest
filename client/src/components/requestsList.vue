<template>
  <div class="container-mt-4">
    <div class="table-sm-1">
      <th ><strong>Вы получите</strong></th>
      <th ><strong>Вы отдаете</strong></th>
    </div>
    <table class="table table-sm-2">
      <thead>
        <th class="col-1" >Рейтинг</th>
        <th class="col-1">Валюта</th>
        <th class="col-1">Форма</th>
        <th class="col-1">Банк</th>
        <th class="col-1">Назначение</th>
        <th class="col-1">Сумма</th>
        <th class="col-1">Место</th>
        <th class="col-2">Валюта</th>
        <th class="col-2">Форма</th>
        <th class="col-2">Банк</th>
        <th class="col-2">Назначение</th>
        <th class="col-2">Сумма</th>
        <th class="col-2">Место</th>
        <th class="col-3">Дата</th>
        <th class="col-3">Вознаграждение</th>
        <th class="col-3">Связаться</th>
      </thead>
      <tbody>
      <tr v-for="request in requests">
        <td>4</td>
        <td>{{request.current_currency}}</td>
        <td>{{request.current_type}}</td>
        <td>{{request.current_bank}}</td>
        <td>{{request.current_purpose}}</td>
        <td>{{request.current_amount}}</td>
        <td>{{request.current_country}}{{request.current_city}}</td>
        <td>{{request.wanted_currency}}</td>
        <td>{{request.wanted_type}}</td>
        <td>{{request.wanted_bank}}</td>
        <td>{{request.wanted_purpose}}</td>
        <td>{{request.wanted_amount}}</td>
        <td>{{request.wanted_country}}{{request.wanted_city}}</td>
        <td>{{request.created_on.replace(/T/, ' ').slice(0, -7)}}</td>
        <td> +1 %</td>
        <td>
          <button @click="$router.push('/startChat')" type="button" class="btn btn-primary">Чат</button></td>
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

.col-1 {
  background-color: #8383f5;
}.col-2 {
   background-color: #83f5e8;
 }.col-3 {
    background-color: rgba(213, 217, 139, 0.71);
  }

</style>

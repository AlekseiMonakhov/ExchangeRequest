<template>
  <div class="container">
    <div class="col-sm-3">
      <select class="form-select" aria-label="Default select example">
        <option selected>Выберите страну</option>
        <option value="1">Россия</option>
        <option value="2">Турция</option>
        <option value="3">Эстония</option>
      </select>
    </div>

    <div class="col-sm-3">
      <select class="form-select" aria-label="Default select example">
        <option selected>Выберите тип платежа</option>
        <option value="1">Нал</option>
        <option value="2">Банковский счет</option>
      </select>
    </div>

    <div class="col-sm-3">
      <select class="form-select" aria-label="Default select example">
        <option selected>Выберите валюту</option>
        <option value="1">RUB</option>
        <option value="2">USD</option>
        <option value="3">BTC</option>
      </select>
    </div>

    <div class="col-sm-3">
      <input type="amount" class="form-control" placeholder="Введите сумму" />
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.col-sm-3 {
  margin-right: 30;
  float: left;
}
</style>

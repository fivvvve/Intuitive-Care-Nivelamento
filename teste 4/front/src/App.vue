<script setup>
import { ref } from 'vue';
import api from './lib/Axios'

// ref variables
const text = ref("");
const type = ref("text");
const data = ref([]);
const modalOpened = ref(false);
const currOper = ref();

// function to search for data in api
function submit() {
  api.get("textual-search", {
    params: {
      text: text.value,
      type: type.value
    }
  }).then((response) => {
    // saves data return in variable data to be loaded on screen
    data.value = response.data;
  }).catch(() => {
    // sets data variable empty in case nothing was found
    data.value = [];
  });
}

// function to open modal and save the data of the current operadora
function openModal(oper) {
  currOper.value = oper;
  modalOpened.value = true;
}

// function to open modal and remove data from the current operadora
function closeModal() {
  modalOpened.value = false;
  currOper.value = undefined;
}

// function to format data to brazilian default
function formatDate(date) {
  return new Date(date).toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
  });
}

</script>

<template>

  <!-- loads modal in case variable modalOpened is true -->
  <div v-if="modalOpened" class="modal">
    <div class="modal-back"></div>

    <!-- loads all info from current operadora -->
    <div class="modal-info">
      <h2>Dados da Operadora</h2>
      <p>Registro ANS: {{ currOper.Registro_ANS }}</p>
      <p>Data de Registro: {{ formatDate(currOper.Data_Registro_ANS) }} </p>
      <p>Razão Social: {{ currOper.Razao_Social }}</p>
      <p>CNPJ: {{ currOper.CNPJ }}</p>
      <p>Nome Fantasia: {{ currOper.Nome_Fantasia ? currOper.Nome_Fantasia : "Não possui" }}</p>
      <p>Modalidade: {{ currOper.Modalidade }}</p>
      <p>Endereço: {{ currOper.Logradouro + " " + currOper.Numero + ", " + currOper.Bairro + (currOper.Complemento && ", " + currOper.Complemento) }}</p>
      <p>Cidade: {{ currOper.Cidade + " - " + currOper.UF }}</p>
      <p>CEP: {{ currOper.CEP }}</p>
      <p>Tel.: {{ (currOper.DDD && "(" + currOper.DDD + ") ") + (currOper.Telefone ? currOper.Telefone : "Não possui") }}</p>
      <p>Email: {{ currOper.Endereco_eletronico ? currOper.Endereco_eletronico : "Não possui" }}</p>
      <p>Representante: {{ currOper.Representante + ", " + currOper.Cargo_Representante }}</p>
      <p>Região de Comercialização: {{ currOper.Regiao_de_Comercializacao ? currOper.Regiao_de_Comercializacao : "Não informado" }}</p>

      <!-- button to close modal -->
      <button @click="closeModal">Fechar</button>
    </div>
  </div>

  <h1>Bem-vindo ao Intuitive Care Nivelamento Teste 4</h1>

  <div class="info">
    <p>Candidato: Thiago Fernandes Mendes da Silva</p>
    <p>Clique <a href="https://github.com/fivvvve/Intuitive-Care-Nivelamento" target="_blank">aqui</a> para acessar o código fonte</p>
  </div>
  
  <!-- form to search for data in api -->
  <form @submit.prevent="submit" method="get">
    <h2>Formulário para busca de operadoras</h2>

    <div class="form-group">
      <label for="text">Digite o que deseja buscar:</label>
      <input type="text" name="text" id="text" v-model="text" required>
    </div>

    <div class="form-group">
      <label for="type">O que seus dados descrevem:</label>
      <select name="type" id="type" v-model="type">
        <option value="text" selected>Dados Gerais</option>
        <option value="registro_ans">Registro ANS</option>
        <option value="cnpj">CNPJ</option>
        <option value="modalidade">Modalidade</option>
      </select>
    </div>

    <button>Buscar</button>

  </form>

  <!-- table that will show the data received from backend -->
  <table>
    <thead>
      <tr>
        <th class="small-column">Registro ANS</th>
        <th class="small-column">CNJP</th>
        <th class="large-column">Razão Social</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="oper in data" :key="oper.Registro_ANS">
        <td>{{ oper.Registro_ANS }}</td>
        <td>{{ oper.CNPJ }}</td>
        <td class="last-column-item"><span>{{ oper.Razao_Social }}</span>
          <v-icon name="co-fullscreen" class="fullscreen-icon" @click="openModal(oper)"/>
        </td>
      </tr>
    </tbody>
  </table>

  <!-- load this message in case any data was found -->
  <p v-if="!data.length">Nenhum dado para mostrar</p>
  
</template>

<style scoped>

h1 {
  text-align: center;
}

.info {
  margin: 30px 0;
}

.info p {
  margin: 0;
  padding: 0;
}


form {
  max-width: 80%;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  margin: 0 auto;
  border: 2px solid black;
  border-radius: 15px;
  padding: 30px;
  background-color: rgb(49, 49, 49);
}

form h2 {
  padding: 0;
  margin: 10px 0;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: start;
  gap: 5px;
}

.form-group input{
  width: 300px;
  outline: none;
  padding: 10px;
  border: 0;
  border-radius: 5px;

}

.form-group select{
  width: 320px;
  padding: 10px;
  outline: none;
  border: 0;
  border-radius: 5px;
}

table {
  margin: 50px auto;
  border-collapse: collapse;
  width: 80%;
}

table th {
  background-color: rgb(49, 49, 49);
}

table td, th {
  position: relative;
  border: 1px solid #dddddd;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: rgb(49, 49, 49);
}

.small-column {
  width: 100px;
}

.large-column {
  width: 250px;
}

.last-column-item {
  display: flex;
  align-items: center;
  justify-content: center;
}

.last-column-item span{
  display: inline-block;
  width: 80%;
}

.fullscreen-icon {
  cursor: pointer;
  position: absolute;
  right: 5px;
}

.modal {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.modal-back {
  position: fixed;
  width: 100vw;
  height: 100vh;
  background-color: black;
  opacity: 0.5;
}

.modal-info {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* Centraliza no meio */
  width: 500px;
  max-width: 80%;
  min-height: 200px;
  background-color: rgb(49, 49, 49);
  padding: 15px;
  border: 2px solid black;
  border-radius: 15px;
  overflow-y: auto;
  z-index: 2;
}

.modal-info h2 {
  padding: 0;
  margin: 15px 0;
}

.modal-info button {
  margin-top: 20px;
}

.modal-info p:first-of-type {
  border-top: 1px dashed #ddd;
}

.modal-info p {
  margin: 0;
  padding: 8px 0;
  border-bottom: 1px dashed #ddd;
}

</style>

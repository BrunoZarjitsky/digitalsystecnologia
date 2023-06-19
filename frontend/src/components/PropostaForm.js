import React, { useState } from 'react';
import axios from 'axios';
import '../styles/PropostaForm.css';

const PropostaForm = () => {
  const [data, setData] = useState({
    nome_completo: '',
    cpf: '',
    endereco: '',
    valor_emprestimo: '',
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://localhost:8000/api/propostas/nova/', data)
      .then((response) => {
        console.log(response.data);
        window.location.href = 'http://localhost:3000';
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleChange = (event) => {
    setData({ ...data, [event.target.name]: event.target.value });
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <div>
        <label htmlFor="nome_completo">Nome completo:</label>
        <input type="text" id="nome_completo" name="nome_completo" onChange={handleChange} />
      </div>
      <div>
        <label htmlFor="cpf">CPF (somente numeros):</label>
        <input type="text" id="cpf" name="cpf" onChange={handleChange} maxlength="11" minlength="11" placeholder="12345678901"/>
      </div>
      <div>
        <label htmlFor="endereco">Endereço:</label>
        <input type="text" id="endereco" name="endereco" onChange={handleChange} />
      </div>
      <div>
        <label htmlFor="valor_emprestimo">Valor do emprestimo:</label>
        <input type="number" id="valor_emprestimo" name="valor_emprestimo" onChange={handleChange} placeholder="0" />
      </div>
      <button type="submit">Enviar</button>
    </form>
  );
};

export default PropostaForm;

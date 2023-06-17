import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/PropostaList.css';

const PropostaList = () => {
  const [propostas, setPropostas] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/proposta/propostas/')
      .then((response) => {
        setPropostas(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h2>Lista de Propostas</h2>
      <ul className='proposta-list'>
        {propostas.reverse().map((proposta) => (
          <li key={proposta.id} class='proposta-item'>
            Proposta {proposta.id}: {proposta.cpf} - {proposta.valor_emprestimo} - {proposta.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PropostaList;

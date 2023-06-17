import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import PropostaPage from './views/NovaPropostaPage';
import ListaPropostasPage from './views/ListaPropostasPage';

function App() {
  return (
    <div className="App">
      <nav>
        <ul>
          <li>
            <Link to="/">Lista de Propostas</Link>
          </li>
          <li>
            <Link to="/nova_proposta">Nova Proposta</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<ListaPropostasPage/>} />
        <Route path="/nova_proposta" element={<PropostaPage/>} />
      </Routes>
    </div>
  );
}

export default App;

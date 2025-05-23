// src/pages/Home.jsx
import React, { useEffect, useState } from "react";
import axios from "axios";
import Swal from "sweetalert2";
import ReactDOM from "react-dom/client";
import CardHeroe from "../components/CardHeroe";
import Header from "../components/Header";
import HeroForm from "../components/HeroForm";

export default function Home() {
  const [heroes, setHeroes] = useState([]);
  const [filteredHeroes, setFilteredHeroes] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("http://localhost:8001/api/superheroes/")
      .then((res) => {
        setHeroes(res.data);
        setFilteredHeroes(res.data);
      })
      .catch((err) => {
        console.error(err);
        setError("Error al cargar los superhéroes.");
      });
  }, []);

  const handleSearch = (query) => {
    const filtered = heroes.filter(h =>
      h.name.toLowerCase().includes(query.toLowerCase()) ||
      (h.real_name && h.real_name.toLowerCase().includes(query.toLowerCase()))
    );
    setFilteredHeroes(filtered);
  };

  const handleCreate = () => {
    Swal.fire({
      title: "Agregar superhéroe",
      html: "<div id='form-container'></div>",
      didOpen: () => {
        const container = document.getElementById("form-container");
        ReactDOM.createRoot(container).render(
          <HeroForm onSave={handleCreateSubmit} />
        );
      },
      showConfirmButton: false,
      width: "800px"
    });
  };

  const handleCreateSubmit = (data) => {
    axios.post("http://localhost:8001/api/superheroes/", data)
      .then(() => {
        Swal.fire("Creado", "Superhéroe agregado correctamente", "success")
          .then(() => window.location.reload());
      })
      .catch(() => {
        Swal.fire("Error", "No se pudo crear", "error");
      });
  };

  return (
    <div>
      <Header onSearch={handleSearch} />

      <div className="container mt-4">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h1>Todos los Superhéroes</h1>
          <button className="btn btn-success" onClick={handleCreate}>
            + Agregar superhéroe
          </button>
        </div>

        {error && <div className="alert alert-danger">{error}</div>}

        <div className="row">
          {filteredHeroes.map((hero) => (
            <div className="col-md-4" key={hero.id}>
              <CardHeroe hero={hero} />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

import React, { useEffect, useState } from "react";
import axios from "axios";
import CardHeroe from "../components/CardHeroe";
import Header from "../components/Header";

export default function Marvel() {
  const [heroes, setHeroes] = useState([]);
  const [filteredHeroes, setFilteredHeroes] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("http://localhost:8001/api/superheroes/")
      .then((res) => {
        const marvelHeroes = res.data.filter(h => h.house === "Marvel");
        setHeroes(marvelHeroes);
        setFilteredHeroes(marvelHeroes);
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

  return (
    <div>
      <Header onSearch={handleSearch} />

      <div className="container mt-4">
        <h1 className="mb-4">Superhéroes de Marvel</h1>

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

// src/pages/HeroDetail.jsx
import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";
import Swal from "sweetalert2";
import ReactDOM from "react-dom/client";
import HeroForm from "../components/HeroForm";
import "../styles/detailStyles.css";

export default function HeroDetail() {
  const { id } = useParams();
  const [hero, setHero] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/api/superheroes/${id}/`)
      .then(res => setHero(res.data))
      .catch(() => setError("No se pudo cargar el héroe"));
  }, [id]);

  const handleDelete = () => {
    Swal.fire({
      title: "¿Estás seguro?",
      text: "Esta acción no se puede deshacer",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sí, eliminar",
      cancelButtonText: "Cancelar"
    }).then(result => {
      if (result.isConfirmed) {
        axios.delete(`http://localhost:8000/api/superheroes/${id}/`)
          .then(() => {
            Swal.fire("¡Eliminado!", "El superhéroe fue eliminado.", "success")
              .then(() => window.location.href = "/");
          })
          .catch(() => {
            Swal.fire("Error", "No se pudo eliminar", "error");
          });
      }
    });
  };

  const handleEdit = () => {
    Swal.fire({
      title: "Editar superhéroe",
      html: "<div id='form-container'></div>",
      didOpen: () => {
        const container = document.getElementById("form-container");
        ReactDOM.createRoot(container).render(
          <HeroForm initialData={hero} onSave={handleUpdate} />
        );
      },
      showConfirmButton: false,
      width: "800px"
    });
  };

  const handleUpdate = (data) => {
    axios.put(`http://localhost:8000/api/superheroes/${id}/`, data)
      .then(() => {
        Swal.fire("Actualizado", "Superhéroe editado correctamente", "success")
          .then(() => window.location.reload());
      })
      .catch(() => {
        Swal.fire("Error", "No se pudo actualizar", "error");
      });
  };

  if (error) return <div className="alert alert-danger">{error}</div>;
  if (!hero) return <div className="text-center mt-5">Cargando...</div>;

  return (
    <div className="container hero-detail mt-4">
      <h1 className="mb-3">{hero.name}</h1>

      {hero.house === "Marvel" ? (
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Marvel_Logo.svg/500px-Marvel_Logo.svg.png" alt="Marvel" style={{ height: "40px" }} />
      ) : (
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3d/DC_Comics_logo.svg" alt="DC" style={{ height: "40px" }} />
      )}

      {/* Carrusel */}
      <div id={`carousel-${hero.id}-detail`} className="carousel slide my-4" data-bs-ride="carousel">
        <div className="carousel-inner">
          {hero.images.map((img, idx) => (
            <div key={idx} className={`carousel-item ${idx === 0 ? "active" : ""}`}>
              <img src={img} className="d-block w-100" alt={`img-${idx}`} />
            </div>
          ))}
        </div>
        {hero.images.length > 1 && (
          <>
            <button className="carousel-control-prev" type="button" data-bs-target={`#carousel-${hero.id}-detail`} data-bs-slide="prev">
              <span className="carousel-control-prev-icon" />
            </button>
            <button className="carousel-control-next" type="button" data-bs-target={`#carousel-${hero.id}-detail`} data-bs-slide="next">
              <span className="carousel-control-next-icon" />
            </button>
          </>
        )}
      </div>

      <p><strong>Nombre real:</strong> {hero.real_name || "No especificado"}</p>
      <p><strong>Año de debut:</strong> {hero.debut_year}</p>
      <p><strong>Casa:</strong> {hero.house}</p>
      <p><strong>Biografía:</strong> {hero.biography}</p>
      <p><strong>Equipamiento:</strong> {hero.equipment || "Ninguno"}</p>

      <div className="mt-4 d-flex gap-3">
        <button className="btn btn-warning" onClick={handleEdit}>Editar</button>
        <button className="btn btn-danger" onClick={handleDelete}>Eliminar</button>
        <Link to="/" className="btn btn-secondary">Volver</Link>
      </div>
    </div>
  );
}

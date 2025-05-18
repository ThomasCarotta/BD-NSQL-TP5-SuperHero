// src/components/CardHeroe.jsx
import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/heroStyles.css";

export default function CardHeroe({ hero }) {
  const navigate = useNavigate();

  return (
    <div className="card mb-4" style={{ cursor: "default" }}>
      {hero.images.length > 1 ? (
        <div id={`carousel-${hero.id}`} className="carousel slide" data-bs-ride="carousel">
          <div className="carousel-inner">
            {hero.images.map((img, idx) => (
              <div key={idx} className={`carousel-item ${idx === 0 ? "active" : ""}`}>
                <img src={img} className="d-block w-100" alt={`${hero.name}-${idx}`} style={{ height: "200px", objectFit: "cover" }} />
              </div>
            ))}
          </div>
          <button className="carousel-control-prev" type="button" data-bs-target={`#carousel-${hero.id}`} data-bs-slide="prev">
            <span className="carousel-control-prev-icon" />
          </button>
          <button className="carousel-control-next" type="button" data-bs-target={`#carousel-${hero.id}`} data-bs-slide="next">
            <span className="carousel-control-next-icon" />
          </button>
        </div>
      ) : (
        <img
          src={hero.images[0]}
          className="card-img-top"
          alt={hero.name}
          style={{ height: "200px", objectFit: "cover" }}
        />
      )}

      <div className="card-body d-flex flex-column justify-content-between">
        <div>
          <h5 className="card-title">{hero.name}</h5>
          {hero.real_name && <h6 className="card-subtitle mb-2 text-muted">{hero.real_name}</h6>}
          <p className="card-text">
            {hero.biography ? hero.biography.slice(0, 100) + "..." : ""}
          </p>
        </div>

        <button className="btn btn-primary mt-3" onClick={() => navigate(`/detalle/${hero.id}`)}>
          Ver detalles
        </button>
      </div>
    </div>
  );
}

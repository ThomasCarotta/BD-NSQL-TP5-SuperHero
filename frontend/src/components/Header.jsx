import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Header({ onSearch }) {
  const navigate = useNavigate();

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <Link className="navbar-brand fw-bold text-white" to="/">Superhéroes App</Link>

      <div className="d-flex gap-3">
        <button className="btn btn-outline-light" onClick={() => navigate("/")}>Todos</button>
        <button className="btn btn-outline-light" onClick={() => navigate("/marvel")}>Marvel</button>
        <button className="btn btn-outline-light" onClick={() => navigate("/dc")}>DC</button>
      </div>

      <form className="d-flex ms-auto" onSubmit={e => e.preventDefault()}>
        <input
          type="text"
          className="form-control ms-3"
          placeholder="Buscar..."
          onChange={(e) => onSearch(e.target.value)}
        />
      </form>
    </nav>
  );
}

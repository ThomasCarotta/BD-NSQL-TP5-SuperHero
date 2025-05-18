// src/components/HeroForm.jsx
import React, { useState, useEffect } from "react";

export default function HeroForm({ initialData = {}, onSave }) {
  const [form, setForm] = useState({
    name: "",
    real_name: "",
    debut_year: "",
    house: "Marvel",
    biography: "",
    equipment: "",
    images: [""],
  });

  useEffect(() => {
    if (initialData.name) setForm(initialData);
  }, [initialData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleImageChange = (index, value) => {
    const newImages = [...form.images];
    newImages[index] = value;
    setForm({ ...form, images: newImages });
  };

  const addImageField = () => {
    setForm({ ...form, images: [...form.images, ""] });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(form);
  };

  return (
    <form onSubmit={handleSubmit}>
      {["name", "real_name", "debut_year", "biography", "equipment"].map((field) => (
        <div key={field} className="mb-3">
          <label className="form-label">{field.replace("_", " ")}</label>
          <input
            type={field === "debut_year" ? "number" : "text"}
            className="form-control"
            name={field}
            value={form[field]}
            onChange={handleChange}
          />
        </div>
      ))}

      <div className="mb-3">
        <label className="form-label">Casa</label>
        <select name="house" className="form-select" value={form.house} onChange={handleChange}>
          <option value="Marvel">Marvel</option>
          <option value="DC">DC</option>
        </select>
      </div>

      <div className="mb-3">
        <label className="form-label">Imágenes</label>
        {form.images.map((img, idx) => (
          <input
            key={idx}
            type="text"
            className="form-control mb-2"
            value={img}
            onChange={(e) => handleImageChange(idx, e.target.value)}
            placeholder={`Imagen ${idx + 1}`}
          />
        ))}
        <button type="button" className="btn btn-secondary btn-sm" onClick={addImageField}>
          + Agregar otra imagen
        </button>
      </div>

      <button type="submit" className="btn btn-primary mt-3">
        Guardar
      </button>
    </form>
  );
}

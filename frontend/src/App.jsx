import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import React from 'react';

import Marvel from "./pages/Marvel";
import DC from "./pages/DC";
import HeroDetail from "./components/HeroDetail";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/marvel" element={<Marvel />} />
        <Route path="/dc" element={<DC />} />
        <Route path="/detalle/:id" element={<HeroDetail />} />
      </Routes>
    </Router>
  );
}

export default App;

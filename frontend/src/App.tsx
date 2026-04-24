import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { TableProvider } from "./contexts/TableContext";
import Person from "./pages/Person";
import City from "./pages/City";

function App() {
  return (
    <TableProvider>
      <div className="app-container">
        <main className="app-main">
          <Routes>
            <Route path="/person" element={<Person />} />
            <Route path="/city" element={<City />} />
            <Route path="/" element={<Navigate to="/person" replace />} />
            <Route path="*" element={<Navigate to="/person" replace />} />
          </Routes>
        </main>
      </div>
    </TableProvider>
  );
}
export default App;

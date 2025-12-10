import { BrowserRouter, Routes, Route } from "react-router-dom";
import KPIs from "./pages/KPIs";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<KPIs />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
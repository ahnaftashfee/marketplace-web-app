import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Page1 from "./pages/login";
import Page2 from "./pages/cart"; 
import Page3 from "./pages/seller";
import SearchPage from "./pages/search"; 
import Page5 from "./pages/product";  

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Page1 />} />
        <Route path="/" element={<Page1 />} />
        <Route path="/cart" element={<Page2 />} />
        <Route path="/seller" element={<Page3 />} />
        <Route path="/search" element={<SearchPage />} /> 
        <Route path="/product" element={<Page5 />} /> 
        <Route path="/item/:id" element={<Page5 />} />
      </Routes>
    </Router>
  );
}
//jj testsset fjaiefjaeif
export default App;

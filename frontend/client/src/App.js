import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Provider } from "react-redux";

import HomePage from "pages/HomePage";
import RegisterPage from "pages/RegisterPage";
import LoginPage from "pages/LoginPage";
import DashboardPage from "pages/DashboardPage";

import { store } from "store";

const App = () => (
  <Provider store={store}>
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </Router>
  </Provider>
);

export default App;

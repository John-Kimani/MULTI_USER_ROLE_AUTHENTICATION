import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { checkAuth } from "features/user";

import HomePage from "pages/HomePage";
import RegisterPage from "pages/RegisterPage";
import LoginPage from "pages/LoginPage";
import DashboardPage from "pages/DashboardPage";

const App = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(checkAuth());
  }, []);
  return (
    <Router>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/dashboard" element={<DashboardPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
    </Routes>
  </Router>
  );
  };

export default App;

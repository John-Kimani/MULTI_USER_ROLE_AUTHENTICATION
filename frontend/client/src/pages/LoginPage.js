import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { resetRegistered } from "features/user";
import Layout from "components/Layout";

export const LoginPage = () => {

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(resetRegistered());
  })
    return (
      <Layout title="MultiUser Site | Login" content="Login page">
        <h1>LoginPage</h1>
      </Layout>
    );
  };
  
  
  export default LoginPage;
import { useState } from "react";
import Layout from "components/Layout";
import { Navigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { register } from "features/user";

export const RegisterPage = () => {
  const dispatch = useDispatch();

  const { registered, loading } = useSelector((state) => state.user);

  const [formData, setFormData] = useState({
    email: "",
    username: "",
    phone_number: "",
    password: "",
  });

  const { email, username, phone_number, password } = formData;

  const onChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();

    console.log('Register', email, username, phone_number, password)


    dispatch(register({ email, username, phone_number, password }));
  };

  if (registered) return <Navigate to="/login" />;

  return (
    <Layout title="MultiUser Site | Register" content="Register page">
      <h1>Register and Account</h1>
      <form className="mt-5" onSubmit={onSubmit}>
      <div className="form-group mt-3">
          <lable className="form-label" htmlFor="email">
            Email
          </lable>
          <input
            className="form-control"
            type="email"
            name="email"
            onChange={onChange}
            value={email}
            required
          />
        </div>

        <div className="form-group mt-3">
          <lable className="form-label" htmlFor="last_name">
            Username
          </lable>
          <input
            className="form-control"
            type="text"
            name="username"
            onChange={onChange}
            value={username}
            required
          />
        </div>

        <div className="form-group mt-3">
          <lable className="form-label" htmlFor="email">
            Phone Number
          </lable>
          <input
            className="form-control"
            name="phone_number"
            onChange={onChange}
            value={phone_number}
            required
          />
        </div>

        <div className="form-group mt-3">
          <lable className="form-label" htmlFor="password">
            Password
          </lable>
          <input
            className="form-control"
            type="password"
            name="password"
            onChange={onChange}
            value={password}
            required
          />
        </div>
        {loading ? (
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        ) : (
          <button className="btn btn-primary mt-4">Register</button>
        )}
      </form>
    </Layout>
  );
};

export default RegisterPage;

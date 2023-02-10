import { useSelector } from "react-redux";
import { Navigate } from "react-router-dom";
import Layout from "components/Layout";

export const DashboardPage = () => {
  const { isAuthenticated, user, loading } = useSelector((state) => state.user);

  if(!isAuthenticated && !loading && user == null) return <Navigate to='/login' /> 

  return (
    <Layout title="MultiUser Site | Dashboard" content="Dashboard page">
      {loading && user === null ? (
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
      ) : (
        <>
          <h1 className="mb-5">Dashboard</h1>
          <p>User Details</p>
          <ul>
            <li>Email: {user.email}</li>
            <li>Username: {user.username}</li>
            <li>Phone: {user.phone_number}</li>
          </ul>
        </>
      )}
    </Layout>
  );
};

export default DashboardPage;
